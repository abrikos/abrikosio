import {useCustomStore} from '~/store/custom-store'
import moment from "moment";
import {useQuasar} from 'quasar'
import axios from 'axios'

export default defineNuxtPlugin((_nuxtApp) => {
    const config = useRuntimeConfig()
    const devMode = process.dev
    const $q = useQuasar()
    const {logout, setLoading, unsetLoading} = useCustomStore()

    function getHeaders(ct?: string | undefined) {
        const access_token = useCookie(config.public.authTokenName)
        return {
            Authorization: access_token.value ? `Bearer ${access_token.value}` : '',
            'Content-Type': ct
        }
    }

    const instance = axios.create({
        baseURL: devMode ? 'http://127.0.0.1:8000/api' : '/api',
    });

    instance.interceptors.response.use(
        (res) => {
            devMode && console.log(res.config.method, ':', res.config.url, res.data);
            return typeof res.data === 'object' ? res.data : {};
        },
        (e) => {
            devMode && console.log(e.response);
            const error:{status:number,messages:string[]} = {status: 0, messages:[]}
            switch (true) {
                case e.status === 401:
                    return
                case e.status >= 500:
                    error.messages = [e.statusText]
                    error.status = e.status
                    break
                default:
                    if (Array.isArray(e.response.data.detail)) {
                        error.messages = e.response.data.detail.map((detail:any) => `${detail.loc[1]}: ${detail.msg}`)

                    } else {
                        error.messages = [e.status + ': ' + JSON.stringify(e.response.data)];

                    }
            }
            for (const message of error.messages) {
                $q.notify({
                    group: false,
                    color: 'negative',
                    icon: 'mdi-alert-circle',
                    message,
                    position: 'bottom-left',
                })
            }

        },
    );


    const showResponse = false
    return {
        provide: {
            POST: async (path: string, body?: any): Promise<any> => {
                setLoading()
                if (devMode) console.log('POST', path, body);
                const res = await instance.post(path, body, {headers: getHeaders()})
                if (res && devMode && showResponse) console.log('POST response:', path, res)
                unsetLoading()
                return res
            },
            UPLOAD: async (path: string, body?: any): Promise<any> => {
                setLoading()
                //await new Promise(resolve => setTimeout(resolve, 5000));
                if (devMode) console.log('UPLOAD', path, body);
                const res = await instance.post(path, body, {headers: getHeaders('multipart/form-data')})
                if (res && devMode && showResponse) console.log('POST response:', path, res)
                unsetLoading()
                return res
            },
            PATCH: async (path: string, body?: any): Promise<any> => {
                setLoading()
                //await new Promise(resolve => setTimeout(resolve, 5000));
                if (devMode) console.log('PATCH', path, body);
                const res = await instance.patch(path, body, {headers: getHeaders()})
                if (res && devMode && showResponse) console.log('PATCH response:', path, res)
                unsetLoading()
                return res
            },
            PUT: async (path: string, body?: any): Promise<any> => {
                setLoading()
                if (devMode) console.log('PUT', path, body);
                const res = await instance.put(path, body, {headers: getHeaders()})
                if (res && devMode && showResponse) console.log('PUT response:', path, res)
                unsetLoading()
                return res
            },
            GET: async (path: string): Promise<any> => {
                setLoading()
                if (devMode) console.log('GET', path);
                let res = await instance.get(path, {headers: getHeaders()})
                if (res && devMode && showResponse) console.log('GET response:', path, res)
                unsetLoading()
                return res
            },
            DELETE: async (path: string): Promise<any> => {
                setLoading()
                if (devMode) console.log('DEL', path);
                const res = await instance.delete(path, {headers: getHeaders()})
                if (res && devMode && showResponse) console.log('DEL response:', path, res)
                unsetLoading()
                return res
            },
        }
    }
})
