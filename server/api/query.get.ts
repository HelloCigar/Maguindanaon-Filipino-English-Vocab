export default defineEventHandler(async (event) => {
  const query = getQuery(event)
  const API_BASE_URL = useRuntimeConfig().public.API_BASE_URL

    const words = await $fetch<Response>(`${API_BASE_URL}/api/translate`, {
        query: { 
          word: query.word,
          page: query.page
         }
    })

    return words
  })

type WordList = {
  english: string
  filipino: string
  maguindanaon: string
}[]

type Response = {
  items: WordList
  count: number
}