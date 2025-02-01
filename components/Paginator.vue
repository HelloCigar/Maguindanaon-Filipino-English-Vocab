<script setup lang="ts">
import { 
  Button,
} from '@/components/ui/button'

import {
  Pagination,
  PaginationEllipsis,
  PaginationFirst,
  PaginationLast,
  PaginationList,
  PaginationListItem,
  PaginationNext,
  PaginationPrev,
} from '@/components/ui/pagination'

// Define props
const props = defineProps({
  total: { type: Number, required: true }, // Total items count
  perPage: { type: Number, default: 10 }  // Items per page (default: 10)
})

// Define emit event for sending page to the parent
const emit = defineEmits(['update:page'])

// Reactive variable for current page
const currentPage = ref(1)

// Function to update page and emit event
const onPageChange = (newPage: number) => {
  currentPage.value = newPage
  emit('update:page', newPage) // Send new page to parent
}
</script>

<template>
  <Pagination v-slot="{ page }" :total="total" :items-per-page="perPage" :sibling-count="1" show-edges :default-page="currentPage" @update:page="onPageChange">
    <PaginationList v-slot="{ items }" class="flex items-center gap-1">
      <PaginationFirst />
      <PaginationPrev />

      <template v-for="(item, index) in items">
        <PaginationListItem v-if="item.type === 'page'" :key="index" :value="item.value" as-child>
          <Button class="w-10 h-10 p-0" :variant="item.value === page ? 'default' : 'outline'">
            {{ item.value }}
          </Button>
        </PaginationListItem>
        <PaginationEllipsis v-else :key="item.type" :index="index" />
      </template>
      <PaginationNext />
      <PaginationLast />
    </PaginationList>
  </Pagination>
</template>
