<script setup lang="ts">
import { Plus } from "lucide-vue-next"
import { Label } from "@/components/ui/label"
import { Dialog, DialogClose, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog"
import { useForm } from 'vee-validate'
import { toTypedSchema } from '@vee-validate/zod'
import * as z from 'zod'
import FormItem from "./ui/form/FormItem.vue"
import { toast } from 'vue-sonner'

const formSchema = toTypedSchema(z.object({
    maguindanaon: z.string().min(2).max(100),
    filipino: z.string().min(2).max(100),   
    english: z.string().min(2).max(100),
}))

const form = useForm({
  validationSchema: formSchema,
})

const onSubmit = form.handleSubmit(async (values) => {
    console.log(values)
    const response = await $fetch('/api/addword', {
        method: 'POST',
        body: values
    })

    if (response.success) {
        toast.success(response.message, {
                action: {
                  label: 'OK',
                  onClick: () => {},
                },
            }
        )
    } else {
        toast.error(response.message, {
                action: {
                  label: 'OK',
                  onClick: () => {},
                },
            }
        )
    }
    
    
})

import { FormControl, FormField, FormLabel } from "@/components/ui/form"
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
        <Form class="space-y-4" @submit="onSubmit">
            <FormField class="space-y-2" v-slot="{ componentField }" name="maguindanaon">
                <FormItem>
                    <FormLabel>Maguindanaon</FormLabel>
                    <FormControl v-bind="componentField">
                        <Input type="text" v-bind="componentField" />
                    </FormControl>
                </FormItem>
            </FormField>
            <FormField class="space-y-2" v-slot="{ componentField }" name="filipino">
                <FormItem>
                    <FormLabel>Filipino</FormLabel>
                    <FormControl v-bind="componentField">
                        <Input type="text" v-bind="componentField" />
                    </FormControl>
                </FormItem>
            </FormField>
            <FormField class="space-y-2" v-slot="{ componentField }" name="english">
                <FormItem>
                    <FormLabel>English</FormLabel>
                    <FormControl v-bind="componentField">
                        <Input type="text" v-bind="componentField" />
                    </FormControl>
                </FormItem>
            </FormField>
            <DialogClose as-child>
                <Button type="submit">Add Word</Button>
            </DialogClose>
        </Form>
        </DialogContent>
    </Dialog>
</template>