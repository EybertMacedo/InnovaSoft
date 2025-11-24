<script setup>
import { ref } from 'vue'
import { ExternalLink, Github, Code2, Terminal, Cpu, Globe, Database } from 'lucide-vue-next'

const projects = ref([
  {
    title: 'SafetyMind AI',
    description: 'Sistema de visión artificial para detección de EPPs en tiempo real en minería.',
    tags: ['YOLOv8', 'Python', 'OpenCV'],
    image: 'https://images.unsplash.com/photo-1581092921461-eab62e97a783?q=80&w=2070&auto=format&fit=crop',
    link: '#',
    github: '#'
  },
  {
    title: 'GeoHousing Data',
    description: 'Plataforma de análisis predictivo para el mercado inmobiliario usando Big Data.',
    tags: ['Pandas', 'Scikit-learn', 'Vue.js'],
    image: 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?q=80&w=2073&auto=format&fit=crop',
    link: '#',
    github: '#'
  },
  {
    title: 'InnovaBot RAG',
    description: 'Asistente virtual inteligente con memoria contextual para soporte técnico.',
    tags: ['LangChain', 'OpenAI', 'FastAPI'],
    image: 'https://images.unsplash.com/photo-1531746790731-6c087fecd65a?q=80&w=2006&auto=format&fit=crop',
    link: '#',
    github: '#'
  },
  {
    title: 'Industrial IoT Dashboard',
    description: 'Monitoreo de sensores industriales con visualización en tiempo real.',
    tags: ['MQTT', 'InfluxDB', 'Grafana'],
    image: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=2070&auto=format&fit=crop',
    link: '#',
    github: '#'
  },
  {
    title: 'Smart Logistics',
    description: 'Optimización de rutas de entrega usando algoritmos genéticos.',
    tags: ['Python', 'Google Maps API', 'React'],
    image: 'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=2070&auto=format&fit=crop',
    link: '#',
    github: '#'
  },
  {
    title: 'Crypto Sentiment',
    description: 'Análisis de sentimiento en redes sociales para predicción de criptomonedas.',
    tags: ['NLP', 'Twitter API', 'TensorFlow'],
    image: 'https://images.unsplash.com/photo-1518546305927-5a555bb7020d?q=80&w=2069&auto=format&fit=crop',
    link: '#',
    github: '#'
  },
  {
    title: 'AutoInvoice OCR',
    description: 'Automatización de facturas usando OCR y extracción de entidades.',
    tags: ['Tesseract', 'Spacy', 'Django'],
    image: 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?q=80&w=2072&auto=format&fit=crop',
    link: '#',
    github: '#'
  }
])
</script>

<template>
  <section id="projects" class="py-24 px-6 relative z-10 scroll-mt-24">
    <div class="max-w-7xl mx-auto">
      <div class="flex flex-col md:flex-row justify-between items-end mb-16 gap-6">
        <div>
          <h2 class="text-3xl md:text-4xl font-bold text-zinc-900 mb-4 flex items-center gap-3">
            <Code2 class="w-8 h-8 text-zinc-900" />
            Proyectos Destacados
          </h2>
          <p class="text-zinc-500 max-w-xl">
            Una selección de soluciones tecnológicas aplicadas a problemas reales, desde visión artificial hasta análisis predictivo.
          </p>
        </div>
        <a href="https://github.com/EybertMacedo" target="_blank" class="text-zinc-900 font-medium hover:underline flex items-center gap-2 group">
          Ver todos en GitHub
          <ExternalLink class="w-4 h-4 transition-transform group-hover:translate-x-1" />
        </a>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div 
          v-for="(project, index) in projects" 
          :key="index"
          class="group relative bg-white border border-zinc-200 overflow-hidden hover:shadow-xl transition-all duration-500 rounded-none flex flex-col h-full"
        >
          <!-- Image Container -->
          <div class="relative h-48 overflow-hidden">
            <div class="absolute inset-0 bg-zinc-900/10 group-hover:bg-zinc-900/0 transition-colors z-10"></div>
            <img 
              :src="project.image" 
              :alt="project.title" 
              class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700"
            />
          </div>

          <!-- Content -->
          <div class="p-6 flex flex-col flex-1">
            <h3 class="text-xl font-bold text-zinc-900 mb-2 group-hover:text-zinc-700 transition-colors">
              {{ project.title }}
            </h3>
            <p class="text-zinc-500 text-sm mb-6 flex-1">
              {{ project.description }}
            </p>

            <!-- Tags -->
            <div class="flex flex-wrap gap-2 mb-6">
              <span 
                v-for="tag in project.tags" 
                :key="tag"
                class="px-2 py-1 bg-zinc-100 text-zinc-600 text-xs font-medium border border-zinc-200"
              >
                {{ tag }}
              </span>
            </div>

            <!-- Links -->
            <div class="flex items-center gap-4 pt-4 border-t border-zinc-100 mt-auto">
              <a :href="project.link" class="flex items-center gap-2 text-sm font-medium text-zinc-900 hover:text-zinc-600 transition-colors">
                <Globe class="w-4 h-4" />
                Demo
              </a>
              <a :href="project.github" class="flex items-center gap-2 text-sm font-medium text-zinc-900 hover:text-zinc-600 transition-colors">
                <Github class="w-4 h-4" />
                Código
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
