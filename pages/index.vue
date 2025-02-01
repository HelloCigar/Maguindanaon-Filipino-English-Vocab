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
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "@/components/ui/hover-card"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"

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
                            <TableRow v-for="word in 100" :key="word">
                                <TableCell>{word}</TableCell>
                                <TableCell>{word}</TableCell>
                                <TableCell>{word}</TableCell>
                            </TableRow>
                        </TableBody>
                        
                        </Table>
                    </ScrollArea>
                    </div>
                    </CardContent>
            </CardHeader>
                
            <CardFooter>
                <HoverCard>
                    <HoverCardTrigger>
                        <Button variant="link" >
                            <span class="text-center underline italic">source</span>
                        </Button>
                    </HoverCardTrigger>
                    <HoverCardContent class="w-80">
                    <div class="flex justify-between space-x-4">
                        <div class="space-y-1">
                        <h4 class="text-sm font-semibold">
                            Vocabulary: Magindanawn-Pilipino-English; Pilipino-English-Magindanawn; English-Pilipino-Magindanawn. 
                        </h4>
                        <p class="text-sm">
                            Fleischman, E., Glang, N., Solaiman, M., Ayub, H. A., & Daud, F. (1981). Summer Institute of Linguistics.
                        </p>
                        <div class="flex items-center pt-2">
                            <NuxtLink href="https://www.sil.org/resources/archives/23880">
                            <span class="text-xs text-muted-foreground underline">
                                 https://www.sil.org/resources/archives/23880
                            </span>
                            </NuxtLink>
                        </div>
                        </div>
                    </div>
                    </HoverCardContent>
                </HoverCard>
            </CardFooter>
        </Card>
    </div>
</template>