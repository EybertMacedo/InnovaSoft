<script setup>
import { ref, onMounted, onUnmounted, reactive } from 'vue'
import { Cpu, Code, Wrench, Server } from 'lucide-vue-next'

const getIconUrl = (slug) => {
  const overrides = {
    'css3': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg',
    'csharp': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg',
    'cvat': '/icons/cvat.svg',
    'unity': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/unity/unity-original.svg',
    'microsoftazure': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/azure/azure-original.svg',
    'azure': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/azure/azure-original.svg'
  }
  return overrides[slug] || `https://cdn.simpleicons.org/${slug}?v=1`
}



const rawCategories = [
  {
    title: 'Lenguajes de Programación',
    icon: Code,
    items: [
      { name: 'Python', percent: 95, slug: 'python' },
      { name: 'JavaScript', percent: 85, slug: 'javascript' },
      { name: 'TypeScript', percent: 80, slug: 'typescript' },
      { name: 'HTML', percent: 75, slug: 'html5' },
      { name: 'CSS', percent: 70, slug: 'css3' },
      { name: 'C#', percent: 55, slug: 'csharp' },
      { name: 'SQL', percent: 70, slug: 'postgresql' },
      { name: 'Bash', percent: 55, slug: 'gnubash' },
      { name: 'Go', percent: 20, slug: 'go' },
    ]
  },
  {
    title: 'Frameworks / Librerías',
    icon: Wrench,
    items: [
      { name: 'NumPy', percent: 85, slug: 'numpy' },
      { name: 'Pandas', percent: 85, slug: 'pandas' },
      { name: 'Scikit-learn', percent: 70, slug: 'scikitlearn' },
      { name: 'YOLOv8', percent: 80, slug: 'ultralytics' },
      { name: 'OpenCV', percent: 80, slug: 'opencv' },
      { name: 'LangChain', percent: 65, slug: 'langchain' },
      { name: 'FastAPI', percent: 70, slug: 'fastapi' },
      { name: 'Flask', percent: 40, slug: 'flask' },
      { name: 'Node.js', percent: 55, slug: 'nodedotjs' },
      { name: 'Angular', percent: 55, slug: 'angular' },
      { name: 'React', percent: 40, slug: 'react' },
      { name: 'Git', percent: 65, slug: 'git' },
      { name: 'Unity', percent: 55, slug: 'unity' },
      { name: 'n8n', percent: 60, slug: 'n8n' },
    ]
  },
  {
    title: 'DevOps / Infraestructura',
    icon: Server,
    items: [
      { name: 'Docker', percent: 60, slug: 'docker' },
      { name: 'Nginx', percent: 55, slug: 'nginx' },
      { name: 'Linux', percent: 75, slug: 'linux' },
      { name: 'DNS', percent: 65, slug: 'cloudflare' },
      { name: 'Droplets', percent: 65, slug: 'digitalocean' },
      { name: 'Azure', percent: 60, slug: 'microsoftazure' },
      { name: 'Vercel', percent: 75, slug: 'vercel' },
    ]
  }
]

// --- Estado Global ---
const categoryStates = reactive(rawCategories.map(cat => ({
  rotationAngle: 0,
  currentSpeed: 0.2, 
  targetSpeed: 0.2, 
  mouseX: 0, 
  mouseY: 0,
  items: [] 
})))

// --- Inicialización ---
rawCategories.forEach((cat, idx) => {
  const count = cat.items.length;
  // Radio reducido un poco para agruparlos mejor
  const radius = 125; 
  const phi = Math.PI * (3 - Math.sqrt(5)); 

  categoryStates[idx].items = cat.items.map((item, i) => {
    const y = 1 - (i / (count - 1)) * 2; 
    const radiusAtY = Math.sqrt(1 - y * y); 
    const theta = phi * i; 

    return { 
      ...item, 
      baseX: Math.cos(theta) * radiusAtY * radius,
      baseY: y * radius,
      baseZ: Math.sin(theta) * radiusAtY * radius,
      repelX: 0, 
      repelY: 0,
      currentZIndex: 10,
      isHovered: false 
    }
  })
})

// --- Physics Engine ---
let animationFrameId
const animate = () => {
  categoryStates.forEach((state) => {
    // 1. Inercia de Rotación (Frenado más agresivo: 0.1)
    state.currentSpeed += (state.targetSpeed - state.currentSpeed) * 0.1
    state.rotationAngle += state.currentSpeed

    const rad = state.rotationAngle * (Math.PI / 180)
    const cos = Math.cos(rad)
    const sin = Math.sin(rad)

    state.items.forEach(item => {
      // 2. Z-Index Dinámico
      const rotatedZ = item.baseZ * cos + item.baseX * sin
      item.currentZIndex = Math.floor(rotatedZ + 2000) // Base alta para evitar conflictos

      // 3. Física de Repulsión
      let targetRepelX = 0
      let targetRepelY = 0

      if (item.isHovered) {
        const currentX = item.baseX * cos - item.baseZ * sin
        const currentY = item.baseY 
        
        const dx = state.mouseX - currentX
        const dy = state.mouseY - currentY
        const dist = Math.sqrt(dx * dx + dy * dy) || 1

        // Reducimos la distancia de repulsión a 30px para que no se aleje demasiado
        const power = 30 
        targetRepelX = -(dx / dist) * power
        targetRepelY = -(dy / dist) * power
      }

      // Movimiento elástico
      item.repelX += (targetRepelX - item.repelX) * 0.1
      item.repelY += (targetRepelY - item.repelY) * 0.1
    })
  })

  animationFrameId = requestAnimationFrame(animate)
}

