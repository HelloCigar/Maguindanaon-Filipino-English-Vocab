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
import { Dialog, DialogClose, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog"
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { Download, Plus } from "lucide-vue-next"
import { ScrollArea } from "@/components/ui/scroll-area"

// Example: Total items and per-page count
const totalItems = ref(0) // Change this dynamically
const perPage = ref(15)

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

console.log(totalItems.value)


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
                        <Dialog>
                            <DialogTrigger>
                            <Button variant="outline">
                                <Plus class="mr-2 h-4 w-4" /> Add Word
                            </Button>
                            </DialogTrigger>
                            <DialogContent class="sm:max-w-[425px]">
                            <DialogHeader>
                                <DialogTitle>Add New Word</DialogTitle>
                            </DialogHeader>
                            <form class="space-y-4">
                                <div>
                                <Label htmlFor="english">English</Label>
                                <Input
                                    id="english"
                                    required
                                />
                                </div>
                                <div>
                                <Label htmlFor="spanish">Spanish</Label>
                                <Input
                                    id="spanish"
                                    required
                                />
                                </div>
                                <div>
                                <Label htmlFor="french">French</Label>
                                <Input
                                    id="french"
                                    required
                                />
                                </div>
                                <Button type="submit">Add Word</Button>
                            </form>
                            </DialogContent>
                        </Dialog>
                        <Button variant="outline">
                            <Download class="mr-2 h-4 w-4" /> Download CSV
                        </Button>
                        </div>
                    </div>
                    <div class="overflow-x-auto">
                        <ScrollArea class="h-[600px]">
                        <Table>
                        <TableHeader>
                            <TableRow>
                            <TableHead class="w-1/3">Manguindanaon</TableHead>
                            <TableHead class="w-1/3">Filipino</TableHead>
                            <TableHead class="w-1/3">English</TableHead>
                            </TableRow>
                        </TableHeader>
                        
                        <TableBody>
                            <TableRow v-for="word in wordlist?.items">
                                <TableCell>{{ word.maguindanaon }}</TableCell>
                                <TableCell>{{ word.filipino }}</TableCell>
                                <TableCell>{{ word.english }}</TableCell>
                            </TableRow>
                        </TableBody>
                        
                        </Table>
                    </ScrollArea>
                    </div>
                </CardContent>
            </CardHeader>
            <CardFooter class="flex justify-between">
                <SourceCard />
                <Pages 
                    :total="totalItems" 
                    :perPage="perPage"
                    @update:page="handlePageChange" 
                />
            </CardFooter>
        </Card>
    </div>
</template>