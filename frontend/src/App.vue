<script setup>
import { ref } from 'vue'
import Navbar from './components/Navbar.vue'
import Hero from './components/Hero.vue'
import ProjectsGrid from './components/ProjectsGrid.vue'
import DemoCenter from './components/DemoCenter.vue'
import FounderProfile from './components/FounderProfile.vue'
import Footer from './components/Footer.vue'
import WhatsAppButton from './components/WhatsAppButton.vue'
import ChatWidget from './components/ChatWidget.vue'

const heroRef = ref(null)

const handleLogoClick = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' })
  heroRef.value?.triggerShimmer()
}
</script>

<template>
  <div class="min-h-screen bg-[#F5F5F7] text-zinc-900 font-sans selection:bg-zinc-900 selection:text-white relative overflow-x-hidden">
    <!-- Ambient Liquid Background -->
    <div class="fixed inset-0 overflow-hidden pointer-events-none">
      <div class="absolute top-[-20%] left-[-10%] w-[70%] h-[70%] rounded-full bg-blue-400/20 blur-[120px] animate-blob mix-blend-multiply"></div>
      <div class="absolute top-[-10%] right-[-20%] w-[60%] h-[60%] rounded-full bg-purple-400/20 blur-[120px] animate-blob animation-delay-2000 mix-blend-multiply"></div>
      <div class="absolute bottom-[-20%] left-[20%] w-[60%] h-[60%] rounded-full bg-indigo-400/20 blur-[120px] animate-blob animation-delay-4000 mix-blend-multiply"></div>
    </div>
    <Navbar @logo-click="handleLogoClick" />
    <Hero ref="heroRef" />
    <ProjectsGrid />
    <DemoCenter />
    <FounderProfile />
    <Footer />
    <WhatsAppButton />
    <ChatWidget />
  </div>
</template>
