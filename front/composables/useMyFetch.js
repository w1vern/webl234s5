export const useMyFetch = (request, opts) => {
    const config = useRuntimeConfig()
  
    return useFetch(request, { baseURL: 'http://localhost:8081', ...opts, server: false })
  }
 