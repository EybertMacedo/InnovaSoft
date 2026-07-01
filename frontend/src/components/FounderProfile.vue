<script setup>
import { Linkedin, Github, Mail, X, Send } from 'lucide-vue-next'
import { ref } from 'vue'

const showContactModal = ref(false)
const contactForm = ref({
  name: '',
  email: '',
  message: ''
})

const isSubmitting = ref(false)

const handleContact = async () => {
  isSubmitting.value = true
  try {
    const apiUrl = import.meta.env.VITE_API_URL || '';
    const response = await fetch(`${apiUrl}/api/contact`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(contactForm.value),
    })

    if (response.ok) {
      alert('Mensaje enviado correctamente!')
      showContactModal.value = false
      contactForm.value = { name: '', email: '', message: '' }
    } else {
      const contentType = response.headers.get("content-type");
      if (contentType && contentType.indexOf("application/json") !== -1) {
        const errorData = await response.json();
        alert(`Error: ${errorData.detail || 'Hubo un error al enviar el mensaje.'}`);
      } else {
        const errorText = await response.text();
        console.error('Non-JSON Error Response:', errorText);
        alert(`Error del servidor: ${errorText.substring(0, 150)}...`);
      }
    }
  } catch (error) {
    console.error('Error:', error)
    alert('Error de conexión con el servidor.')
  } finally {
    isSubmitting.value = false
  }
}
const openContactModal = () => {
  showContactModal.value = true
}

defineExpose({ openContactModal })

const githubUrl = import.meta.env.VITE_GITHUB_URL || 'https://github.com/EybertMacedo'
const linkedinUrl = import.meta.env.VITE_LINKEDIN_URL || 'https://www.linkedin.com/in/emacedop/'
</script>

<template>
  <section id="contact" class="py-24 px-6 bg-zinc-900 relative overflow-hidden">
    <!-- Background Grid -->
    <div class="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px]"></div>
    
    <div class="max-w-4xl mx-auto bg-zinc-800/50 backdrop-blur-xl border border-zinc-700 p-8 md:p-12 flex flex-col items-center gap-10 rounded-xl shadow-2xl hover:shadow-blue-500/10 transition-all duration-500 text-center relative z-10">
      
      <div class="flex-1">
        <h2 class="text-3xl font-bold text-white mb-2">Hablemos</h2>
        <p class="text-zinc-400 font-medium mb-4">¿Tienes un proyecto en mente?</p>
        <p class="text-zinc-300 leading-relaxed mb-6 max-w-2xl mx-auto">
          Estoy disponible para colaborar en proyectos desafiantes de IA, Machine Learning y Desarrollo de Software.
        </p>
        
        <div class="mt-8 flex gap-4 justify-center">
          <a :href="githubUrl" target="_blank" rel="noopener noreferrer" class="text-zinc-500 hover:text-blue-400 transition-colors duration-300"><Github class="w-6 h-6" /></a>
          <a href="https://orcid.org/0000-0001-5802-4054" target="_blank" rel="noopener noreferrer" class="text-zinc-500 hover:text-[#A6CE39] transition-colors duration-300">
            <svg viewBox="0 0 24 24" class="w-6 h-6" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 0C5.372 0 0 5.372 0 12s5.372 12 12 12 12-5.372 12-12S18.628 0 12 0zM7.369 4.378c.525 0 .947.431.947.947s-.422.947-.947.947a.95.95 0 0 1-.947-.947c0-.525.422-.947.947-.947zm-.722 3.038h1.444v10.041H6.647V7.416zm3.562 0h3.9c3.712 0 5.344 2.653 5.344 5.025 0 2.578-2.016 5.025-5.325 5.025h-3.919V7.416zm1.444 1.303v7.444h2.297c3.272 0 4.022-2.484 4.022-3.722 0-2.016-1.284-3.722-4.097-3.722h-2.222z" fill="currentColor"/>
            </svg>
          </a>
          <a :href="linkedinUrl" target="_blank" rel="noopener noreferrer" class="text-zinc-500 hover:text-blue-400 transition-colors duration-300"><Linkedin class="w-6 h-6" /></a>
          <button @click="showContactModal = true" class="text-zinc-500 hover:text-blue-400 transition-colors duration-300"><Mail class="w-6 h-6" /></button>
        </div>
      </div>
    </div>

    <!-- Contact Modal -->
    <Transition name="modal">
      <div 
        v-if="showContactModal" 
        class="fixed inset-0 z-50 flex items-center justify-center p-4"
      >
        <div 
          class="absolute inset-0 bg-zinc-900/60 backdrop-blur-sm"
          @click="showContactModal = false"
        ></div>

        <div class="relative w-full max-w-md bg-white shadow-2xl border border-zinc-200 p-8 z-10">
          <button 
            @click="showContactModal = false"
            class="absolute top-4 right-4 p-2 hover:bg-zinc-100 transition-colors"
          >
            <X class="w-6 h-6 text-zinc-500" />
          </button>

          <h3 class="text-2xl font-bold text-zinc-900 mb-6 flex items-center gap-2">
            <Mail class="w-6 h-6" />
            Enviar mensaje simple
          </h3>

          <form @submit.prevent="handleContact" class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-zinc-700 mb-1">Nombre</label>
              <input 
                v-model="contactForm.name"
                type="text" 
                required
                class="w-full bg-zinc-50 border border-zinc-200 px-4 py-2 text-zinc-900 focus:outline-none focus:border-zinc-900 focus:bg-white transition-all rounded-none"
                placeholder="Tu nombre"
              >
            </div>
            
            <div>
              <label class="block text-sm font-medium text-zinc-700 mb-1">Correo</label>
              <input 
                v-model="contactForm.email"
                type="email" 
                required
                class="w-full bg-zinc-50 border border-zinc-200 px-4 py-2 text-zinc-900 focus:outline-none focus:border-zinc-900 focus:bg-white transition-all rounded-none"
                placeholder="tu@correo.com"
              >
            </div>
            
            <div>
              <label class="block text-sm font-medium text-zinc-700 mb-1">Mensaje</label>
              <textarea 
                v-model="contactForm.message"
                required
                rows="4"
                class="w-full bg-zinc-50 border border-zinc-200 px-4 py-2 text-zinc-900 focus:outline-none focus:border-zinc-900 focus:bg-white transition-all rounded-none resize-none"
                placeholder="¿En qué podemos ayudarte?"
              ></textarea>
            </div>

            <button 
              type="submit"
              :disabled="isSubmitting"
              class="w-full bg-zinc-900 hover:bg-zinc-800 disabled:bg-zinc-400 text-white py-3 font-medium transition-all flex items-center justify-center gap-2 rounded-none mt-4"
            >
              <Send v-if="!isSubmitting" class="w-4 h-4" />
              <div v-else class="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin"></div>
              {{ isSubmitting ? 'Enviando...' : 'Enviar Mensaje' }}
            </button>
          </form>
        </div>
      </div>
    </Transition>
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
