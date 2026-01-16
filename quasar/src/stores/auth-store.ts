import {defineStore, acceptHMRUpdate} from 'pinia';
import {Cookies} from 'quasar'
import axios from "axios";
import {ICredentials} from "pages/LoginPage.vue";

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
    async login(user: ICredentials) {
      const csrftoken = Cookies.get('csrftoken')
      const token = await axios.post('/token/', user, {headers: {'CSRFToken': csrftoken}})
      // const auth = await axios.get('/user/auth', {headers: {'Authorization': 'Bearer ' + token.data.access}})
      // this.user = auth.data
      Cookies.set('auth', token.data.access)
      await this.checkAuth()
    },
    async checkAuth(){
      const auth = Cookies.get('auth')
      const user = await axios.get('/user/auth', {headers: {'Authorization': 'Bearer ' + auth}})
      this.user = user.data
    },
    async logout() {
      this.user = null
      Cookies.set('auth', '')
    }
  }
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useCounterStore, import.meta.hot));
}
