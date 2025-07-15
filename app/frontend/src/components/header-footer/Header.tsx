import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { ModeToggle } from "./mode-toggle";
export default function Header() {
  return (
    <header className="shadow-md">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-4">
        <h1 className="text-4xl font-bold">Quiminhoca</h1>
        <nav className="flex gap-4 px-4 py-3">
          <Link to="/">
            <Button variant="ghost">Inicio</Button>
          </Link>
          <Link to="/login">
            <Button variant="ghost">Login</Button>
          </Link>
          <ModeToggle></ModeToggle>
        </nav>
      </div>
    </header>
  );
}
