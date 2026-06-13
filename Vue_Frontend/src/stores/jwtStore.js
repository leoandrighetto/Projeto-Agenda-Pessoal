import { defineStore } from "pinia";

const jwlStore = defineStore("jwt-store", {
  state: () => ({
    jwtToken: "teste",
  }),

  getters: () => {
    hasToken: (state) => !!state.jwtToken;
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
