export default function Footer() {
  return (
    <footer className="mt-12 border-t border-gray-300">
      <div className="mx-auto max-w-7xl px-4 py-6 text-center text-sm text-gray-500 dark:text-white">
        © {new Date().getFullYear()} Quiminhoca.
      </div>
    </footer>
  );
}
