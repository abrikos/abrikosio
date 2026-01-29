import request from './fetch.js';

const store = Vue.reactive({
    count: 10,
    increment(){
        this.count++
    }
})
const init = async()=>{
    const {createApp, ref} = Vue
    const app = createApp({
        delimiters: ['[[', ']]'],
        setup() {
            const leftDrawerOpen = ref(true)
            const user = ref({email:'abrikoz@gmail.com', password:'1'})

            return {
                store,
                user,
                leftDrawerOpen,
                data(){
                    return {

                    }
                }
            }
        },
        methods: {
            login() {
                request.post('/users/login/',this.user)
            },
            inc(){
                console.log('IIII', this.store.count)
                this.store.increment()
            },
        },
        mounted(){
            request.get('/users/me/')
                .then(console.log)
        }
    })
    //const c = await component1()
    //app.component('MyButton', c)
    app.use(Quasar)
    app.mount('#app')

}
init()