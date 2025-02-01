<script setup lang="ts">
import { Plus } from "lucide-vue-next"
import { Label } from "@/components/ui/label"
import { Dialog, DialogClose, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog"

</script>

<template>
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
</template>