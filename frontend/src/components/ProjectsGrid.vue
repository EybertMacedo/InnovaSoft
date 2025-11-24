<script setup>
import { ref } from 'vue'
import { 
  Terminal, 
  Cpu, 
  Globe, 
  Shield, 
  Database, 
  Code2, 
  BarChart3, 
  X,
  ExternalLink
} from 'lucide-vue-next'

const projects = [
  {
    title: 'SafetyMind AI',
    desc: 'Sistema de visión artificial para detección de EPPs en tiempo real en minería.',
    icon: Shield,
    status: 'Production',
    tech: ['YOLOv8', 'Python', 'OpenCV']
  },
  {
    title: 'GeoHousing Data',
    desc: 'Plataforma de análisis predictivo para el mercado inmobiliario usando Big Data.',
    icon: Database,
    status: 'Beta',
    tech: ['Pandas', 'Scikit-learn', 'Vue.js']
  },
  {
    title: 'InnovaBot RAG',
    desc: 'Asistente virtual inteligente con memoria contextual para soporte técnico.',
    icon: Terminal,
    status: 'Active',
    tech: ['LangChain', 'OpenAI', 'FastAPI']
  },
  {
    title: 'Industrial IoT Dashboard',
    desc: 'Monitoreo de sensores industriales con visualización en tiempo real.',
    icon: BarChart3,
    status: 'Production',
    tech: ['MQTT', 'InfluxDB', 'Grafana']
  },
  {
    title: 'Smart Logistics',
    desc: 'Optimización de rutas de entrega usando algoritmos genéticos.',
    icon: Globe,
    status: 'Development',
    tech: ['Python', 'Google Maps API', 'React']
  },
  {
    title: 'Crypto Sentiment',
    desc: 'Análisis de sentimiento en redes sociales para predicción de criptomonedas.',
    icon: Code2,
    status: 'Research',
    tech: ['NLP', 'Twitter API', 'TensorFlow']
  },
  {
    title: 'AutoInvoice OCR',
    desc: 'Automatización de facturas usando OCR y extracción de entidades.',
    icon: Cpu,
    status: 'Production',
    tech: ['Tesseract', 'Spacy', 'Django']
  }
]

const statusColors = {
  'Production': 'bg-emerald-100 text-emerald-700 border-emerald-200',
  'Beta': 'bg-blue-100 text-blue-700 border-blue-200',
  'Active': 'bg-green-100 text-green-700 border-green-200',
  'Development': 'bg-amber-100 text-amber-700 border-amber-200',
  'Research': 'bg-purple-100 text-purple-700 border-purple-200'
}

const selectedProject = ref(null)
</script>

<template>
  <section id="projects" class="flex flex-col justify-center py-24 px-6 relative z-10 scroll-mt-24">
    <div class="max-w-7xl mx-auto">
      <h2 class="text-3xl font-bold text-zinc-900 mb-12 flex items-center gap-3">
        <Terminal class="w-8 h-8 text-zinc-900" />
        Proyectos Destacados
      </h2>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          v-for="(project, index) in projects" 
          :key="index"
          @click="selectedProject = project"
          class="group bg-white border border-zinc-200 p-6 hover:border-zinc-400 transition-all duration-300 cursor-pointer hover:shadow-lg relative overflow-hidden rounded-none"
        >
          <div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
            <component :is="project.icon" class="w-24 h-24" />
          </div>

          <div class="relative z-10">
            <div class="flex justify-between items-start mb-4">
              <div class="p-3 bg-zinc-50 border border-zinc-100 inline-block">
                <component :is="project.icon" class="w-6 h-6 text-zinc-700" />
              </div>
              <span 
                :class="statusColors[project.status]"
                class="text-[10px] uppercase tracking-wider px-2 py-1 border font-bold rounded-none"
              >
                {{ project.status }}
              </span>
            </div>

            <h3 class="text-lg font-bold text-zinc-900 mb-2 group-hover:text-zinc-600 transition-colors">
              {{ project.title }}
            </h3>
            <p class="text-zinc-500 text-sm mb-6 line-clamp-2">
              {{ project.desc }}
            </p>

            <div class="flex flex-wrap gap-2 mt-auto">
              <span 
                v-for="tech in project.tech" 
                :key="tech"
                class="text-xs text-zinc-500 bg-zinc-100 px-2 py-1 border border-zinc-200 font-medium rounded-none"
              >
                {{ tech }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Project Detail Modal -->
    <Teleport to="body">
      <Transition name="modal">
        <div 
          v-if="selectedProject" 
          class="fixed inset-0 z-[9999] flex items-center justify-center p-4"
        >
          <!-- Backdrop -->
          <div 
            class="absolute inset-0 bg-zinc-900/60 backdrop-blur-sm"
            @click="selectedProject = null"
          ></div>

          <!-- Content -->
          <div class="relative w-full max-w-2xl bg-white shadow-2xl border border-zinc-200 p-8 z-10">
            <button 
              @click="selectedProject = null"
              class="absolute top-4 right-4 p-2 hover:bg-zinc-100 transition-colors"
            >
              <X class="w-6 h-6 text-zinc-500" />
            </button>

            <div class="flex items-start gap-6 mb-8">
              <div class="p-4 bg-zinc-50 border border-zinc-100 shrink-0">
                <component :is="selectedProject.icon" class="w-12 h-12 text-zinc-900" />
              </div>
              <div>
                <h3 class="text-2xl font-bold text-zinc-900 mb-3">{{ selectedProject.title }}</h3>
                <span 
                  :class="statusColors[selectedProject.status]"
                  class="text-xs px-2 py-1 border font-medium rounded-none"
                >
                  {{ selectedProject.status }}
                </span>
              </div>
            </div>

            <div class="space-y-6 text-zinc-600 leading-relaxed">
              <p class="text-lg font-medium text-zinc-800">{{ selectedProject.desc }}</p>
              <p>
                Esta solución está diseñada para optimizar flujos de trabajo críticos mediante la integración de tecnologías avanzadas. 
                El sistema permite una escalabilidad sin precedentes y reduce la carga operativa manual en un 40%.
              </p>
              <ul class="list-disc list-inside space-y-2 pl-2">
                <li>Integración en tiempo real</li>
                <li>Analítica predictiva avanzada</li>
                <li>Arquitectura modular y segura</li>
              </ul>
              
              <div class="pt-8 flex gap-4 border-t border-zinc-100 mt-8">
                  <button class="bg-zinc-900 text-white px-6 py-3 hover:bg-zinc-800 transition-colors font-medium flex-1 sm:flex-none text-center">
                      Solicitar Demo
                  </button>
                  <button class="border border-zinc-200 text-zinc-900 px-6 py-3 hover:bg-zinc-50 transition-colors font-medium flex-1 sm:flex-none text-center">
                      Ver Documentación
                  </button>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </section>
</template>

<style scoped>
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-active .relative,
.modal-leave-active .relative {
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.modal-enter-from .relative,
.modal-leave-to .relative {
  opacity: 0;
  transform: scale(0.95);
}
</style>
