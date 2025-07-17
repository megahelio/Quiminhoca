import { z } from "zod";
import { loginEmailField, loginPasswordField, registerEmailField, registerPasswordField } from "./fields";
import i18n from "@/i18n"
const t = i18n.t;

export const loginSchema = z.object({
    email: loginEmailField,
    password: loginPasswordField,
});

export const signUpSchema = z
    .object({
        email: registerEmailField,
        password: registerPasswordField,
        confirmPassword: z.string({ message: t("password.minLength") })
    })
    .refine((data) => data.password === data.confirmPassword, {
        path: ["confirmPassword"],
        message: t("password.passwordsMismatch")
    });

export type LoginFormData = z.infer<typeof loginSchema>;
export type SignUpFormData = z.infer<typeof signUpSchema>;
