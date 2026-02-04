import {defineStore} from 'pinia';

export interface UserPayloadInterface {
    id?: number;
    email?: string;
    password?: string;
    error?: string;
    avatar?: string;
    is_admin?: boolean;
    publisher?: boolean;
}

export const useCustomStore = defineStore('auth', {
    state: (): { loading: boolean, loggedUser: UserPayloadInterface | undefined, redirect: string } => ({
        loggedUser: undefined,
        loading: false,
        redirect: '',
    }),
    actions: {
        setRedirect(path: string) {
            this.redirect = path
        },
        setLoading() {
            this.loading = true
        },
        unsetLoading() {
            this.loading = false
        },


        async login(credentials: UserPayloadInterface) {
            const token = await useNuxtApp().$POST(`/users/login/`, credentials)
            if(token?.id) {
                navigateTo(this.redirect)
            }
        },
        async signup(credentials: UserPayloadInterface) {
            const user = await useNuxtApp().$POST('/users/', credentials) as UserPayloadInterface
            if (user?.id) {
                await this.login(credentials);
            }
        },
        async getMe() {
            const user = await useNuxtApp().$GET('/users/me/') as UserPayloadInterface
            if (user?.id) {
                this.loggedUser = user;
                return this.loggedUser;
            }
        },
        logout() {
            this.loggedUser = undefined;
            const config = useRuntimeConfig()
            const cookie = useCookie(config.public.authTokenName)
            cookie.value = '';
        },

    },
});
