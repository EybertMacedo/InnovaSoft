<script setup>
import { MessageCircle } from 'lucide-vue-next'
</script>

<template>
  <a 
    href="https://wa.me/+51960208373?text=Hola%20InnovaSoft,%20me%20gustaria%20realizar%20una%20consulta" 
    target="_blank" 
    rel="noopener noreferrer"
    class="fixed bottom-8 right-8 z-50 flex items-center justify-center w-14 h-14 bg-[#25D366] hover:bg-[#20bd5a] text-white rounded-full shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-110 group"
    aria-label="Chat on WhatsApp"
  >
    <!-- WhatsApp SVG Icon -->
    <svg 
      viewBox="0 0 24 24" 
      width="24" 
      height="24" 
      stroke="currentColor" 
      stroke-width="2" 
      fill="none" 
      stroke-linecap="round" 
      stroke-linejoin="round" 
      class="w-8 h-8 fill-current stroke-none"
    >
      <path d="M17.498 14.382c-.301-.15-1.767-.867-2.04-.966-.273-.101-.473-.15-.673.15-.197.295-.771.964-.944 1.162-.175.195-.349.21-.646.075-.3-.15-1.263-.465-2.403-1.485-.888-.795-1.484-1.77-1.66-2.07-.174-.3-.019-.465.13-.615.136-.135.303-.345.451-.523.146-.181.194-.301.297-.496.1-.21.049-.375-.025-.524-.075-.15-.672-1.62-.922-2.206-.24-.584-.487-.51-.672-.51h-.572c-.197 0-.52.074-.793.372-.27.297-1.043 1.016-1.043 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.572-.349z"></path>
      <path d="M12 0C5.373 0 0 5.373 0 12c0 2.125.55 4.125 1.5 5.875L.5 23.5l5.75-1C7.875 23.45 9.875 24 12 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 21.875c-1.8 0-3.525-.475-5.025-1.3l-.35-.2-3.725.625.65-3.65-.225-.375c-.9-1.575-1.4-3.375-1.4-5.25 0-5.325 4.325-9.625 9.625-9.625 5.325 0 9.625 4.325 9.625 9.625s-4.3 9.625-9.625 9.625z"></path>
    </svg>
    
    <!-- Ping Animation -->
    <span class="absolute top-0 right-0 flex h-3 w-3">
      <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
      <span class="relative inline-flex rounded-full h-3 w-3 bg-green-500"></span>
    </span>
  </a>
</template>
