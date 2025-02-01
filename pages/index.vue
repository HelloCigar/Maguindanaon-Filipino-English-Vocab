<script setup lang="ts">
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card'
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Download } from "lucide-vue-next"

// Example: Total items and per-page count
const totalItems = ref(0) // Change this dynamically
const perPage = ref(50)

const query = ref("")
const currentPage = ref(1)
const { data: wordlist } = await useAsyncData(
  'wordlist',
  () => $fetch('/api/query', {
    method: 'GET',
    query: {
      word: query.value,
      page: currentPage.value
    }
  }).then((res) =>{
    totalItems.value = res.count
    return res
  }), {
    watch: [query, currentPage]
  }
)

// Handle page change event
const handlePageChange = (page: number) => {
  console.log('Current Page:', page)
  currentPage.value = page
}

const handleDownloadCSV = () => {
  const headers = ["Maguindanaon", "Filipino", "English"]
  if (wordlist.value) {
    const rows = wordlist.value.items.map((item) => [item.maguindanaon, item.filipino, item.english])
    const csvContent = headers.join(',') + '\n' + rows.join('\n')
    const blob = new Blob([csvContent], { type: 'text/csv' })
    const url = URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.download = 'maguindanaon_filipino_english.csv'
    link.click()
  }
}
</script>

<template>
  <div class="container mx-auto px-4 py-4 sm:py-8">
    <Card class="w-full">
      <CardHeader>
        <CardTitle class="text-xl sm:text-2xl font-bold text-center">Maguindanaon-Filipino-English</CardTitle>
        <CardTitle class="text-xl sm:text-2xl font-bold text-center">Vocabulary</CardTitle>
      </CardHeader>
      <CardContent>
        <div class="flex flex-col sm:flex-row justify-between items-center mb-4 sm:mb-6 space-y-4 sm:space-y-0">
          <Input
            id="search"
            v-model="query"
            placeholder="Search a word"
            class="w-full sm:max-w-sm sm:mr-4"
          />
          <div class="flex justify-center sm:justify-start space-x-2 space-y-2 sm:space-y-0 sm:flex-row">
            <div class="flex flex-col sm:flex-row gap-2">
              <AddWordDialog />
              <Button variant="outline" class="w-full sm:w-auto" @click="handleDownloadCSV">
                <Download class="mr-2 h-4 w-4" /> CSV
              </Button>
              <DarkModeToggle />
          </div>
          </div>
        </div>
        <div class="overflow-x-auto">
          <WordTable v-if="wordlist" :wordlist="wordlist.items" />
        </div>
      </CardContent>
      <CardFooter class="flex flex-col sm:flex-row sm:justify-center md:justify-between items-center space-y-4 sm:space-y-0">
        <SourceCard class="w-full sm:w-auto" />
        <Paginator
          :total="totalItems" 
          :perPage="perPage"
          @update:page="handlePageChange" 
          class="w-full sm:w-auto"
        />
      </CardFooter>
    </Card>
  </div>
</template>