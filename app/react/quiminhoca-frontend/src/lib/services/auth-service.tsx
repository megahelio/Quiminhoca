import { api } from "./api";

export async function login(email: string, password: string) {
  const res = await api.post("/login", { email, password });
  localStorage.setItem("token", res.data.access_token);
  return res.data;
}

export async function register(email: string, password: string) {
  const res = await api.post("/register", { email, password });
  localStorage.setItem("token", res.data.access_token);
  return res.data;
}
