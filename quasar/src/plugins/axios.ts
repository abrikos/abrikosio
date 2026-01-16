import axios from 'axios';
import { Cookies, Notify } from 'quasar';

const instance = axios.create({
  baseURL: '/api',
  headers: { CSRFToken: Cookies.get('csrftoken'), Authorization: 'Bearer ' + Cookies.get('auth') },
});
instance.interceptors.response.use(
  (res) => {
    //console.log(res.config.method, ':', res.config.url, res.data);
    return res;
  },
  (error) => {
    if (error.response?.status === 401) {
      return;
    }
    //console.log(error.response)
    Notify.create({ message: error.response.statusText, color: 'red' });
    return { data: { error: error.response.data } };
  },
);

export default instance;
