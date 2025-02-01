// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  ssr: false,
  colorMode: {
    classSuffix: '',
    preference: 'system',
    fallback: 'dark',
  },
  shadcn: {
    /**
     * Prefix for all the imported component
     */
    prefix: '',
    /**
     * Directory that the component lives in.
     * @default "./components/ui"
     */
    componentDir: './components/ui'
  },
  runtimeConfig:{
    public: {
      API_BASE_URL: "https://0601-111-125-83-172.ngrok-free.app"
    }
  },

  modules: ['shadcn-nuxt', '@nuxtjs/color-mode']
})