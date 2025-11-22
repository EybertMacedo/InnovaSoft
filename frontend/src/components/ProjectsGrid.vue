<script setup>
import { 
  MessageSquare, 
  Eye, 
  BrainCircuit, 
  ShieldCheck, 
  BarChart3, 
  Cpu, 
  Code2,
  Terminal,
  X
} from 'lucide-vue-next'
import { ref } from 'vue'

const projects = [
  { id: 1, title: 'Auto-WhatsApp Business', desc: 'Bots con Twilio/Node', status: 'Prod', icon: MessageSquare },
  { id: 2, title: 'Industrial Safety Vision', desc: 'Detección EPPs/Cobbles con YOLOv8', status: 'Prod', icon: Eye },
  { id: 3, title: 'Behavior AI', desc: 'Detección de anomalías/seguridad', status: 'Dev', icon: BrainCircuit },
  { id: 4, title: 'Gov-Tech Assistant', desc: 'Clasificación documental con LLMs', status: 'Beta', icon: ShieldCheck },
  { id: 5, title: 'Predictive Core', desc: 'Dashboard de inventarios', status: 'Prod', icon: BarChart3 },
  { id: 6, title: 'Unity Industrial Sim', desc: 'Visualización 3D WebGL', status: 'Demo', icon: Cpu },
  { id: 7, title: 'Smart OCR', desc: 'Extracción de data estructurada', status: 'Dev', icon: Code2 },
]

const statusColors = {
  Prod: 'text-emerald-700 bg-emerald-100/50 border-emerald-200',
  Dev: 'text-blue-700 bg-blue-100/50 border-blue-200',
  Beta: 'text-amber-700 bg-amber-100/50 border-amber-200',
  Demo: 'text-purple-700 bg-purple-100/50 border-purple-200'
}

const selectedProject = ref(null)
</script>

<template>
  <section id="projects" class="flex flex-col justify-center py-12 px-6 relative z-10">
    <div class="max-w-7xl mx-auto">
      <h2 class="text-3xl font-bold text-zinc-900 mb-12 flex items-center gap-3">
        <Terminal class="w-8 h-8 text-zinc-900" />
        Proyectos Destacados
      </h2>
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          v-for="project in projects" 
          :key="project.id"
          @click="selectedProject = project"
          class="group relative bg-white/40 backdrop-blur-md border border-white/50 p-6 hover:bg-white/60 transition-all duration-500 hover:shadow-xl hover:border-zinc-400/50 rounded-none cursor-pointer"
        >
          <div class="absolute top-4 right-4">
            <span 
              :class="statusColors[project.status] || 'text-zinc-600 bg-zinc-100/50 border-zinc-200'"
              class="text-xs px-2 py-1 border font-medium rounded-none backdrop-blur-sm"
            >
              {{ project.status }}
            </span>
          </div>
          
          <component :is="project.icon" class="w-10 h-10 text-zinc-400 group-hover:text-zinc-900 transition-colors mb-4" />
          
          <h3 class="text-xl font-bold text-zinc-900 mb-2">
            {{ project.title }}
          </h3>
          <p class="text-zinc-500 text-sm leading-relaxed">
            {{ project.desc }}
          </p>
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
