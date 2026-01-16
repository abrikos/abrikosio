// https://nuxt.com/docs/api/configuration/nuxt-config
import path from'path'
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  ssr: false,
  modules: [
    'nuxt-quasar-ui',
    '@pinia/nuxt',
  ],
  quasar: {
    //sassVariables: '~~/public/quazar.variables.sass',
    plugins:['Notify'],
    components: {
      defaults: {
        QCard:{
          flat: true,
          bordered: true
        },
        QBtn: {
          dense: true,
          flat: true,
          noCaps: true
        },
        QSelect: {
          outlined: true,
          dense: true
        },
        QInput: {
          outlined: true,
          dense: true
        }
      }
    },
    iconSet: 'mdi-v7',
    lang: 'ru'

  },

  nitro: {
    output:{
      publicDir: path.join(__dirname,'../blog/templates/static')
    }
  }
})
