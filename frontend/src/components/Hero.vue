<script setup>
import { ref, nextTick, onMounted } from 'vue'
import { ChevronRight, Github, Linkedin } from 'lucide-vue-next'

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
const linkedinUrl = 'https://www.linkedin.com/in/emacedop/'
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
        <a 
          href="https://orcid.org/0000-0001-5802-4054" 
          target="_blank" 
          rel="noopener noreferrer"
          class="flex items-center justify-center gap-2 bg-white hover:bg-zinc-50 text-zinc-900 px-8 py-3 font-medium border border-zinc-200 transition-all duration-300 hover:shadow-md rounded-none"
        >
          <svg viewBox="0 0 24 24" class="w-4 h-4" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 0C5.372 0 0 5.372 0 12s5.372 12 12 12 12-5.372 12-12S18.628 0 12 0zM7.369 4.378c.525 0 .947.431.947.947s-.422.947-.947.947a.95.95 0 0 1-.947-.947c0-.525.422-.947.947-.947zm-.722 3.038h1.444v10.041H6.647V7.416zm3.562 0h3.9c3.712 0 5.344 2.653 5.344 5.025 0 2.578-2.016 5.025-5.325 5.025h-3.919V7.416zm1.444 1.303v7.444h2.297c3.272 0 4.022-2.484 4.022-3.722 0-2.016-1.284-3.722-4.097-3.722h-2.222z" fill="#A6CE39"/>
          </svg>
          ORCID
        </a>
        <a 
          :href="linkedinUrl" 
          target="_blank" 
          rel="noopener noreferrer"
          class="flex items-center justify-center gap-2 bg-white hover:bg-zinc-50 text-zinc-900 px-8 py-3 font-medium border border-zinc-200 transition-all duration-300 hover:shadow-md rounded-none"
        >
          <Linkedin class="w-4 h-4" />
          LinkedIn
        </a>
      </div>
    </div>
  </header>
</template>
