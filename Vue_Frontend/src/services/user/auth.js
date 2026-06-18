import api from "../api";

async function register(payload){
  console.log(payload)
  console.log(import.meta.env.BACKEND_URL)
  try {
    const resp = await api.post("/auth/register", payload);
    return resp.data;

  } catch (error) {
    console.log(error);

    errorMsg = error.response?.data?.detail || "Erro inesperado no servidor.";

    throw new Error(errorMsg);
  }
};

export default register;
