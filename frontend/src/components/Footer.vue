<script setup>
const currentYear = new Date().getFullYear()
</script>

<template>
  <footer class="py-8 border-t border-white/30 bg-white/20 backdrop-blur-md text-center text-zinc-500 text-sm relative z-10">
    <p>&copy; {{ currentYear }} InnovaSoft. All systems operational.</p>
  </footer>
</template>
