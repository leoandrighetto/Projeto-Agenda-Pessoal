import api from "../api";

const register = async () => {
  try {
    const resp = await api.post("/auth/register", payload);
    return resp.data;
  } catch (error) {
    console.error(error);
    
    errorMsg = error.response?.data?.detail || "Erro inesperado no servidor."

    throw new Error(errorMsg);
  }
};

