import axios from "axios";
console.log(import.meta.env);
const baseURL =
  import.meta.env.MODE !== "production"
    ? "http://localhost:8000"
    : import.meta.env.VITE_API_URL;

export const api = axios.create({ baseURL });

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});
