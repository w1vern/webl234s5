export const useAuthStore = defineStore("authStore", {
  state: () => ({
    isAuth: false,
    phone: "",
  }),
  actions: {
    async fetch_session() {
      const { data } = await useMyFetch("/api/auth/session");
      if (data.value) {
        this.isAuth = data.value.is_auth;
        this.phone = data.value.phone;
      } else {
        this.isAuth = false;
        this.phone = "";
      }
    },
    async login(phone, password, remember_me) {
      const { data, status, error } = await useMyFetch("/api/auth/login", {
        method: "post",
        body: {
          phone: phone,
          password: password,
        },
      });
      await this.fetch_session();
      if (status.value == "error")
        return {
          status: error.value.statusCode,
          data: error.value.data?.detail,
        };
      return {
        status: 200,
        data: data.value,
      };
    },
    async registration(phone, password, password1) {
      const { data, status, error } = await useMyFetch(
        "/api/auth/register",
        {
          method: "post",
          body: {
            phone: phone,
            password: password,
            password_repeat: password1,
          },
        }
      );
      await this.fetch_session();
      if (status.value == "error")
        return {
          status: error.value.statusCode,
          data: error.value.data?.detail,
        };
      return {
        status: 200,
        data: data.value,
      };
    },
    async logout() {
      const { data, status, error } = await useMyFetch("/api/auth/logout", {
        method: "post",
      });
      await this.fetch_session();
    },
  },
});
