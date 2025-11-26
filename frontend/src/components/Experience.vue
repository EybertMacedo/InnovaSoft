<script setup>
import { ref, onMounted } from 'vue'
import { Briefcase, Calendar, MapPin } from 'lucide-vue-next'

const experiences = [
  {
    role: 'AI Integration Assistant',
    company: 'Peru Ministry of Housing',
    location: 'Lima, Peru',
    period: 'Abril 2025 - Actual',
    description: 'Diseño e implementación de flujos de trabajo basados en IA para monitorear la percepción pública de proyectos nacionales.',
    achievements: [
      'Diseñé flujos de trabajo con PLN, análisis de sentimientos y ML para monitoreo de percepción pública.',
      'Desarrollé canales de datos escalables y paneles en tiempo real para procesar miles de menciones.',
      'Implementé infraestructura segura en la nube compatible con estándares gubernamentales.'
    ],
    tech: ['Python', 'FastAPI', 'Pandas', 'Docker', 'Supabase', 'LangChain', 'OpenAI', 'Gemini']
  },
  {
    role: 'AI/ML Engineer',
    company: 'SafetyMind S.A.C.',
    location: 'Remote',
    period: 'Setiembre 2024 – Marzo 2025',
    description: 'Desarrollo de sistemas de seguridad industrial basados en visión artificial.',
    achievements: [
      'Diseñé sistemas de seguridad con visión artificial para detectar riesgos en entornos industriales.',
      'Optimicé modelos de detección (YOLOv8) para rendimiento en tiempo real.',
      'Desarrollé canales de datos automatizados para identificar patrones de riesgo.'
    ],
    tech: ['YOLOv8', 'PyTorch', 'TensorFlow', 'OpenCV', 'Qdrant', 'Docker', 'MLOps']
  },
  {
    role: 'Investigador Principal',
    company: 'UNSA - Investigación sobre Inteligencia Artificial',
    location: 'Arequipa, Perú',
    period: 'Enero 2024 – Julio 2024',
    description: 'Liderazgo de proyecto de investigación para clasificación de manos de póker con IA.',
    achievements: [
      'Lideré un equipo para desarrollar un modelo de IA para clasificación de manos de póker.',
      'Abordé desequilibrio de clases severo y optimicé ingeniería de características.',
      'Dirigí diseño, entrenamiento y estrategias de optimización logrando mejoras significativas en precisión.'
    ],
    tech: ['Python', 'TensorFlow', 'Scikit-learn', 'Pandas', 'NumPy', 'OpenCV', 'Git']
  },
  {
    role: 'Data Engineer / Python Developer',
    company: 'FreeLancer',
    location: 'Remote',
    period: '2024',
    description: 'Automatización del procesamiento de facturas de profesores a partir de archivos .lis.',
    achievements: [
      'Construí un sistema en Python para leer, limpiar y transformar archivos .lis en estructuras tabulares analizables.',
      'Implementé extracción automática de códigos, nombres y montos mediante parsing línea por línea.',
      'Diseñé un pipeline de validación y normalización de datos para integrarlos en un DataFrame final.',
      'Aceleré el flujo de trabajo administrativo reduciendo el tiempo manual de procesamiento.'
    ],
    tech: ['Python', 'Pandas', 'Regex', 'Data Cleaning', 'ETL']
  },
  {
    role: 'Web Developer (Odoo)',
    company: 'Tecnovedades E.I.R.L. — Freelance',
    location: 'Remote',
    period: '2023',
    description: 'Desarrollo de un aplicativo médico sobre la plataforma Odoo.',
    achievements: [
      'Implementé módulos personalizados en Odoo para gestionar historias clínicas, agenda médica y control de pacientes.',
      'Desarrollé vistas, modelos y controladores usando el framework MVC de Odoo.',
      'Integré flujos automatizados para registro de consultas, emisión de reportes y administración de usuarios.',
      'Optimicé el rendimiento del backend y personalicé la UI mediante XML, JavaScript y QWeb.'
    ],
    tech: ['Odoo', 'Python', 'PostgreSQL', 'XML/QWeb', 'JavaScript', 'Odoo ORM']
  }
]

