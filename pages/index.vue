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
</script>

<template>
    <div class="container mx-auto px-4 py-8">
        <Card class="w-full">
            <CardHeader>
                <CardTitle class="text-2xl font-bold text-center">Maguindanaon-Filipino-English</CardTitle>
                <CardTitle class="text-2xl font-bold text-center">Vocabulary</CardTitle>
                <CardContent>
                    <div class="flex justify-between items-center mb-6">
                        <Input
                            id="search"
                            v-model="query"
                            placeholder="Search a Manguindanaon/Filipino/English word"
                            class="w-full max-w-sm mr-4"
                        />
                        <div class="flex space-x-2">
                        <AddWordDialog />
                        <Button variant="outline">
                            <Download class="mr-2 h-4 w-4" /> Download CSV
                        </Button>
                        <DarkModeToggle />
                        </div>
                    </div>
                    <div class="overflow-x-auto">
                        <WordTable v-if="wordlist" :wordlist="wordlist.items" />
                    </div>
                </CardContent>
            </CardHeader>
            <CardFooter class="flex justify-between">
                <SourceCard />
                <Paginator
                    :total="totalItems" 
                    :perPage="perPage"
                    @update:page="handlePageChange" 
                />
            </CardFooter>
        </Card>
    </div>
</template>