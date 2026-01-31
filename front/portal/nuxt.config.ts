// https://nuxt.com/docs/api/configuration/nuxt-config
const devMode = process.env.NODE_ENV === 'development'
const title = 'Abrikos portal'
const description = 'My site'
const image = ''


export default defineNuxtConfig({
  ssr: false,
  compatibilityDate: '2025-07-15',
  app:{
    head: {
      title,
      meta:[
        { name: 'title', content: title },
        { property: 'og:site_name', content: 'Abrikoz' },
        { property: 'og:title', content: title },
        { property: 'og:description', content: description },
        { name: 'description', content: description },
        { property: 'og:type', content: 'site' },
        { property: 'og:image', content: image },
      ]
    }
  },
  devtools: { enabled: true },
  runtimeConfig: {
    public: {
      devMode: process.env.NODE_ENV !== 'production',
      authExpiration: 3600 * 24 * 30,
      authRefreshBeforeExpiration: 3000,
      authTokenName: 'access',
      authPages:['user-cabinet','post-create','post-edit']
    }
  },
  devServer: {
    port: 9000,
    // host:'abrikosio.local',
  },
  modules: [
    'nuxt-quasar-ui',
    '@pinia/nuxt',
  ],
  quasar: {
    sassVariables: '~~/public/quazar.variables.sass',
    plugins:['Notify'],
    components: {
      defaults: {
        QCard:{
          flat: true,
          bordered: true
        },
        QBtn: {
          dense: true,
          noCaps: true
        },
        QSelect: {
          outlined: true,
          dense: true
        },
      }
    },
    iconSet: 'mdi-v7',
    lang: 'ru'

  },
  nitro: {
    output: {
      dir: '/home/abrikos/PycharmProjects/abrikosio/blog_static' // Change the main output directory from '.output' to 'mydir'
    }
  }
})
