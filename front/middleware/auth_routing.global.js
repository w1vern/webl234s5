export default defineNuxtRouteMiddleware(async (to, from) => {
    const authStore = useAuthStore()
    await authStore.fetch_session()
    if (to.meta?.need_not_auth && authStore.isAuth){
        return navigateTo("/")
    }
    if (to.meta?.need_auth && !authStore.isAuth){
        return navigateTo("/auth/login")
    }
})