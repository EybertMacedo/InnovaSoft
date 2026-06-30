<script setup>
import { ref, onMounted } from 'vue'
import { GraduationCap, Award, BookOpen, ShieldCheck, ExternalLink } from 'lucide-vue-next'
import educationData from '../data/education.json'

const { education, certifications } = educationData

const isVisible = ref(false)

onMounted(() => {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          isVisible.value = true
        }
      })
    },
    { threshold: 0.1 }
  )

  const section = document.querySelector('#education')
  if (section) observer.observe(section)
})
</script>

<template>
  <section id="education" class="py-24 px-6 relative z-10 scroll-mt-16">
    <div class="max-w-7xl mx-auto">
      <h2 class="text-3xl font-bold text-zinc-900 mb-12 flex items-center gap-3 animate-fade-in">
        <GraduationCap class="w-8 h-8 text-zinc-900" />
        Educación y Certificaciones
      </h2>

      <div class="flex flex-col gap-12">
        <!-- Academic -->
        <div class="space-y-6">
          <h3 
            class="text-xl font-semibold text-zinc-800 flex items-center gap-2 mb-6 opacity-0 -translate-x-4 transition-all duration-400"
            :class="{ 'opacity-100 translate-x-0': isVisible }"
            style="transition-delay: 100ms"
          >
            <BookOpen class="w-5 h-5" /> Formación Académica
          </h3>
          
          <div 
            v-for="(edu, index) in education" 
            :key="index"
            class="bg-white p-6 border border-zinc-200 shadow-sm hover:shadow-md transition-all duration-400 rounded-none max-w-2xl opacity-0 translate-y-4"
            :class="{ 'opacity-100 translate-y-0': isVisible }"
            style="transition-delay: 200ms"
          >
            <div class="flex items-center gap-3 mb-2">
              <img :src="edu.logo" alt="University Logo" class="w-8 h-8 object-contain" />
              <h4 class="font-bold text-lg text-zinc-900">{{ edu.school }}</h4>
            </div>
            <p class="text-zinc-600 font-medium">{{ edu.degree }}</p>
            <p class="text-zinc-500 text-sm mt-2">{{ edu.location }}</p>
          </div>
        </div>

        <!-- Certifications -->
        <div class="space-y-6">
          <h3 
            class="text-xl font-semibold text-zinc-800 flex items-center gap-2 mb-6 opacity-0 -translate-x-4 transition-all duration-400"
            :class="{ 'opacity-100 translate-x-0': isVisible }"
            style="transition-delay: 300ms"
          >
            <Award class="w-5 h-5" /> Certificaciones & Lifelong Learning
          </h3>
          
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            <div 
              v-for="(cert, index) in certifications" 
              :key="index"
              class="bg-white p-3 border border-zinc-200 flex flex-col gap-2 hover:border-zinc-400 transition-all duration-500 rounded-none opacity-0 scale-95 relative group overflow-hidden min-h-[110px]"
              :class="{ 'opacity-100 scale-100': isVisible }"
              :style="{ transitionDelay: `${400 + index * 50}ms` }"
            >
              <div class="flex items-start gap-4">
                <div class="mt-1 shrink-0">
                  <img 
                    v-if="cert.issuer.includes('DataCamp')" 
                    src="https://catalogartifact.azureedge.net/publicartifacts/86079200.72c546bd-88c2-4f61-9758-1991903dfb6c-12c43ca8-6c10-45a6-9d37-da6504dc0af4/image0_DataCamp.png" 
                    alt="DataCamp" 
                    class="w-5 h-5 object-contain"
                  />
                  <img 
                    v-else-if="cert.issuer.includes('Google Cloud')" 
                    src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" 
                    alt="Google Cloud" 
                    class="w-5 h-5"
                  />
                  <img 
                    v-else-if="cert.issuer.includes('Google')" 
                    src="https://upload.wikimedia.org/wikipedia/commons/5/53/Google_%22G%22_Logo.svg" 
                    alt="Google" 
                    class="w-5 h-5"
                  />
                  <img 
                    v-else-if="cert.issuer.includes('IBM')" 
                    src="https://upload.wikimedia.org/wikipedia/commons/5/51/IBM_logo.svg" 
                    alt="IBM" 
                    class="w-6 h-3 mt-1"
                  />
                  <img 
                    v-else-if="cert.issuer.includes('Amazon')" 
                    src="https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg" 
                    alt="AWS" 
                    class="w-6 h-4 mt-0.5"
                  />
                  <ShieldCheck 
                    v-else-if="cert.issuer.includes('Certiprof')" 
                    class="w-6 h-6 -mt-1 text-blue-600" 
                  />
                  <img 
                    v-else-if="cert.issuer.includes('Coursera')" 
                    src="https://upload.wikimedia.org/wikipedia/commons/9/97/Coursera-Logo_600x600.svg" 
                    alt="Coursera" 
                    class="w-5 h-5"
                  />
                  <Award v-else class="w-5 h-5 text-zinc-400" />
                </div>
                <div>
                  <h4 class="font-medium text-zinc-900 text-sm leading-tight">{{ cert.name }}</h4>
                  <p class="text-zinc-500 text-xs mt-1">{{ cert.issuer }}</p>
                </div>
              </div>

              <!-- Hover Overlay for Skills & Link -->
              <div 
                v-if="cert.skills || cert.credlyUrl"
                class="absolute inset-0 bg-zinc-50/95 backdrop-blur-sm p-3 opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-10 flex flex-col"
              >
                <!-- Skills Section -->
                <div v-if="cert.skills" class="flex-1 overflow-y-auto no-scrollbar">
                  <div class="flex flex-wrap gap-1 content-start">
                    <span 
                      v-for="skill in cert.skills" 
                      :key="skill"
                      class="text-[12px] bg-white text-zinc-600 px-1.5 py-0.5 rounded-md border border-zinc-200 shadow-sm leading-none"
                    >
                      {{ skill }}
                    </span>
                  </div>
                </div>

                <!-- Credly Link -->
                <div v-if="cert.credlyUrl" class="flex justify-end mt-2 pt-2 border-t border-zinc-200/50 shrink-0">
                  <a 
                    :href="cert.credlyUrl"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="flex items-center gap-1 text-[10px] text-zinc-600 hover:text-blue-600 transition-colors font-medium group/link"
                  >
                    Ver Credencial 
                    <ExternalLink class="w-2.5 h-2.5 group-hover/link:translate-x-0.5 transition-transform" />
                  </a>
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
  animation: fade-in 0.8s ease-out;
}
</style>
