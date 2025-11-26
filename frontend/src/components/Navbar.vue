<script setup>


defineEmits(['logo-click'])
</script>

<template>
  <nav class="fixed top-0 w-full z-50 bg-white/60 backdrop-blur-xl border-b border-white/40 shadow-sm supports-[backdrop-filter]:bg-white/60">
    <div class="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
      <div 
        @click="$emit('logo-click')"
        class="flex items-center gap-2 cursor-pointer hover:opacity-80 transition-opacity"
      >
        <img src="/innovasoft_logo_icon.png" alt="InnovaSoft Logo" class="h-8 rounded-lg shadow-sm" />
        <span class="font-bold text-xl tracking-tighter text-zinc-900">Innova<span class="text-zinc-500">Soft</span></span>
      </div>
      <div class="hidden md:flex gap-8 text-sm font-medium text-zinc-500">
        <a href="#experience" class="hover:text-zinc-900 transition-all active:scale-95 transform">Experiencia</a>
        <a href="#projects" class="hover:text-zinc-900 transition-all active:scale-95 transform">Proyectos</a>
        <a href="#skills" class="hover:text-zinc-900 transition-all active:scale-95 transform">Habilidades</a>
        <a href="#education" class="hover:text-zinc-900 transition-all active:scale-95 transform">Educación</a>
        <a href="#demos" class="hover:text-zinc-900 transition-all active:scale-95 transform">Demo</a>
      </div>
      <a href="#contact" class="bg-zinc-900 hover:bg-zinc-800 text-white px-5 py-2 text-sm font-medium transition-all rounded-none">Contactar</a>
    </div>
  </nav>
</template>
