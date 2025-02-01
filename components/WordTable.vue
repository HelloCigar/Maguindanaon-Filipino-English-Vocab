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
            <TableRow v-for="word in wordlist">
                <TableCell>{{ word.maguindanaon }}</TableCell>
                <TableCell>{{ word.filipino }}</TableCell>
                <TableCell>{{ word.english }}</TableCell>
            </TableRow>
        </TableBody>
        </Table>
        </ScrollArea>
</template>