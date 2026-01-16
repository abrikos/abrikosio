import {useCustomStore} from '~/store/custom-store';
//import {storeToRefs} from "pinia"; // import the auth store we just created
export default defineNuxtRouteMiddleware(async (to, from) => {
    const {getUser, setRedirect, redirect} = useCustomStore();
    const loggedUser = await getUser()
});