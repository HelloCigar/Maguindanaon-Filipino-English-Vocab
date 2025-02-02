<script setup lang="ts">
import { Toaster } from '@/components/ui/sonner'
useSeoMeta({
  title: 'Maguindanaon-Filipino-English Vocabulary',
  ogTitle: 'Maguindanaon-Filipino-English Vocabulary',
  description: 'Maguindanaon vocabulary based on the book "Vocabulary: Magindanawn-Pilipino-English; Pilipino-English-Magindanawn; English-Pilipino-Magindanawn." by Fleischman et. al',
  ogDescription: 'Maguindanaon vocabulary based on the book "Vocabulary: Magindanawn-Pilipino-English; Pilipino-English-Magindanawn; English-Pilipino-Magindanawn." by Fleischman et. al',
  robots: 'index, follow',
  ogType: 'website',
  ogUrl: 'https://https://maguindanaon-filipino-english-vocab.netlify.app/',
  charset: 'utf-8',
})

</script>

<template>
  <Toaster />
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>
