import Header from "../components/header-footer/Header";
import Footer from "../components/header-footer/Footer";
import { ThemeProvider } from "../lib/services/theme-provider";
import { Outlet } from "react-router-dom";

function AppLayout() {
  return (
    <div className="flex min-h-screen flex-col">
      <ThemeProvider defaultTheme="light" storageKey="vite-ui-theme">
        <Header />
        <main className="flex flex-grow flex-col items-center justify-center px-4 py-8">
          <Outlet />
        </main>
        <Footer />
      </ThemeProvider>
    </div>
  );
}

export default AppLayout;
