import path from "path"
import tailwindcss from "@tailwindcss/vite"
import react from "@vitejs/plugin-react"
import { defineConfig } from "vite"

const baseUrl = process.env.VITE_FRONTEND_BASE_URL;

export default defineConfig({
  base: baseUrl,
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  // Solo se usa en DEV no hace falta verificar ENV_MODE
  server: {
    proxy: {
      '/api': 'http://localhost:8000',
    }
  }
})