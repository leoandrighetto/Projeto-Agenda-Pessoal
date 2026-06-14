import { defineStore } from "pinia";

const jwlStore = defineStore("jwt-store", {
  state: () => ({
    jwtToken: null,
  }),

  getters: {
    hasToken: (state) => {
      return !!state.jwtToken?.trim();
    }
  },

  actions: {
    saveJwt(newJwt) {
      this.jwt = newJwt;
    },
  },

  killJwt() {
    this.jwt = null;
  },
});

export default jwlStore;
