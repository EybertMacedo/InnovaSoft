<script setup>
import { ref, onMounted, onUnmounted, watch, nextTick } from 'vue'
import { 
  Cpu,
  Scan, 
  AlertTriangle, 
  HardHat, 
  Activity, 
  Play, 
  Pause,
  MessageSquare, 
  Send, 
  BarChart3 
} from 'lucide-vue-next'

// Computer Vision Models
const models = [
  {
    id: 'bar_jam',
    name: 'Steel Bar Jam',
    description: 'Identifica pausas de producción y atasco de material.',
    icon: AlertTriangle,
    color: 'text-amber-500',
    video: '/demos/cobbles_output.mp4',
    stats: { accuracy: '93.2%', latency: '12ms', fps: '60' }
  },
  {
    id: 'safety',
    name: 'Danger Zone',
    description: 'Monitorea áreas restringidas y detecta personal no autorizado.',
    icon: Scan,
    color: 'text-red-500',
    video: '/demos/risk_output.mp4',
    stats: { accuracy: '90.8%', latency: '18ms', fps: '58' }
  },
  {
    id: 'ppe',
    name: 'PPE Detection',
    description: 'Detecta equipo de protección personal en tiempo real.',
    icon: HardHat,
    color: 'text-blue-500',
    video: '/demos/ppe_output.mp4',
    stats: { accuracy: '92.5%', latency: '15ms', fps: '60' }
  }
]

const selectedModel = ref(models[0])
const isPlaying = ref(false)
const videoRef = ref(null)
const sectionRef = ref(null)
const confidence = ref(0)
const processing = ref(true)

// Simulation Loop
let interval
const startSimulation = () => {
  interval = setInterval(() => {
    confidence.value = Math.floor(Math.random() * (93 - 85 + 1) + 85)
  }, 800)
}

const selectModel = (model) => {
  selectedModel.value = model
  processing.value = true
  setTimeout(() => {
    processing.value = false
  }, 1000)
}

// Watch for model changes to reload video
watch(selectedModel, async () => {
  await nextTick()
  if (videoRef.value) {
    videoRef.value.load()
    if (isPlaying.value) {
      videoRef.value.play().catch(e => console.error("Autoplay failed:", e))
    }
  }
})

const togglePlay = () => {
  if (videoRef.value) {
    if (isPlaying.value) {
      videoRef.value.pause()
    } else {
      videoRef.value.play()
    }
    isPlaying.value = !isPlaying.value
  }
}

// Chat Simulator
const chatMessages = ref([
  { id: 1, text: '¡Hola! Soy la IA de InnovaSoft. Pregúntame sobre mis proyectos, habilidades o experiencia.', sender: 'bot' }
])
const chatInput = ref('')
const isTyping = ref(false)

