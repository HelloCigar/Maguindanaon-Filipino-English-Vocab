export default defineEventHandler(async (event) => {
  const query = getQuery(event)

    const words = await $fetch<{
      english: string
      filipino: string
      maguindanaon: string
      }[]>('http://127.0.0.1:8000/api/translate', {
        query: { word: query.word }
    })

    return words
  })
  