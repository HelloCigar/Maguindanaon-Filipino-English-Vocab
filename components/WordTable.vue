<script setup lang="ts">
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"

import { ScrollArea } from "@/components/ui/scroll-area"

type WordList = {
  english: string
  filipino: string
  maguindanaon: string
}[]

// Define props
const props = defineProps({
    wordlist: { type: Object as () => WordList, required: true },
})

</script>

<template>
  <div class="w-full">
    <ScrollArea class="h-[400px] sm:h-[600px]">
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead class="whitespace-nowrap">Manguindanaon</TableHead>
            <TableHead class="whitespace-nowrap">Filipino</TableHead>
            <TableHead class="whitespace-nowrap">English</TableHead>
          </TableRow>
        </TableHeader>
        
        <TableBody>
          <TableRow v-for="word in wordlist" :key="word.maguindanaon">
            <TableCell class="font-medium break-words">{{ word.maguindanaon }}</TableCell>
            <TableCell class="break-words">{{ word.filipino }}</TableCell>
            <TableCell class="break-words">{{ word.english }}</TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </ScrollArea>
  </div>
</template>

<style scoped>
:deep(table) {
  width: 100%;
  table-layout: fixed;
}

:deep(th),
:deep(td) {
  padding: 0.75rem;
  vertical-align: top;
}

@media (max-width: 640px) {
  :deep(table) {
    font-size: 0.875rem;
  }
  
  :deep(th),
  :deep(td) {
    padding: 0.5rem;
  }
}
</style>