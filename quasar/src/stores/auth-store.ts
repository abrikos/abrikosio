import {defineStore, acceptHMRUpdate} from 'pinia';
import {Cookies} from 'quasar'
import type {ICredentials} from "pages/LoginPage.vue";
import axios from '../plugins/axios';

export const useCounterStore = defineStore('counter', {
  state: () => ({
    counter: 0,
  }),

  getters: {
    doubleCount: (state) => state.counter * 2,
  },

  actions: {
    increment() {
      this.counter++;
    },
  },
});

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
  }),
  actions: {
    async login(credentials: ICredentials) {
      const token = await axios.post('/token/', credentials);
      if(!token) return
      Cookies.set('auth', token.data?.access)
      await this.checkAuth()
    },
    async signup(credentials: ICredentials) {
      const user = await axios.post('/user/', credentials)
      if(!user.data.error){
        await this.login(credentials)
      }
      return user;
    },
    async checkAuth(){
      const auth = Cookies.get('auth')
      const user = await axios.get('/user/auth', {headers: {'Authorization': 'Bearer ' + auth}})
      this.user = user?.data
    },
    logout() {
      this.user = null
      Cookies.set('auth', '')
    }
  }
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useCounterStore, import.meta.hot));
}
