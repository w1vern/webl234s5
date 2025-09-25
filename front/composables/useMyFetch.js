export const useMyFetch = (request, opts = {}) => {
  const config = useRuntimeConfig()

  return useFetch(request, { ...opts, server: false })
}
