<script setup>
import { ref, onMounted } from 'vue'
import { 
  Zap, 
  MessageSquare, 
  Send, 
  Eye, 
  BarChart3 
} from 'lucide-vue-next'

// 1. Chat Simulator
const chatMessages = ref([
  { id: 1, text: 'Hola, necesito optimizar mi línea de producción.', sender: 'user' }
])
const chatInput = ref('')
const isTyping = ref(false)

const sendMessage = () => {
  if (!chatInput.value.trim()) return
  
  // Add user message
  chatMessages.value.push({
    id: Date.now(),
    text: chatInput.value,
    sender: 'user'
  })
  chatInput.value = ''
  
  // Simulate bot typing
  isTyping.value = true
  setTimeout(() => {
    isTyping.value = false
    chatMessages.value.push({
      id: Date.now() + 1,
      text: '[DEMO] Esta es una simulación estática. Para hablar con la IA real, usa el botón flotante en la esquina inferior derecha ↘️',
      sender: 'bot'
    })
  }, 1500)
}

// 2. Vision Simulator
const isScanning = ref(false)
const toggleScan = () => {
  isScanning.value = !isScanning.value
}

// 3. Dashboard Simulator
const metrics = ref([
  { label: 'Uptime', value: 0, target: 99.9, suffix: '%' },
  { label: 'Anomalies', value: 0, target: 12, suffix: '/hr' },
  { label: 'Efficiency', value: 0, target: 85, suffix: '%' }
])

const animateMetrics = () => {
  metrics.value.forEach(metric => {
    let current = 0
    const interval = setInterval(() => {
      current += metric.target / 50
      if (current >= metric.target) {
        metric.value = metric.target
        clearInterval(interval)
      } else {
        metric.value = Math.floor(current * 10) / 10
      }
    }, 20)
  })
}

onMounted(() => {
  animateMetrics()
})
</script>

