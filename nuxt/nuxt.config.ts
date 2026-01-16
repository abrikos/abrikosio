// https://nuxt.com/docs/api/configuration/nuxt-config
import path from'path'

export default defineNuxtConfig({
  app: {
    //baseURL: '/pages/',
    buildAssetsDir:'static'
  },
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  nitro: {
    output:{
      publicDir: path.join(__dirname,'../static/nuxt')
    }
  }

})
