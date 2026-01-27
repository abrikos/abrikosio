const app = Vue.createApp({
    setup () {
        return {}
    },
    methods:{
        test(){
            console.log('CCCCCcllick')
        }
    }
})
app.use(Quasar)
app.mount('#q-app')