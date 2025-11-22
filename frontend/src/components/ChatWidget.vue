<script setup>
import { ref, nextTick, watch } from 'vue'
import { MessageCircle, X, Send, Bot, User } from 'lucide-vue-next'

const isOpen = ref(false)
const messages = ref([
  { role: 'assistant', content: '¡Hola! Soy el asistente virtual de InnovaSoft. ¿En qué puedo ayudarte hoy?' }
])
const userInput = ref('')
const isLoading = ref(false)
const messagesContainer = ref(null)

const scrollToBottom = async () => {
  await nextTick()
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
}

watch(messages, scrollToBottom, { deep: true })
watch(isOpen, () => {
  if (isOpen.value) scrollToBottom()
})

const sendMessage = async () => {
  if (!userInput.value.trim() || isLoading.value) return

  const userMsg = userInput.value.trim()
  messages.value.push({ role: 'user', content: userMsg })
  userInput.value = ''
  isLoading.value = true

  try {
    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: userMsg })
    })

    if (!response.ok) throw new Error('Error en la respuesta')

    const data = await response.json()
    messages.value.push({ role: 'assistant', content: data.response })
  } catch (error) {
    console.error(error)
    messages.value.push({ role: 'assistant', content: 'Lo siento, tuve un problema al procesar tu mensaje. Por favor intenta de nuevo.' })
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="fixed bottom-6 right-6 z-50 flex flex-col items-end">
    <!-- Chat Window -->
    <Transition name="slide-up">
      <div 
        v-if="isOpen"
        class="mb-4 w-[350px] max-w-[calc(100vw-3rem)] bg-white border border-zinc-200 shadow-2xl flex flex-col overflow-hidden rounded-none"
        style="height: 500px; max-height: calc(100vh - 150px);"
      >
        <!-- Header -->
        <div class="bg-zinc-900 text-white p-4 flex justify-between items-center">
          <div class="flex items-center gap-2">
            <Bot class="w-5 h-5" />
            <span class="font-bold">InnovaSoft AI</span>
          </div>
          <button @click="isOpen = false" class="hover:bg-zinc-800 p-1 rounded transition-colors">
            <X class="w-5 h-5" />
          </button>
        </div>

        <!-- Messages -->
        <div 
          ref="messagesContainer"
          class="flex-1 overflow-y-auto p-4 space-y-4 bg-zinc-50"
        >
          <div 
            v-for="(msg, index) in messages" 
            :key="index"
            class="flex gap-3"
            :class="msg.role === 'user' ? 'flex-row-reverse' : ''"
          >
            <div 
              class="w-8 h-8 rounded-full flex items-center justify-center shrink-0"
              :class="msg.role === 'user' ? 'bg-zinc-900 text-white' : 'bg-blue-600 text-white'"
            >
              <User v-if="msg.role === 'user'" class="w-5 h-5" />
              <Bot v-else class="w-5 h-5" />
            </div>
            
            <div 
              class="max-w-[80%] p-3 text-sm leading-relaxed shadow-sm"
              :class="msg.role === 'user' ? 'bg-white border border-zinc-200 text-zinc-800' : 'bg-blue-50 border border-blue-100 text-zinc-800'"
            >
              {{ msg.content }}
            </div>
          </div>

          <div v-if="isLoading" class="flex gap-3">
            <div class="w-8 h-8 rounded-full bg-blue-600 text-white flex items-center justify-center shrink-0">
              <Bot class="w-5 h-5" />
            </div>
            <div class="bg-blue-50 border border-blue-100 p-3 text-sm text-zinc-500 flex items-center gap-1">
              <span class="w-2 h-2 bg-zinc-400 rounded-full animate-bounce" style="animation-delay: 0ms"></span>
              <span class="w-2 h-2 bg-zinc-400 rounded-full animate-bounce" style="animation-delay: 150ms"></span>
              <span class="w-2 h-2 bg-zinc-400 rounded-full animate-bounce" style="animation-delay: 300ms"></span>
            </div>
          </div>
        </div>

        <!-- Input -->
        <form @submit.prevent="sendMessage" class="p-4 bg-white border-t border-zinc-100 flex gap-2">
          <input 
            v-model="userInput"
            type="text" 
            placeholder="Pregunta sobre mis proyectos..." 
            class="flex-1 bg-zinc-50 border border-zinc-200 px-3 py-2 text-sm focus:outline-none focus:border-zinc-900 transition-colors"
          >
          <button 
            type="submit" 
            :disabled="isLoading || !userInput.trim()"
            class="bg-zinc-900 text-white p-2 hover:bg-zinc-800 disabled:bg-zinc-300 disabled:cursor-not-allowed transition-colors"
          >
            <Send class="w-5 h-5" />
          </button>
        </form>
      </div>
    </Transition>

    <!-- Toggle Button -->
    <button 
      @click="isOpen = !isOpen"
      class="w-14 h-14 bg-zinc-900 text-white shadow-xl flex items-center justify-center hover:scale-110 transition-transform duration-300 group"
    >
      <MessageCircle v-if="!isOpen" class="w-7 h-7 group-hover:rotate-12 transition-transform" />
      <X v-else class="w-7 h-7" />
    </button>
  </div>
</template>

<style scoped>
.slide-up-enter-active,
.slide-up-leave-active {
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.slide-up-enter-from,
.slide-up-leave-to {
  opacity: 0;
  transform: translateY(20px) scale(0.95);
}
</style>
