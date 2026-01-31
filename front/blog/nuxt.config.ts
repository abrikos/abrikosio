// https://nuxt.com/docs/api/configuration/nuxt-config
const devMode = process.env.NODE_ENV === 'development'
export default defineNuxtConfig({
  ssr: false,
  compatibilityDate: '2025-07-15',
  app:{
    head: {
      title: '{{ title }}',
      meta:[
        { name: 'title', content: '{{ title }}' },
        { property: 'og:site_name', content: 'Abrikosio' },
        { property: 'og:title', content: '{{ title }}' },
        { property: 'og:description', content: '{{short}}' },
        { name: 'description', content: '{{short}}' },
        { property: 'og:type', content: 'article' },
        { property: 'og:image', content: '{{poster}}' },
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

  }
})
