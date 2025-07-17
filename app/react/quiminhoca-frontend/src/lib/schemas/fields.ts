import { z } from "zod";
import i18n from "@/i18n"
const t = i18n.t;

export const registerEmailField = z.email({ message: t("email.invalid") });
export const loginEmailField = z.email({ message: t("email.invalid") });

export const loginPasswordField = z.string({ message: t("password.string") })
export const registerPasswordField = z
    .string({ message: t("password.string") })
    .min(8, { message: t("password.minLength") })
    .max(20, { message: t("password.maxLength") })
    .refine((val) => /[A-Z]/.test(val), { message: t("password.uppercase") })
    .refine((val) => /[a-z]/.test(val), { message: t("password.lowercase") })
    .refine((val) => /\d/.test(val), { message: t("password.number") })
    .refine((val) => /[!@#$%^&*]/.test(val), { message: t("password.specialChar") });