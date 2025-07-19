import React from "react";
import ReactDOM from "react-dom/client";
import { I18nextProvider } from "react-i18next";
import "./index.css";
import i18n from "@/i18n";
import AppRoutes from "./routes";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <I18nextProvider i18n={i18n}>
      <AppRoutes />
    </I18nextProvider>
  </React.StrictMode>,
);