const visibleItems = ref(new Set())

onMounted(() => {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const index = entry.target.dataset.index
          visibleItems.value.add(parseInt(index))
        }
      })
    },
    { threshold: 0.2 }
  )

  document.querySelectorAll('.experience-card').forEach((el) => {
    observer.observe(el)
  })
})
</script>

<template>
  <section id="experience" class="py-24 px-6 relative z-10 bg-white/30 backdrop-blur-lg border-y border-white/20 scroll-mt-16">
    <div class="max-w-4xl mx-auto">
      <h2 class="text-3xl font-bold text-zinc-900 mb-12 flex items-center gap-3 animate-fade-in">
        <Briefcase class="w-8 h-8 text-zinc-900" />
        Experiencia Profesional
      </h2>

      <div class="space-y-12 relative before:absolute before:inset-0 before:ml-5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-zinc-300 before:to-transparent">
        <div 
          v-for="(exp, index) in experiences" 
          :key="index"
          :data-index="index"
          class="experience-card relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group opacity-0 translate-y-8 transition-all duration-500"
          :class="{ 'opacity-100 translate-y-0': visibleItems.has(index) }"
          :style="{ transitionDelay: `${index * 200}ms` }"
        >
          <!-- Timeline Dot -->
          <div class="flex items-center justify-center w-10 h-10 rounded-full border border-white bg-zinc-100 shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10 transition-all duration-500 group-hover:scale-110 group-hover:bg-zinc-900 group-hover:shadow-lg">
            <Briefcase class="w-5 h-5 text-zinc-600 transition-colors duration-300 group-hover:text-white" />
          </div>

          <!-- Content Card -->
          <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] bg-white p-6 border border-zinc-200 shadow-sm hover:shadow-xl transition-all duration-400 rounded-none hover:-translate-y-1 hover:border-zinc-400">
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-4 gap-2">
              <div>
                <h3 class="font-bold text-lg text-zinc-900 group-hover:text-zinc-700 transition-colors">{{ exp.role }}</h3>
                <span class="text-zinc-600 font-medium">{{ exp.company }}</span>
              </div>
              <div class="flex flex-col items-start sm:items-end text-xs text-zinc-500 gap-1">
                <span class="flex items-center gap-1 bg-zinc-100 px-2 py-1 rounded-none group-hover:bg-zinc-900 group-hover:text-white transition-all duration-500">
                  <Calendar class="w-3 h-3" /> {{ exp.period }}
                </span>
                <span class="flex items-center gap-1">
                  <MapPin class="w-3 h-3" /> {{ exp.location }}
                </span>
              </div>
            </div>
            
            <p class="text-zinc-700 text-sm mb-4">{{ exp.description }}</p>

            <ul class="space-y-2 mb-4">
              <li 
                v-for="(achievement, i) in exp.achievements" 
                :key="i"
                class="text-sm text-zinc-600 flex items-start gap-2 opacity-0 translate-x-4 transition-all duration-400"
                :class="{ 'opacity-100 translate-x-0': visibleItems.has(index) }"
                :style="{ transitionDelay: `${index * 200 + (i + 1) * 150}ms` }"
              >
                <span class="text-zinc-400 mt-1">▸</span>
                <span>{{ achievement }}</span>
              </li>
            </ul>

            <div class="flex flex-wrap gap-2">
              <span 
                v-for="(tech, i) in exp.tech" 
                :key="tech"
                class="text-xs bg-zinc-100 text-zinc-700 px-2 py-1 rounded-none border border-zinc-200 hover:bg-zinc-900 hover:text-white hover:border-zinc-900 transition-all duration-500 opacity-0 scale-95"
                :class="{ 'opacity-100 scale-100': visibleItems.has(index) }"
                :style="{ transitionDelay: `${index * 200 + (exp.achievements.length + i + 1) * 100}ms` }"
              >
                {{ tech }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
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
</style>
