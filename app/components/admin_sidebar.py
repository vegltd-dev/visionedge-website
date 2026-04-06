import reflex as rx
from app.states.auth_state import AuthState


def sidebar_item(text: str, icon: str, href: str) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="w-5 h-5 mr-3"),
        rx.el.span(text),
        href=href,
        class_name="flex items-center px-4 py-3 text-slate-300 hover:bg-slate-800 hover:text-white rounded-lg transition-colors mb-1",
    )


def admin_sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.icon("layers", class_name="w-8 h-8 text-orange-500 mr-2"),
                rx.el.span(
                    "VisionEdge Admin", class_name="text-xl font-bold text-white"
                ),
                class_name="flex items-center px-4 py-6 border-b border-slate-800 mb-6",
            ),
            rx.el.nav(
                sidebar_item("Dashboard", "layout-dashboard", "/admin/dashboard"),
                sidebar_item("Content CMS", "file-text", "/admin/content"),
                sidebar_item("Settings", "settings", "#"),
                class_name="px-2",
            ),
            class_name="flex-grow",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("log-out", class_name="w-5 h-5 mr-3"),
                rx.el.span("Logout"),
                on_click=AuthState.logout,
                class_name="flex w-full items-center px-6 py-4 text-slate-400 hover:text-white hover:bg-slate-800 transition-colors border-t border-slate-800",
            )
        ),
        class_name="flex flex-col w-64 bg-slate-900 border-r border-slate-800 min-h-screen hidden md:flex sticky top-0 h-screen",
    )