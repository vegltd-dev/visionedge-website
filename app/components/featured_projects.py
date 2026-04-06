import reflex as rx
from app.states.theme_state import ThemeState


def project_card(img: str, title: str, category: str) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.image(
                src=img,
                class_name="w-full h-72 object-cover transition-transform duration-700 group-hover:scale-110",
            ),
            rx.el.div(
                class_name="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent opacity-80"
            ),
            rx.el.div(
                rx.el.span(
                    category,
                    class_name="text-orange-500 font-bold text-xs uppercase tracking-wider mb-2 block",
                ),
                rx.el.h3(
                    title, class_name="text-white font-bold text-xl mb-1 leading-tight"
                ),
                rx.el.div(
                    "View Project",
                    rx.icon(
                        "arrow-right",
                        class_name="w-4 h-4 ml-2 transition-transform group-hover:translate-x-1",
                    ),
                    class_name="inline-flex items-center text-sm text-gray-300 mt-4 opacity-0 group-hover:opacity-100 transform translate-y-2 group-hover:translate-y-0 transition-all duration-300",
                ),
                class_name="absolute bottom-0 left-0 right-0 p-6 transform translate-y-2 group-hover:translate-y-0 transition-transform duration-300",
            ),
            class_name="relative overflow-hidden rounded-2xl shadow-lg h-full group",
        ),
        href="/showcase",
        class_name="block transform transition-all duration-300 hover:-translate-y-2",
    )


def featured_projects() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Featured Projects",
                        class_name=rx.cond(
                            ThemeState.is_dark,
                            "text-3xl sm:text-4xl font-extrabold text-white mb-4",
                            "text-3xl sm:text-4xl font-extrabold text-slate-900 mb-4",
                        ),
                    ),
                    rx.el.p(
                        "A glimpse into our recent masterpieces. We take pride in every detail.",
                        class_name=rx.cond(
                            ThemeState.is_dark,
                            "text-lg text-slate-400",
                            "text-lg text-slate-600",
                        ),
                    ),
                    class_name="mb-8 md:mb-0",
                ),
                rx.el.a(
                    "View Full Portfolio",
                    rx.icon("arrow-right", class_name="w-4 h-4 ml-2"),
                    href="/showcase",
                    class_name="inline-flex items-center font-bold text-orange-600 hover:text-orange-700 transition-colors px-4 py-2 rounded-full bg-orange-50 hover:bg-orange-100",
                ),
                class_name="flex flex-col md:flex-row justify-between items-end md:items-center mb-12",
            ),
            rx.el.div(
                project_card(
                    "/photos/plascon1.jpeg",
                    "Plascon Outdoor wall-branding",
                    "Branding",
                ),
                project_card(
                    "/photos/skol1.jpeg",
                    "Skol Brewery Limited Outlet branding upcountry",
                    "Branding",
                ),
                project_card(
                    "/photos/airtel.jpeg",
                    "Airtel's car Branding",
                    "Car Repair and Branding",
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-8",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        class_name=rx.cond(
            ThemeState.is_dark, "py-24 bg-slate-900", "py-24 bg-slate-50"
        ),
    )