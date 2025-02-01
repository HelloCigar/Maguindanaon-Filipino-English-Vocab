export default defineEventHandler(async (event) => {
  const query = getQuery(event)

    const words = await $fetch<Response>('http://127.0.0.1:8000/api/translate', {
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