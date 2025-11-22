<script setup>
import { Cpu } from 'lucide-vue-next'

defineEmits(['logo-click'])
</script>

<template>
  <nav class="fixed top-0 w-full z-50 bg-white/60 backdrop-blur-xl border-b border-white/40 shadow-sm supports-[backdrop-filter]:bg-white/60">
    <div class="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
      <div 
        @click="$emit('logo-click')"
        class="flex items-center gap-2 cursor-pointer hover:opacity-80 transition-opacity"
      >
        <Cpu class="w-6 h-6 text-zinc-900" />
        <span class="font-bold text-xl tracking-tighter text-zinc-900">Innova<span class="text-zinc-500">Soft</span></span>
      </div>
      <div class="hidden md:flex gap-8 text-sm font-medium text-zinc-500">
        <a href="#projects" class="hover:text-zinc-900 transition-all active:scale-95 transform">Proyectos</a>
        <a href="#demo" class="hover:text-zinc-900 transition-all active:scale-95 transform">Demo Center</a>
        <a href="#founder" class="hover:text-zinc-900 transition-all active:scale-95 transform">Fundador</a>
      </div>
      <button class="bg-zinc-900 hover:bg-zinc-800 text-white px-5 py-2 text-sm font-medium transition-all rounded-none">
        Contactar
      </button>
    </div>
  </nav>
</template>
