export const useMyFetch = (request, opts = {}) => {
  const config = useRuntimeConfig()
  const base = config.public?.apiBase || 'http://localhost:80'

  return useFetch(request, { baseURL: base, ...opts, server: false })
}
