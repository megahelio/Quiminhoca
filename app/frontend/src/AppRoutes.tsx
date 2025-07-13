// src/routes.jsx
import { Routes, Route } from "react-router-dom"
import Search from "./pages/Search"

export default function AppRoutes() {
    return (
        <Routes>
            <Route path="/" element={<Search />} />
        </Routes>
    )
}