const sendMessage = async () => {
  if (!chatInput.value.trim() || isTyping.value) return
  
  const userText = chatInput.value
  
  chatMessages.value.push({
    id: Date.now(),
    text: userText,
    sender: 'user'
  })
  chatInput.value = ''
  
  isTyping.value = true
  
  try {
    const apiUrl = import.meta.env.VITE_API_URL || '';
    const response = await fetch(`${apiUrl}/api/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        message: userText,
        session_id: 'demo-session'
      })
    })

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}))
      throw new Error(errorData.detail || 'Error desconocido en el servidor')
    }

    const data = await response.json()
    
    chatMessages.value.push({
      id: Date.now() + 1,
      text: data.response,
      sender: 'bot'
    })
  } catch (error) {
    console.error(error)
    let errorMessage = 'Lo siento, hubo un error al conectar con mi cerebro digital.'
    if (error.message && error.message !== 'Error en la respuesta') {
       errorMessage += ` Detalles: ${error.message}`
    }
    
    chatMessages.value.push({
      id: Date.now() + 1,
      text: errorMessage,
      sender: 'bot'
    })
  } finally {
    isTyping.value = false
  }
}

// Mini Browser
const browserUrl = ref('https://sentidata-dashboard.vercel.app/')
const currentUrl = ref('https://sentidata-dashboard.vercel.app/')
const iframeKey = ref(0)

const navigateTo = () => {
  window.open(currentUrl.value, '_blank')
}

onMounted(() => {
  startSimulation()
  
  let hasInitialized = false
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !hasInitialized) {
        hasInitialized = true
        // Show loading overlay for 1.5 seconds
        setTimeout(() => {
          processing.value = false
          // Start video playback
          if (videoRef.value) {
            videoRef.value.muted = true
            videoRef.value.play()
              .then(() => {
                isPlaying.value = true
              })
              .catch(e => console.error('Autoplay failed:', e))
          }
        }, 1500)
      }
    })
  }, { threshold: 0.3 })
  
  if (sectionRef.value) {
    observer.observe(sectionRef.value)
  }
})

onUnmounted(() => {
  clearInterval(interval)
})
</script>

<template>
  <section id="demos" ref="sectionRef" class="py-24 px-6 bg-zinc-900 relative overflow-hidden">
    <!-- Background Grid -->
    <div class="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px]"></div>
    
    <div class="max-w-7xl mx-auto relative z-10">
      <div class="mb-12">
        <h2 class="text-3xl font-bold text-white mb-4 flex items-center gap-3">
          <Cpu class="w-8 h-8 text-blue-500" />
          Interactive Demo Center
        </h2>
        <p class="text-zinc-400 max-w-2xl">
          Experimenta nuestras soluciones de IA en acción. Desde modelos de visión por computadora hasta asistentes inteligentes.
        </p>
      </div>

      <!-- Computer Vision Demo -->
      <div class="max-w-5xl mx-auto w-full mb-4">
        <h3 class="text-xl font-semibold text-white mb-2">Visión Artificial en Tiempo Real</h3>
        <p class="text-zinc-400 text-sm max-w-2xl">
          Detecta objetos, analiza peligros y monitorea la seguridad industrial con nuestros modelos de alta precisión y baja latencia.
        </p>
      </div>
      <div class="grid lg:grid-cols-12 gap-8 h-[600px] mb-16 max-w-5xl mx-auto w-full">
        <!-- Sidebar Controls -->
        <div class="lg:col-span-3 flex flex-col gap-4">
          <button
            v-for="model in models"
            :key="model.id"
            @click="selectModel(model)"
            class="p-4 rounded-xl border transition-all duration-300 text-left group relative overflow-hidden"
            :class="selectedModel.id === model.id
              ? 'bg-zinc-800 border-blue-500/50 shadow-[0_0_20px_rgba(59,130,246,0.15)]'
              : 'bg-zinc-900/50 border-zinc-800 hover:bg-zinc-800 hover:border-zinc-700'"
          >
            <div class="relative z-10">
              <div class="flex items-center justify-between mb-2">
                <component :is="model.icon" class="w-6 h-6" :class="model.color" />
                <div v-if="selectedModel.id === model.id" class="flex items-center gap-1.5">
                  <span class="relative flex h-2 w-2">
                    <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
                    <span class="relative inline-flex rounded-full h-2 w-2 bg-green-500"></span>
                  </span>
                  <span class="text-[10px] font-mono text-green-500 uppercase tracking-wider">Active</span>
                </div>
              </div>
              <h3 class="text-white font-medium mb-1">{{ model.name }}</h3>
              <p class="text-xs text-zinc-500 line-clamp-2">{{ model.description }}</p>
            </div>
          </button>

          <!-- Stats Card -->
          <div class="mt-auto p-4 bg-zinc-950/50 rounded-xl border border-zinc-800">
            <h4 class="text-xs font-mono text-zinc-500 uppercase mb-3">Model Performance</h4>
            <div class="grid grid-cols-3 gap-2">
              <div class="text-center">
                <div class="text-lg font-bold text-white">{{ selectedModel.stats.accuracy }}</div>
                <div class="text-[10px] text-zinc-500">Accuracy</div>
              </div>
              <div class="text-center border-l border-zinc-800">
                <div class="text-lg font-bold text-white">{{ selectedModel.stats.latency }}</div>
                <div class="text-[10px] text-zinc-500">Latency</div>
              </div>
              <div class="text-center border-l border-zinc-800">
                <div class="text-lg font-bold text-white">{{ selectedModel.stats.fps }}</div>
                <div class="text-[10px] text-zinc-500">FPS</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Main Viewport -->
        <div class="lg:col-span-9 relative rounded-2xl overflow-hidden bg-black border border-zinc-800 shadow-2xl group">
          <!-- Video Player -->
          <video
            ref="videoRef"
            :src="selectedModel.video"
            class="w-full h-full object-cover opacity-80"
            loop
            muted
            autoplay
            playsinline
          ></video>

          <!-- Overlay UI -->
          <div class="absolute inset-0 pointer-events-none p-6 flex flex-col justify-between">
            <!-- Top Bar -->
            <div class="flex items-start justify-between">
              <div class="bg-black/60 backdrop-blur-md rounded-lg p-2 border border-white/10 flex items-center gap-3">
                <div class="flex items-center gap-2 px-2 border-r border-white/10">
                  <span class="w-2 h-2 rounded-full bg-red-500 animate-pulse"></span>
                  <span class="text-xs font-mono text-white">LIVE FEED</span>
                </div>
                <div class="text-xs font-mono text-zinc-400">
                  CAM_01 • {{ selectedModel.name.toUpperCase() }}
                </div>
              </div>
              
              <div class="bg-black/60 backdrop-blur-md rounded-lg p-2 border border-white/10">
                <div class="text-xs font-mono text-green-400 flex items-center gap-2">
                  <Activity class="w-4 h-4" />
                  SYSTEM ONLINE
                </div>
              </div>
            </div>

            <!-- Center Loading State -->
            <div v-if="processing" class="absolute inset-0 flex items-center justify-center bg-black/80 backdrop-blur-sm z-20 transition-opacity duration-300">
              <div class="flex flex-col items-center gap-3">
                <div class="w-12 h-12 border-4 border-blue-500 border-t-transparent rounded-full animate-spin"></div>
                <div class="text-sm font-mono text-blue-400 animate-pulse">LOADING MODEL...</div>
              </div>
            </div>

            <!-- Bottom Bar -->
            <div class="flex items-end justify-between">
              <!-- Controls -->
              <div class="flex gap-2 pointer-events-auto">
                <button @click="togglePlay" class="p-3 bg-white/10 hover:bg-white/20 backdrop-blur-md rounded-lg text-white transition-colors">
                  <component :is="isPlaying ? Pause : Play" class="w-5 h-5" />
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Chat and Metrics -->
      <div class="grid grid-cols-1 gap-12 max-w-5xl mx-auto w-full">
        <!-- Chat Simulator -->
        <div>
          <div class="mb-4">
            <h3 class="text-xl font-semibold text-white mb-2">Asistente de IA Conversacional</h3>
            <p class="text-zinc-400 text-sm max-w-2xl">
              Interactúa con nuestro agente inteligente capaz de responder preguntas técnicas, asistir en tareas complejas y mantener el contexto de la conversación.
            </p>
          </div>
          <div class="bg-zinc-800/50 backdrop-blur-xl border border-zinc-700 rounded-xl overflow-hidden flex flex-col h-[500px] shadow-lg hover:shadow-2xl transition-all duration-500">
          <div class="p-4 border-b border-zinc-700 bg-zinc-900/50 flex items-center justify-between">
            <span class="font-semibold text-white flex items-center gap-2">
              <MessageSquare class="w-4 h-4 text-blue-500" />
              InnovaSoft AI Assistant
            </span>
            <span class="text-xs text-emerald-400 flex items-center gap-1">
              <span class="w-2 h-2 bg-emerald-500 rounded-full animate-pulse"></span>
              Online
            </span>
          </div>
          
          <div class="flex-1 p-4 overflow-y-auto space-y-4 scrollbar-thin scrollbar-thumb-zinc-600/50">
            <TransitionGroup name="message">
              <div 
                v-for="msg in chatMessages" 
                :key="msg.id"
                :class="['max-w-[80%] p-3 text-sm border rounded-lg backdrop-blur-sm', msg.sender === 'user' ? 'ml-auto bg-blue-600/90 text-white border-blue-500/50' : 'bg-zinc-700/60 text-zinc-100 border-zinc-600/50']"
              >
                {{ msg.text }}
              </div>
            </TransitionGroup>
            
            <div v-if="isTyping" class="bg-zinc-700/60 border border-zinc-600/50 text-zinc-300 p-3 inline-block text-xs animate-pulse rounded-lg backdrop-blur-sm">
              Escribiendo...
            </div>
          </div>
          
          <div class="p-4 border-t border-zinc-700 bg-zinc-900/50 flex gap-2">
            <input 
              v-model="chatInput" 
              @keyup.enter="sendMessage"
              type="text" 
              placeholder="Escribe un mensaje..." 
              class="flex-1 bg-zinc-800/50 border border-zinc-700 px-4 py-2 text-sm text-white focus:outline-none focus:bg-zinc-800 focus:border-blue-500 transition-all placeholder:text-zinc-500 rounded-lg"
            >
            <button 
              @click="sendMessage"
              class="bg-blue-600 hover:bg-blue-500 text-white p-2 transition-colors rounded-lg shadow-lg"
            >
              <Send class="w-4 h-4" />
            </button>
          </div>
        </div>
        </div>

        <!-- Live Dashboard Preview -->
        <div>
          <div class="mb-4">
            <h3 class="text-xl font-semibold text-white mb-2">Visualización de Datos en Vivo</h3>
            <p class="text-zinc-400 text-sm max-w-2xl">
              Monitorea métricas críticas y análisis de percepción ciudadana en tiempo real a través de nuestra plataforma SentiData.
            </p>
          </div>
          <div class="bg-zinc-900/40 backdrop-blur-xl border border-white/5 rounded-2xl overflow-hidden relative h-[500px] shadow-2xl hover:shadow-blue-500/10 transition-all duration-500 group">
          <!-- Full Video Background -->
          <div class="absolute inset-0">
            <video 
              src="/demos/sentidata_preview.mp4" 
              class="w-full h-full object-cover opacity-80 group-hover:opacity-100 group-hover:scale-105 transition-all duration-700 ease-out"
              autoplay 
              loop 
              muted 
              playsinline
            ></video>
            
            <!-- Cinematic Gradient Overlay -->
            <div class="absolute inset-0 bg-gradient-to-t from-zinc-950 via-zinc-900/50 to-transparent"></div>
          </div>

          <!-- Content Overlay -->
          <div class="absolute bottom-0 left-0 right-0 p-8 z-10">
            <div class="flex items-end justify-between gap-4">
              <div>
                <h3 class="text-2xl font-bold text-white mb-2 flex items-center gap-3">
                  SentiData
                  <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-green-500/20 text-green-400 border border-green-500/30 backdrop-blur-sm">LIVE</span>
                </h3>
                <p class="text-sm text-zinc-300 leading-relaxed font-light max-w-xl">
                  SentiData es un proyecto que emplea Inteligencia Artificial para recoger y analizar la percepción ciudadana sobre el sector saneamiento, convirtiéndola en una herramienta estratégica para la mejora continua de los servicios públicos.
                </p>
              </div>
              
              <a 
                href="https://sentidata-dashboard.vercel.app/" 
                target="_blank"
                class="shrink-0 text-xs font-medium bg-blue-600 hover:bg-blue-500 text-white px-4 py-2 rounded-full transition-all flex items-center gap-2 shadow-lg shadow-blue-900/20 hover:shadow-blue-500/40 hover:-translate-y-0.5"
              >
                Ver sitio en vivo
                <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
              </a>
            </div>
          </div>
        </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.message-enter-active,
.message-leave-active {
  transition: all 0.3s ease;
}
.message-enter-from,
.message-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>
