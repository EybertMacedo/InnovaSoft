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
  X,
  Database
} from 'lucide-vue-next'
import { ref } from 'vue'

const projects = [
  { 
    id: 1, 
    title: 'SafetyMind Cobbles', 
    desc: 'Detección temprana de eventos de cobble en laminación de acero.', 
    status: 'Demo', 
    icon: Eye,
    url: 'https://github.com/EybertMacedo/cobbles',
    htmlContent: `
      <p class="mb-2">
        <span class="bg-zinc-100 text-zinc-800 text-xs font-medium px-2.5 py-0.5 rounded border border-zinc-200">Código Privado (Demo Repo)</span>
      </p>
      <p>
        Sistema desarrollado para detectar de forma temprana eventos de cobble en barras de acero al rojo vivo durante el proceso de laminación. Utiliza visión por computadora y modelos entrenados con YOLOv8 para identificar deformaciones, atascamientos y comportamientos anómalos en condiciones de alta temperatura y ruido industrial.
      </p>
      <ul class="list-disc list-inside space-y-2 pl-2">
        <li>Procesamiento de video en tiempo real</li>
        <li>Modelo personalizado basado en YOLOv8</li>
        <li>Lógica avanzada de validación y umbrales de confianza</li>
        <li>Generación de videos anotados y métricas por frame</li>
      </ul>
    `
  },
  { 
    id: 2, 
    title: 'SentiData System', 
    desc: 'Plataforma de análisis de sentimiento y percepción ciudadana.', 
    status: 'Prod', 
    icon: BarChart3,
    url: 'https://sentidata-dashboard.vercel.app/',
    htmlContent: `
      <p>
        Plataforma desarrollada para recopilar, procesar y analizar grandes volúmenes de datos textuales provenientes de redes sociales, encuestas y canales digitales. El sistema utiliza técnicas de procesamiento de lenguaje natural (NLP) y modelos de machine learning para identificar patrones de opinión, clasificar sentimiento (positivo, negativo o neutral) y detectar tendencias emergentes.
      </p>
      <ul class="list-disc list-inside space-y-2 pl-2">
        <li>Integración en tiempo real</li>
        <li>Automatización de procesos</li>
        <li>Procesamiento de lenguaje natural con LLMs</li>
        <li>Arquitectura modular y segura</li>
      </ul>
    `
  },
  { 
    id: 3, 
    title: 'Poker Hand Classifier', 
    desc: 'Modelo CNN personalizado para clasificación de manos de póker.', 
    status: 'Research', 
    icon: BrainCircuit,
    url: 'https://revistas.ulasalle.edu.pe/innosoft/article/view/157/206',
    htmlContent: `
      <p>
        Artículo publicado en la Revista Innovación y Software (Vol. 5 Nº 1, 2024), con contribuciones orientadas al desarrollo metodológico, análisis, validación y elaboración del manuscrito. El trabajo integra investigación aplicada, diseño experimental y desarrollo de software para la resolución de un problema computacional complejo.
      </p>
      <ul class="list-disc list-inside space-y-2 pl-2">
        <li>Conceptualización y planteamiento del estudio</li>
        <li>Análisis formal y desarrollo metodológico</li>
        <li>Implementación de software y validación de resultados</li>
        <li>Curación de datos y visualización de información</li>
        <li>Redacción, revisión y edición del manuscrito</li>
      </ul>
    `
  },
  { 
    id: 4, 
    title: 'SafetyModel', 
    desc: 'Detección de Colisiones en Zonas de Riesgo con YOLO.', 
    status: 'Prod', 
    icon: ShieldCheck,
    url: 'https://github.com/EybertMacedo/SafetyModel/tree/main',
    htmlContent: `
      <p>
        Sistema diseñado para detectar en tiempo real el ingreso de personas a zonas de riesgo y la interacción no autorizada con maquinaria en entornos industriales. Utiliza un modelo personalizado entrenado con el algoritmo YOLO para identificar comportamientos inseguros y generar alertas inmediatas.
      </p>
      <ul class="list-disc list-inside space-y-2 pl-2">
        <li>Detección de personas y zonas peligrosas en tiempo real</li>
        <li>Modelo YOLO entrenado con datos personalizados</li>
        <li>Alertas visuales ante violaciones de seguridad</li>
        <li>Mejora de la prevención y supervisión industrial</li>
      </ul>
    `
  },
  { 
    id: 5, 
    title: 'InnovaSoft Landing', 
    desc: 'Portafolio interactivo con simulaciones de IA.', 
    status: 'Prod', 
    icon: Code2,
    url: 'https://github.com/EybertMacedo/InnovaSoft/',
    htmlContent: `
      <p>
        Plataforma web moderna diseñada para exhibir soluciones de Inteligencia Artificial y Ciencia de Datos. Incorpora simulaciones interactivas de visión por computadora y asistentes conversacionales, demostrando capacidades técnicas avanzadas en un entorno visualmente atractivo y responsivo.
      </p>
      <ul class="list-disc list-inside space-y-2 pl-2">
        <li>Arquitectura Single Page Application (SPA) con Vue 3</li>
        <li>Diseño Glassmorphism con Tailwind CSS</li>
        <li>Simulaciones interactivas de IA en el navegador</li>
        <li>Optimización de rendimiento y SEO</li>
      </ul>
    `
  },
  { 
    id: 6, 
    title: 'Bank Marketing in R', 
    desc: 'Análisis predictivo para campañas de marketing bancario.', 
    status: 'Dev', 
    icon: Database,
    url: 'https://github.com/EybertMacedo/bank_marketing_R',
    htmlContent: `
      <p>
        Proyecto orientado al análisis del Bank Marketing Dataset para identificar los factores que influyen en la suscripción de depósitos a plazo. A través de técnicas de análisis exploratorio y modelos de machine learning, se evalúan patrones de comportamiento del cliente con el fin de optimizar estrategias de marketing en futuras campañas bancarias.
      </p>
      <ul class="list-disc list-inside space-y-2 pl-2">
        <li>Análisis exploratorio y segmentación de clientes</li>
        <li>Procesamiento y limpieza de datos con R</li>
        <li>Modelado predictivo con múltiples algoritmos de clasificación</li>
        <li>Identificación de variables clave para la conversión</li>
      </ul>
    `
  },
  { 
    id: 7, 
    title: 'Tasty Bytes Predictor', 
    desc: 'Modelo predictivo de tráfico para recetas de cocina.', 
    status: 'Data Science', 
    icon: BarChart3,
    url: 'https://www.datacamp.com/datalab/w/01330a4f-a78f-42d4-bf32-b902e3da72c9',
    htmlContent: `
      <p>
        Proyecto desarrollado como parte del examen profesional “Data Scientist – Recipe Site Traffic”, enfocado en construir un modelo predictivo capaz de identificar qué recetas generan alto tráfico cuando son destacadas en la página principal. El estudio abarca análisis exploratorio, validación de datos, ingeniería de características y evaluación comparativa de modelos.
      </p>
      <ul class="list-disc list-inside space-y-2 pl-2">
        <li>Análisis exploratorio y visualización de patrones nutricionales</li>
        <li>Limpieza, validación y estandarización del dataset</li>
        <li>Desarrollo y comparación de modelos (Logistic Regression y LinearSVC)</li>
        <li>Optimización mediante selección de umbral y análisis de curvas ROC</li>
        <li>Evaluación con métricas de negocio orientadas a impacto y revenue</li>
      </ul>
    `
  },
  { 
    id: 8, 
    title: 'TikTok Classification', 
    desc: 'Clasificación automática de videos para moderación.', 
    status: 'ML', 
    icon: MessageSquare,
    url: 'https://github.com/EybertMacedo/Google-Data-Science',
    htmlContent: `
      <p>
        Proyecto enfocado en la clasificación automática de videos de TikTok para distinguir entre contenido que contiene afirmaciones (claims) y contenido basado en opiniones con el fin de priorizar la moderación y reducir la propagación de desinformación. Incluye análisis exploratorio, ingeniería de características y evaluación de modelos.
      </p>
      <ul class="list-disc list-inside space-y-2 pl-2">
        <li>Análisis ético y priorización del recall para moderación efectiva</li>
        <li>Ingeniería de características aplicadas a texto y métricas de interacción</li>
        <li>Entrenamiento y comparación de modelos (Random Forest, XGBoost)</li>
        <li>Evaluación basada en métricas orientadas al impacto en moderación</li>
      </ul>
    `
  },
  { 
    id: 9, 
    title: 'IBM Data Science Tools', 
    desc: 'Notebook demostrativo del ecosistema de Data Science.', 
    status: 'Edu', 
    icon: Terminal,
    url: 'https://github.com/EybertMacedo/IBM-Data-Science',
    htmlContent: `
      <p>
        Notebook final desarrollado para el curso "Tools for Data Science" de IBM, donde se aplican conceptos fundamentales del ecosistema de ciencia de datos. El proyecto incluye el uso de lenguajes comunes en data science, librerías esenciales, herramientas de software, ejemplos de expresiones aritméticas y funciones básicas en Python.
      </p>
      <ul class="list-disc list-inside space-y-2 pl-2">
        <li>Lenguajes, librerías y herramientas fundamentales en ciencia de datos</li>
        <li>Demostración de operaciones aritméticas y funciones simples en Python</li>
        <li>Uso de Jupyter Notebooks para documentar, ejecutar y organizar código</li>
        <li>Aplicación práctica de Markdown y estructuración de notebooks</li>
      </ul>
    `
  }
]

