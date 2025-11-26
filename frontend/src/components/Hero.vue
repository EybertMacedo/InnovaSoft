<script setup>
import { ref, nextTick, onMounted } from 'vue'
import { ChevronRight, Github } from 'lucide-vue-next'

const isShimmering = ref(false)

const triggerShimmer = async () => {
  isShimmering.value = false
  await nextTick()
  setTimeout(() => {
    isShimmering.value = true
  }, 100)
}

const scrollToProjects = () => {
  document.getElementById('projects')?.scrollIntoView({ behavior: 'smooth' })
}

onMounted(() => {
  triggerShimmer()
})

defineExpose({ triggerShimmer })
const githubUrl = import.meta.env.VITE_GITHUB_URL || 'https://github.com/EybertMacedo'
</script>

<template>
  <header class="relative min-h-screen flex items-center justify-center pt-20 pb-20 px-6 overflow-hidden">
    <div class="max-w-7xl mx-auto relative z-10 text-center">

      
      <div class="mb-8 relative inline-block">
        <div class="absolute inset-0 bg-gradient-to-tr from-blue-500 to-purple-500 rounded-full blur-lg opacity-20 animate-pulse"></div>
        <img 
          src="/founder.jpg" 
          alt="Eybert Alexis Macedo Pillco" 
          class="w-32 h-32 md:w-40 md:h-40 rounded-full object-cover border-4 border-white shadow-xl relative z-10"
        />
      </div>
      
      <h1 
        class="text-5xl md:text-7xl font-bold tracking-tight mb-6"
        :class="{ 'glass-text-effect': isShimmering }"
      >
        Eybert Alexis <span class="font-light">Macedo Pillco</span>
      </h1>
      
      <p class="text-xl text-zinc-500 max-w-2xl mx-auto mb-10 leading-relaxed">
        AI/ML Engineer & Data Scientist. Especializado en transformar operaciones de negocio con Inteligencia Artificial, Computer Vision y LLMs.
      </p>
      
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <button 
          @click="scrollToProjects"
          class="flex items-center justify-center gap-2 bg-zinc-900 hover:bg-zinc-800 text-white px-8 py-3 font-medium transition-all duration-300 hover:shadow-lg rounded-none"
        >
          Explorar Soluciones
          <ChevronRight class="w-4 h-4" />
        </button>
        <a 
          :href="githubUrl" 
          target="_blank" 
          rel="noopener noreferrer"
          class="flex items-center justify-center gap-2 bg-white hover:bg-zinc-50 text-zinc-900 px-8 py-3 font-medium border border-zinc-200 transition-all duration-300 hover:shadow-md rounded-none"
        >
          <Github class="w-4 h-4" />
          Ver Código
        </a>
      </div>
    </div>
  </header>
</template>
