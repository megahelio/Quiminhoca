import {
  createBrowserRouter,
  redirect,
  RouterProvider,
} from "react-router-dom";

import AppLayout from "./layout/AppLayout";
import Search from "./pages/Search";
import Login from "./pages/Login";
import SignUp from "./pages/Sign-up";
import Terms from "./pages/Terms";
import Privacy from "./pages/Privacy";
import Dashboard from "./pages/Dashboard";
import Error from "./pages/Error";

function authLoader() {
  const token = localStorage.getItem("token");
  if (!token) {
    throw redirect("/login");
  }
  return null;
}
console.log(import.meta.env.VITE_FRONTEND_BASE_URL);
const router = createBrowserRouter(
  [
    {
      path: "/",
      element: <AppLayout />,
      errorElement: <Error />,
      children: [
        { index: true, element: <Search /> },
        { path: "login", element: <Login /> },
        { path: "signup", element: <SignUp /> },
        { path: "terms", element: <Terms /> },
        { path: "privacy", element: <Privacy /> },
        {
          path: "dashboard",
          element: <Dashboard />,
          loader: authLoader,
        },
      ],
    },
  ],
  {
    basename: import.meta.env.VITE_FRONTEND_BASE_URL,
  },
);

export default function AppRoutes() {
  return <RouterProvider router={router} />;
}