const statusColors = {
  Prod: 'text-emerald-700 bg-emerald-100/50 border-emerald-200',
  Dev: 'text-blue-700 bg-blue-100/50 border-blue-200',
  Beta: 'text-amber-700 bg-amber-100/50 border-amber-200',
  Demo: 'text-purple-700 bg-purple-100/50 border-purple-200'
}

const selectedProject = ref(null)
defineEmits(['open-contact'])
</script>

<template>
  <section id="projects" class="flex flex-col justify-center py-24 px-6 relative z-10 scroll-mt-16">
    <div class="max-w-7xl mx-auto">
      <h2 class="text-3xl font-bold text-zinc-900 mb-12 flex items-center gap-3 animate-fade-in">
        <Terminal class="w-8 h-8 text-zinc-900" />
        Proyectos Destacados
      </h2>
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          v-for="project in projects" 
          :key="project.id"
          :data-project-id="project.id"
          @click="selectedProject = project"
          class="project-card group relative bg-white/40 backdrop-blur-md border border-white/50 p-6 hover:bg-white/60 transition-all duration-500 hover:shadow-xl hover:border-zinc-400/50 rounded-none cursor-pointer hover:scale-100 hover:-translate-y-2"
        >
          <div class="absolute top-4 right-4">
            <span 
              :class="statusColors[project.status] || 'text-zinc-600 bg-zinc-100/50 border-zinc-200'"
              class="text-xs px-2 py-1 border font-medium rounded-none backdrop-blur-sm"
            >
              {{ project.status }}
            </span>
          </div>
          
          <component :is="project.icon" class="w-10 h-10 text-zinc-400 group-hover:text-zinc-900 transition-all duration-500 group-hover:scale-110 mb-4" />
          
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
              <div v-html="selectedProject.htmlContent" class="space-y-4"></div>
              
              <div class="pt-8 flex gap-4 border-t border-zinc-100 mt-8">
                  <button 
                      @click="$emit('open-contact'); selectedProject = null"
                      class="bg-zinc-900 text-white px-6 py-3 hover:bg-zinc-800 transition-colors font-medium flex-1 sm:flex-none text-center"
                  >
                      Solicitar Demo
                  </button>
                  <a 
                      :href="selectedProject.url"
                      target="_blank"
                      rel="noopener noreferrer"
                      class="border border-zinc-200 text-zinc-900 px-6 py-3 hover:bg-zinc-50 transition-colors font-medium flex-1 sm:flex-none text-center"
                  >
                      {{ selectedProject.buttonText || 'Ver Documentación' }}
                  </a>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </section>
</template>

<style scoped>
@keyframes fade-in {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fade-in 1.2s ease-out;
}

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
