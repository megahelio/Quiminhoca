import Header from "./components/Header";
import Footer from "./components/Footer";
import AppRoutes from "./AppRoutes";
import { ThemeProvider } from "./components/theme-provider";

function App() {
  return (
    <div className="flex min-h-screen flex-col">
      <ThemeProvider defaultTheme="light" storageKey="vite-ui-theme">
        <Header />
        <main className="flex-grow px-4 py-8">
          <AppRoutes />
        </main>
        <Footer />
      </ThemeProvider>
    </div>
  );
}

export default App;
