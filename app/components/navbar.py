import reflex as rx
from app.states.theme_state import ThemeState
from app.states.nav_state import NavState


def nav_link(text: str, href: str = "#") -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        class_name=rx.cond(
            ThemeState.is_dark,
            "text-slate-300 hover:text-orange-500 transition-colors font-medium",
            "text-slate-600 hover:text-orange-600 transition-colors font-medium",
        ),
    )


def mobile_nav_link(text: str, href: str = "#") -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        on_click=NavState.close_mobile_menu,
        class_name=rx.cond(
            ThemeState.is_dark,
            "block px-3 py-2 rounded-md text-base font-medium text-slate-300 hover:text-white hover:bg-slate-700",
            "block px-3 py-2 rounded-md text-base font-medium text-slate-700 hover:text-orange-600 hover:bg-orange-50",
        ),
    )


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.image(src="/logo.jpg",class_name="h-10 w-10 rounded-full object-cover"),
                        rx.el.span(
                            "VisionEdge",
                            class_name=rx.cond(
                                ThemeState.is_dark,
                                "ml-2 text-xl font-bold text-white tracking-tight",
                                "ml-2 text-xl font-bold text-slate-900 tracking-tight",
                            ),
                        ),
                        class_name="flex-shrink-0 flex items-center cursor-pointer",
                    ),
                    rx.el.div(
                        rx.el.div(
                            nav_link("Home", "#"),
                            nav_link("Services", "/#services"),
                            nav_link("Showcase", "/showcase"),
                            nav_link("About", "/about"),
                            nav_link("Contact", "/#contact"),
                            class_name="ml-10 flex items-baseline space-x-8",
                        ),
                        class_name="hidden md:block",
                    ),
                    class_name="flex items-center",
                ),
                rx.el.div(
                    rx.el.button(
                        rx.icon(ThemeState.theme_icon, class_name="h-5 w-5"),
                        on_click=ThemeState.toggle_theme,
                        class_name=rx.cond(
                            ThemeState.is_dark,
                            "p-2 rounded-full text-slate-400 hover:text-white hover:bg-slate-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-slate-800 focus:ring-white transition-all",
                            "p-2 rounded-full text-slate-500 hover:text-slate-900 hover:bg-slate-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500 transition-all",
                        ),
                    ),
                    rx.el.a(
                        "Get Quote",
                        href="/quote",
                        class_name="ml-4 hidden md:inline-flex items-center justify-center px-4 py-2 border border-transparent rounded-lg shadow-sm text-sm font-medium text-white bg-orange-600 hover:bg-orange-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500 transition-colors",
                    ),
                    rx.el.div(
                        rx.el.button(
                            rx.cond(
                                NavState.is_mobile_menu_open,
                                rx.icon("x", class_name="block h-6 w-6"),
                                rx.icon("menu", class_name="block h-6 w-6"),
                            ),
                            on_click=NavState.toggle_mobile_menu,
                            class_name=rx.cond(
                                ThemeState.is_dark,
                                "inline-flex items-center justify-center p-2 rounded-md text-slate-400 hover:text-white hover:bg-slate-700 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white",
                                "inline-flex items-center justify-center p-2 rounded-md text-slate-700 hover:text-orange-600 hover:bg-orange-50 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-orange-500",
                            ),
                        ),
                        class_name="-mr-2 flex md:hidden ml-4",
                    ),
                    class_name="flex items-center",
                ),
                class_name="flex items-center justify-between h-16",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        rx.cond(
            NavState.is_mobile_menu_open,
            rx.el.div(
                rx.el.div(
                    mobile_nav_link("Home", "/"),
                    mobile_nav_link("Services", "/#services"),
                    mobile_nav_link("Showcase", "/showcase"),
                    mobile_nav_link("About", "/#about"),
                    mobile_nav_link("Contact", "/#contact"),
                    rx.el.a(
                        "Get a Quote",
                        href="#quote",
                        class_name="block w-full text-center mt-4 px-4 py-3 rounded-lg font-medium text-white bg-orange-600 hover:bg-orange-700 transition-colors",
                    ),
                    class_name="px-2 pt-2 pb-3 space-y-1 sm:px-3",
                ),
                class_name=rx.cond(
                    ThemeState.is_dark,
                    "md:hidden bg-slate-800 border-t border-slate-700",
                    "md:hidden bg-white border-t border-gray-100",
                ),
            ),
        ),
        class_name=rx.cond(
            ThemeState.is_dark,
            "bg-slate-900/95 backdrop-blur-md border-b border-slate-800 sticky top-0 z-50",
            "bg-white/95 backdrop-blur-md border-b border-gray-100 sticky top-0 z-50",
        ),
    )