<template>
  <section id="demo" class="flex flex-col justify-center py-12 px-6 relative overflow-hidden z-10">
    <div class="max-w-7xl mx-auto relative z-10">
      <h2 class="text-3xl font-bold text-zinc-900 mb-12 flex items-center gap-3">
        <Zap class="w-8 h-8 text-zinc-900" />
        Interactive Demo Center
      </h2>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        
        <!-- 1. CHAT SIMULATOR -->
        <div class="bg-white/40 backdrop-blur-xl border border-white/50 rounded-none overflow-hidden flex flex-col h-[500px] shadow-lg hover:shadow-xl transition-all duration-500">
          <div class="p-4 border-b border-white/30 bg-white/20 flex items-center justify-between">
            <span class="font-semibold text-zinc-900 flex items-center gap-2">
              <MessageSquare class="w-4 h-4 text-zinc-900" />
              Demo Chat Simulator
            </span>
            <span class="text-xs text-emerald-600 flex items-center gap-1">
              <span class="w-2 h-2 bg-emerald-500 rounded-full animate-pulse"></span>
              Online
            </span>
          </div>
          
          <div class="flex-1 p-4 overflow-y-auto space-y-4 scrollbar-thin scrollbar-thumb-zinc-300/50">
            <TransitionGroup name="message">
              <div 
                v-for="msg in chatMessages" 
                :key="msg.id"
                :class="['max-w-[80%] p-3 text-sm border rounded-none backdrop-blur-sm', msg.sender === 'user' ? 'ml-auto bg-zinc-900/90 text-white border-zinc-900/50' : 'bg-white/60 text-zinc-700 border-white/50']"
              >
                {{ msg.text }}
              </div>
            </TransitionGroup>
            
            <div v-if="isTyping" class="bg-white/60 border border-white/50 text-zinc-500 p-3 inline-block text-xs animate-pulse rounded-none backdrop-blur-sm">
              Escribiendo...
            </div>
          </div>
          
          <div class="p-4 border-t border-white/30 bg-white/20 flex gap-2">
            <input 
              v-model="chatInput" 
              @keyup.enter="sendMessage"
              type="text" 
              placeholder="Escribe un mensaje..." 
              class="flex-1 bg-white/50 border border-white/50 px-4 py-2 text-sm text-zinc-900 focus:outline-none focus:bg-white/80 focus:border-zinc-900 transition-all placeholder:text-zinc-400 rounded-none"
            >
            <button 
              @click="sendMessage"
              class="bg-zinc-900 hover:bg-zinc-800 text-white p-2 transition-colors rounded-none shadow-lg"
            >
              <Send class="w-4 h-4" />
            </button>
          </div>
        </div>

        <!-- 2. VISION SIMULATOR -->
        <div class="bg-white/40 backdrop-blur-xl border border-white/50 rounded-none overflow-hidden flex flex-col h-[500px] shadow-lg hover:shadow-xl transition-all duration-500">
          <div class="p-4 border-b border-white/30 bg-white/20 flex items-center justify-between">
            <span class="font-semibold text-zinc-900 flex items-center gap-2">
              <Eye class="w-4 h-4 text-zinc-900" />
              Safety Vision v2.0
            </span>
            <button 
              @click="toggleScan"
              :class="isScanning ? 'bg-red-50/80 text-red-600 border-red-200' : 'bg-white/50 text-zinc-600 border-white/50'"
              class="text-xs px-3 py-1 border transition-all font-medium rounded-none backdrop-blur-sm"
            >
              {{ isScanning ? 'STOP SCAN' : 'START SCAN' }}
            </button>
          </div>
          
          <div class="flex-1 relative bg-zinc-100/50 overflow-hidden group">
            <!-- Mock Industrial Image (CSS Pattern) -->
            <div class="absolute inset-0 opacity-10 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-zinc-400 via-zinc-200 to-zinc-100"></div>
            <div class="absolute inset-0 flex items-center justify-center">
               <div class="grid grid-cols-2 gap-4 w-3/4 h-3/4 opacity-10">
                  <div class="bg-zinc-900 rounded-none"></div>
                  <div class="bg-zinc-900 rounded-none"></div>
                  <div class="bg-zinc-900 rounded-none col-span-2"></div>
               </div>
            </div>
            
            <!-- Scanning Overlay -->
            <div v-if="isScanning" class="absolute inset-0 z-10">
              <div class="absolute top-0 left-0 w-full h-1 bg-red-500/50 animate-scan"></div>
              
              <!-- Bounding Boxes -->
              <div class="absolute top-[20%] left-[15%] w-[30%] h-[40%] border-2 border-red-500 bg-red-500/10 animate-pulse flex items-start justify-between p-1 backdrop-blur-[2px]">
                <span class="bg-red-500 text-white text-[10px] px-1 font-bold rounded-none">DANGER ZONE</span>
                <span class="text-red-600 text-[10px] font-mono font-bold bg-white/80 px-1 rounded-none">98%</span>
              </div>
              
              <div class="absolute bottom-[15%] right-[20%] w-[25%] h-[25%] border-2 border-emerald-500 bg-emerald-500/10 flex items-start justify-between p-1 backdrop-blur-[2px]">
                <span class="bg-emerald-500 text-white text-[10px] px-1 font-bold rounded-none">SAFE</span>
                <span class="text-emerald-600 text-[10px] font-mono font-bold bg-white/80 px-1 rounded-none">99%</span>
              </div>
            </div>
            
            <div v-else class="absolute inset-0 flex items-center justify-center text-zinc-400 flex-col gap-2">
              <Eye class="w-12 h-12 opacity-20" />
              <span class="text-sm">System Standby</span>
            </div>
          </div>
          
          <div class="p-3 bg-white/40 font-mono text-xs text-zinc-500 border-t border-white/30 backdrop-blur-md">
            > YOLOv8 Inference: {{ isScanning ? '14ms' : '0ms' }}
          </div>
        </div>

        <!-- 3. DASHBOARD SIMULATOR -->
        <div class="bg-white/40 backdrop-blur-xl border border-white/50 rounded-none overflow-hidden flex flex-col h-[500px] shadow-lg hover:shadow-xl transition-all duration-500">
          <div class="p-4 border-b border-white/30 bg-white/20">
            <span class="font-semibold text-zinc-900 flex items-center gap-2">
              <BarChart3 class="w-4 h-4 text-zinc-900" />
              Real-time Metrics
            </span>
          </div>
          
          <div class="flex-1 p-6 flex flex-col justify-center gap-8">
            <div v-for="(metric, idx) in metrics" :key="idx" class="relative">
              <div class="flex justify-between text-sm mb-2 text-zinc-600">
                <span>{{ metric.label }}</span>
                <span class="text-zinc-900 font-mono font-medium">{{ metric.value }}{{ metric.suffix }}</span>
              </div>
              <div class="h-2 bg-zinc-200/50 rounded-none overflow-hidden backdrop-blur-sm">
                <div 
                  class="h-full bg-zinc-900 transition-all duration-1000"
                  :style="{ width: `${(metric.value / (metric.target * 1.2)) * 100}%` }"
                ></div>
              </div>
            </div>
            
            <!-- Mini Chart Mock -->
            <div class="mt-4 h-32 flex items-end gap-1 justify-between opacity-30">
              <div v-for="n in 20" :key="n" 
                class="w-full bg-zinc-900 rounded-t-none backdrop-blur-sm"
                :style="{ height: `${Math.random() * 100}%` }"
              ></div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
</template>

<style scoped>
@keyframes scan {
  0% { top: 0%; }
  50% { top: 100%; }
  100% { top: 0%; }
}

.animate-scan {
  animation: scan 3s linear infinite;
}

.message-enter-active,
.message-leave-active {
  transition: all 0.3s ease;
}
.message-enter-from,
.message-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>
