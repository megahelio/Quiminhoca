import Header from "./components/header-footer/Header";
import Footer from "./components/header-footer/Footer";
import AppRoutes from "./AppRoutes";
import { ThemeProvider } from "./lib/services/theme-provider";

function App() {
  return (
    <div className="flex min-h-screen flex-col">
      <ThemeProvider defaultTheme="light" storageKey="vite-ui-theme">
        <Header />
        <main className="flex flex-grow flex-col items-center justify-center px-4 py-8">
          <AppRoutes />
        </main>
        <Footer />
      </ThemeProvider>
    </div>
  );
}

export default App;
