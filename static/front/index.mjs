import home from './home.mjs';
console.log(home)
if (HTMLScriptElement.supports?.("importmap")) {
    console.log("Browser supports import maps.");
}

const component1 = async ()=>{
    const res = await fetch('/static/MyButton.vue')
    const template = await res.text()
    console.log(template)
    return {
        template,
        setup() {
            return {
                props: ['prop'],
                data() {
                    return {item: 'test'}
                },
            }
        }
    }
}


const init = async()=>{
    const app = Vue.createApp({
        setup() {
            return {
                data(){
                    return {
                        contextHome:'zzzzz'
                    }
                }
            }
        },
        methods: {
            test() {
                const x = home
                console.log('ggggggg',x)
                x.login()
            },
            test2(){

            },
            home:()=>home
        }
    })
    //const c = await component1()
    //app.component('MyButton', c)
    app.use(Quasar)
    app.mount('#app')

}
init()