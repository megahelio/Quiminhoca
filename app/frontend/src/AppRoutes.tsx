// src/routes.jsx
import { Routes, Route } from "react-router-dom";
import Search from "./pages/Search";
import Login from "./pages/Login";
import Terms from "./pages/Terms";
import Privacy from "./pages/Privacy";
import SignUp from "./pages/Sing-up";
import Error from "./pages/Error";

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Search />} />

      <Route path="/login" element={<Login />} />
      <Route path="/signup" element={<SignUp />} />

      <Route path="/terms" element={<Terms />} />
      <Route path="/privacy" element={<Privacy />} />
      <Route path="*" element={<Error />} />
    </Routes>
  );
}
