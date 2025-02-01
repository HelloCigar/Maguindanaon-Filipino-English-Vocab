export default defineEventHandler(async (event) => {
    const body = await readBody(event)
  
      const response = await $fetch<Response>('http://127.0.0.1:8000/api/add_word', {
          method: 'POST',
          body: body,
      })
  
      return response
    })

type Response = {
    success: boolean
    message: string
}