<script setup>
import { ref, onMounted } from 'vue'
import { GraduationCap, Award, BookOpen, ShieldCheck } from 'lucide-vue-next'

const education = [
  {
    school: 'Universidad Nacional de San Agustin',
    degree: 'Ingeniería de Sistemas',
    location: 'Arequipa, Peru',
    type: 'university',
    logo: 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Escudo_UNSA.png/500px-Escudo_UNSA.png'
  }
]

const certifications = [
  { 
    name: 'Data Analysis with Python', 
    issuer: 'IBM',
    credlyUrl: 'https://www.credly.com/badges/0541ca92-2beb-40c0-9418-d477bbf6a50a/public_url',
    skills: ['NumPy', 'Pandas', 'Python', 'SciPy', 'Scikit-learn']
  },
  { 
    name: 'Data Visualization with Python', 
    issuer: 'IBM',
    credlyUrl: 'https://www.credly.com/badges/d4166aa6-f2c3-4284-ad3e-bf5caed01c83/public_url',
    skills: ['Matplotlib', 'NumPy', 'Python', 'Seaborn', 'Folium']
  },
  { 
    name: 'Machine Learning with Python', 
    issuer: 'IBM',
    credlyUrl: 'https://www.credly.com/badges/dc78aa68-259c-4509-b2f0-a7c6cbdca947/public_url',
    skills: ['Data Science', 'Recommender Systems', 'SciPy', 'Classification', 'Clustering', 'Machine Learning', 'Regression', 'Scikit-learn']
  },
  { 
    name: 'Applied Data Science Specialization (V2)', 
    issuer: 'IBM',
    credlyUrl: 'https://www.credly.com/badges/f502118c-cf93-4377-8d57-fde9f0d5d74e/public_url',
    skills: ['Data Analysis', 'Data Science', 'Matplotlib', 'NumPy', 'Pandas', 'Python', 'SciPy', 'Seaborn', 'Scikit-learn']
  },
  { 
    name: 'IBM Data Science Professional Certificate', 
    issuer: 'IBM',
    credlyUrl: 'https://www.credly.com/badges/f7bf39a8-30a1-46a7-ad2e-99f57d6b664f/public_url',
    skills: ['Data Science', 'Machine Learning', 'Python', 'SQL', 'Data Analysis', 'Data Visualization', 'Big Data']
  },
  { 
    name: 'Applied Data Science Capstone', 
    issuer: 'IBM',
    credlyUrl: 'https://www.credly.com/badges/123812d7-a383-4cde-89e4-96784d2fd7dc/public_url',
    skills: ['Data Collection', 'Data Science', 'Data Visualization', 'Data Wrangling', 'Exploratory Data Analysis']
  },
  { 
    name: 'Google Advanced Data Analytics Certificate', 
    issuer: 'Google Cloud',
    credlyUrl: 'https://www.credly.com/badges/9e347752-3f34-4280-96a8-71bb08baeb8d/public_url',
    skills: ['Data Analysis', 'Data Science', 'Python', 'Statistical Analysis', 'Tableau', 'Machine Learning', 'Predictive Models']
  },    
  { 
    name: 'Google Cloud Computing Foundations Certificate', 
    issuer: 'Google Cloud',
    credlyUrl: 'https://www.credly.com/badges/23d15c41-cb0b-49cc-9300-6d59096da00b/public_url',
    skills: ['BigQuery', 'Cloud Computing', 'Cloud Infrastructure', 'Cloud Storage', 'Compute Engine', 'IAM', 'Network Security']
  },
  { 
    name: 'Certificado de análisis de datos de Google', 
    issuer: 'Google Cloud',
    credlyUrl: 'https://www.credly.com/badges/9b6e594e-124d-4157-82a7-ea66b71260a7/public_url',
    skills: ['Análisis De Datos', 'SQL', 'Visualización de Datos', 'Limpieza de datos', 'R', 'Tableau']
  },
  { 
    name: 'AWS Academy Graduate - Data Center Technician', 
    issuer: 'Amazon Web Services',
    credlyUrl: 'https://www.credly.com/badges/ef8438c2-cec7-4af1-9c05-2af17922cf62/public_url',
    skills: ['Data Center Operations', 'Hardware Fundamentals', 'Networking Fundamentals', 'Operating System Fundamentals']
  },
  { 
    name: 'AWS Academy Graduate - Introduction to Cloud ', 
    issuer: 'Amazon Web Services',
    credlyUrl: 'https://www.credly.com/badges/57e580f1-6417-462a-8235-0c2c0ec7d0b3/public_url',
    skills: ['AWS Architecture', 'AWS Cloud', 'AWS Core', 'AWS Foundations', 'AWS Pricing', 'AWS Support']
  },
  { 
    name: 'AWS Academy Graduate - Engineering Operations Technicians', 
    issuer: 'Amazon Web Services',
    credlyUrl: 'https://www.credly.com/badges/4a4bcbdc-8003-40d6-8205-7a81cc8f2827/public_url',
    skills: ['Data Centers', 'Data Center Efficiency', 'Physical Infrastructure', 'Cooling', 'Electrical Fundamentals']
  },
  { 
    name: 'AWS Educate Introduction to Generative AI', 
    issuer: 'Amazon Web Services',
    credlyUrl: 'https://www.credly.com/badges/da85d94c-d92a-49d0-9a02-716aa3ab0d0c/public_url',
    skills: ['AWS', 'AI', 'Generative AI', 'Machine Learning', 'AWS Cloud']
  },
  { 
    name: 'AWS Educate Machine Learning Foundations', 
    issuer: 'Amazon Web Services',
    credlyUrl: 'https://www.credly.com/badges/64942342-52f7-47b7-b698-1c94da429595/public_url',
    skills: ['AWS', 'AWS Cloud', 'Machine Learning', 'Artificial Intelligence']
  },
  { 
    name: 'Data Science Orientation', 
    issuer: 'Coursera',
    credlyUrl: 'https://www.credly.com/badges/a602949f-982d-40aa-863b-63e1c1b24f51/public_url',
    skills: ['Data Science', 'AI', 'Artificial Intelligence', 'Machine Learning']
  },
  { 
    name: 'Tools for Data Science', 
    issuer: 'Coursera',
    credlyUrl: 'https://www.credly.com/badges/c8bdbc89-96f9-47e4-a6a8-166ed153a581/public_url',
    skills: ['Jupyter Notebook', 'Data Science Tools', 'GitHub', 'RStudio', 'Watson Studio']
  },
  { 
    name: 'Data Science Methodology', 
    issuer: 'Coursera',
    credlyUrl: 'https://www.credly.com/badges/bba7d2b5-b464-4a1c-9141-f75afd897a89/public_url',
    skills: ['Data Science Methodology', 'Jupyter Notebook', 'Problem Solving']
  },
  { 
    name: 'Python for Data Science and AI', 
    issuer: 'Coursera',
    credlyUrl: 'https://www.credly.com/badges/242c4803-2e0b-4874-bb88-1af68caf1696/public_url',
    skills: ['Python', 'Data Science', 'AI', 'Pandas', 'Numpy']
  },  
  { 
    name: 'Python Project for Data Science', 
    issuer: 'Coursera',
    credlyUrl: 'https://www.credly.com/badges/37834214-2d0e-426e-bc13-1a82540e2d86/public_url',
    skills: ['Data Science', 'Python', 'Artificial Intelligence', 'Project Management']
  },
  { 
    name: 'Databases and SQL for Data Science', 
    issuer: 'IBM',
    credlyUrl: 'https://www.credly.com/badges/64ceeb50-e74a-4665-88d3-ac80dd889ca1/public_url',
    skills: ['Data Science', 'SQL', 'Relational Databases', 'Python', 'Jupyter Notebook']
  },
  { 
    name: 'Software Engineering Essentials', 
    issuer: 'Coursera',
    credlyUrl: 'https://www.credly.com/badges/2a0040b3-21d9-4c64-8ef2-db204964af68/public_url',
    skills: ['Software Engineering', 'SDLC', 'Software Architecture', 'Agile']
  },
  { 
    name: 'Business Intelligence Foundation Professional Certification - BIFPC™', 
    issuer: 'Certiprof',
    credlyUrl: 'https://www.credly.com/badges/81089083-80a9-4568-a5a3-4936cc33a545/public_url',
    skills: ['Business Intelligence', 'Data Analysis', 'Data Mining']
  },
  { 
    name: 'Scrum Foundation Professional Certification - SFPC™', 
    issuer: 'Certiprof',
    credlyUrl: 'https://www.credly.com/badges/9bed095f-20ed-4f81-a69d-d9ab6b043192/public_url',
    skills: ['Scrum', 'Agile', 'Project Management', 'Scrum Master']
  },
]

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
                    v-if="cert.issuer.includes('Google Cloud')" 
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
