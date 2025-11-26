<script setup>
const currentYear = new Date().getFullYear()
</script>

<template>
  <footer class="py-8 bg-zinc-900 relative overflow-hidden">
    <!-- Background Grid -->
    <div class="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px]"></div>
    
    <div class="relative z-10 border-t border-zinc-800 pt-8 text-center text-zinc-500 text-sm">
      <p>&copy; {{ currentYear }} InnovaSoft. All systems operational.</p>
    </div>
  </footer>
</template>