// --- Eventos ---
const onContainerMove = (e, index) => {
  const rect = e.currentTarget.getBoundingClientRect()
  categoryStates[index].mouseX = e.clientX - rect.left - rect.width / 2
  categoryStates[index].mouseY = e.clientY - rect.top - rect.height / 2
}

// AL ENTRAR: Velocidad 0 (Frenado Total)
const onContainerEnter = (index) => { categoryStates[index].targetSpeed = 0 }
// AL SALIR: Velocidad Normal
const onContainerLeave = (index) => { categoryStates[index].targetSpeed = 0.2 }

const onItemEnter = (catIndex, itemIndex) => {
  categoryStates[catIndex].items[itemIndex].isHovered = true
}
const onItemLeave = (catIndex, itemIndex) => {
  categoryStates[catIndex].items[itemIndex].isHovered = false
}

// --- Lifecycle ---
onMounted(() => {
  animationFrameId = requestAnimationFrame(animate)
})
onUnmounted(() => {
  cancelAnimationFrame(animationFrameId)
})

const getSize = (percent) => `${2.2 + (percent / 100) * 1.5}rem`
const getOpacity = (percent) => 0.85 + (percent / 100) * 0.15
const imageErrors = ref({})
const handleImageError = (name) => { imageErrors.value[name] = true }
</script>

<template>
  <section id="skills" class="py-24 px-6 relative z-10 scroll-mt-16 overflow-hidden">
    <div class="max-w-7xl mx-auto">
      <h2 class="text-3xl font-bold text-zinc-900 mb-20 flex items-center gap-3">
        <Cpu class="w-8 h-8 text-zinc-900" />
        Habilidades Técnicas
      </h2>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-24 lg:gap-12">
        <div 
          v-for="(catData, index) in categoryStates" 
          :key="index"
          class="flex flex-col items-center"
        >
          <div class="flex items-center gap-3 mb-10 text-zinc-500">
            <component :is="rawCategories[index].icon" class="w-5 h-5" />
            <h3 class="font-medium tracking-wider uppercase text-sm">{{ rawCategories[index].title }}</h3>
          </div>

          <div 
            class="scene-container w-full h-[350px] flex justify-center items-center perspective-container"
            @mouseenter="onContainerEnter(index)"
            @mouseleave="onContainerLeave(index)"
            @mousemove="(e) => onContainerMove(e, index)"
          >
            <div class="static-tilt preserve-3d">
              <div 
                class="sphere-rotator preserve-3d"
                :style="{ transform: `rotateY(${catData.rotationAngle}deg)` }"
              >
                <div 
                  v-for="(item, i) in catData.items" 
                  :key="item.name"
                  class="sphere-item absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 preserve-3d w-28 h-28 flex justify-center items-center cursor-pointer pointer-events-auto bg-white/0"
                  :style="{
                    transform: `translate3d(${item.baseX}px, ${item.baseY}px, ${item.baseZ}px)`,
                    zIndex: item.currentZIndex
                  }"
                  @mouseenter="onItemEnter(index, i)"
                  @mouseleave="onItemLeave(index, i)"
                >
                  
                  <div 
                    class="counter-rotator preserve-3d"
                    :style="{ transform: `rotateY(${-catData.rotationAngle}deg)` }"
                  >
                    
                    <div 
                      class="repulsion-layer transition-transform duration-75 ease-out pointer-events-none"
                      :style="{ transform: `translate(${item.repelX}px, ${item.repelY}px)` }"
                    >

                      <div class="static-untilt group relative flex justify-center items-center">
                        <div 
                          class="relative transition-all duration-300"
                          :class="{ 'scale-125': item.isHovered }"
                          :style="{ width: getSize(item.percent), height: getSize(item.percent), opacity: getOpacity(item.percent) }"
                        >
                          <img 
                            v-if="item.slug && !imageErrors[item.name]"
                            :src="getIconUrl(item.slug)" 
                            :alt="item.name"
                            class="w-full h-full object-contain filter grayscale brightness-90 opacity-90 transition-all duration-300"
                            :class="{ 'grayscale-0 brightness-100 opacity-100': item.isHovered }"
                            loading="lazy"
                            @error="handleImageError(item.name)" 
                          />
                          <div 
                            v-else 
                            class="w-full h-full flex items-center justify-center bg-zinc-200 rounded-full border border-zinc-300 text-[10px] font-bold text-zinc-700 text-center p-1 leading-tight"
                            :class="{ 'bg-white shadow-md': item.isHovered }"
                          >
                            {{ item.name }}
                          </div>
                        </div>

                        <div 
                          class="absolute -bottom-10 transition-opacity bg-zinc-900 text-white text-xs px-2 py-1 rounded whitespace-nowrap z-50 shadow-lg font-medium"
                          :class="item.isHovered ? 'opacity-100' : 'opacity-0'"
                        >
                          {{ item.name }}
                        </div>
                      </div>

                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.perspective-container {
  perspective: 1000px;
}

.preserve-3d {
  transform-style: preserve-3d;
}

.static-tilt, 
.sphere-rotator, 
.counter-rotator,
.repulsion-layer {
  pointer-events: none; 
}

.static-tilt {
  width: 100%;
  height: 100%;
  position: relative;
  transform: rotateX(10deg);
}

.sphere-rotator {
  width: 100%;
  height: 100%;
  position: relative;
}

.static-untilt {
  transform: rotateX(-10deg);
}
</style>