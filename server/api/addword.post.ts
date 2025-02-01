export default defineEventHandler(async (event) => {
    const body = await readBody(event)
    const API_BASE_URL = useRuntimeConfig().public.API_BASE_URL
  
      const response = await $fetch<Response>(`${API_BASE_URL}/api/add_word`, {
          method: 'POST',
          body: body,
      })
  
      return response
    })

type Response = {
    success: boolean
    message: string
}