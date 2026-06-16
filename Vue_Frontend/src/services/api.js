import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.BACKEND_URL,
  timeout: 10000,
});

export default api;
