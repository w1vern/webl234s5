export default defineNuxtRouteMiddleware((to, from) => {
    const authStore = useAuthStore()
    if (to.meta?.need_not_auth && authStore.isAuth){
        return navigateTo("/")
    }
})