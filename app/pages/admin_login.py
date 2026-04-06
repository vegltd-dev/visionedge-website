import reflex as rx
from app.states.auth_state import AuthState


def admin_login() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("layers", class_name="w-12 h-12 text-orange-600 mx-auto mb-4"),
                rx.el.h1(
                    "Admin Access",
                    class_name="text-2xl font-bold text-slate-900 text-center mb-8",
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.label(
                            "Username",
                            class_name="block text-sm font-medium text-slate-700 mb-2",
                        ),
                        rx.el.input(
                            name="username",
                            placeholder="admin",
                            class_name="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-orange-500 focus:border-transparent outline-none",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Password",
                            class_name="block text-sm font-medium text-slate-700 mb-2",
                        ),
                        rx.el.input(
                            name="password",
                            type="password",
                            placeholder="••••••••",
                            class_name="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-orange-500 focus:border-transparent outline-none",
                        ),
                        class_name="mb-6",
                    ),
                    rx.cond(
                        AuthState.error_message != "",
                        rx.el.div(
                            AuthState.error_message,
                            class_name="mb-4 p-3 rounded bg-red-50 text-red-600 text-sm",
                        ),
                    ),
                    rx.el.button(
                        "Sign In",
                        type="submit",
                        class_name="w-full py-3 bg-orange-600 hover:bg-orange-700 text-white font-bold rounded-lg transition-colors shadow-lg",
                    ),
                    on_submit=AuthState.login,
                ),
                class_name="bg-white p-8 rounded-2xl shadow-xl border border-gray-100 w-full max-w-md",
            ),
            class_name="flex items-center justify-center min-h-screen px-4",
        ),
        class_name="min-h-screen bg-slate-50",
    )