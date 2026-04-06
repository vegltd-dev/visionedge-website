import reflex as rx
from app.components.navbar import navbar
from app.components.footer import footer
from app.components.sticky_buttons import sticky_buttons
from app.components.Slide1_Slide2 import Slide1_Slide2_card
from app.states.theme_state import ThemeState
from app.states.showcase_state import ShowcaseState


def category_filter_button(category: str) -> rx.Component:
    return rx.el.button(
        category,
        on_click=lambda: ShowcaseState.set_category(category),
        class_name=rx.cond(
            ShowcaseState.selected_category == category,
            "px-4 py-2 rounded-full text-sm font-medium bg-orange-600 text-white shadow-lg shadow-orange-500/30 transition-all",
            rx.cond(
                ThemeState.is_dark,
                "px-4 py-2 rounded-full text-sm font-medium bg-slate-800 text-slate-300 hover:bg-slate-700 transition-all",
                "px-4 py-2 rounded-full text-sm font-medium bg-white text-slate-600 hover:bg-gray-50 border border-gray-200 transition-all",
            ),
        ),
    )


def lightbox() -> rx.Component:
    return rx.cond(
        ShowcaseState.is_lightbox_open,
        rx.el.div(
            rx.el.div(
                rx.el.button(
                    rx.icon("x", class_name="w-8 h-8 text-white"),
                    on_click=ShowcaseState.close_lightbox,
                    class_name="absolute top-4 right-4 z-50 p-2 bg-black/50 hover:bg-black/70 rounded-full transition-colors",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "Slide2",
                            class_name="text-white text-center font-bold mb-2 text-xl",
                        ),
                        rx.image(
                            src=ShowcaseState.selected_image["Slide2"],
                            class_name="max-h-[70vh] w-auto object-contain rounded-lg shadow-2xl",
                        ),
                        class_name="flex flex-col",
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "Slide2",
                            class_name="text-white text-center font-bold mb-2 text-xl",
                        ),
                        rx.image(
                            src=ShowcaseState.selected_image["Slide1"],
                            class_name="max-h-[70vh] w-auto object-contain rounded-lg shadow-2xl",
                        ),
                        class_name="flex flex-col",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 gap-8 p-4 w-full max-w-7xl",
                ),
                class_name="relative w-full h-full flex items-center justify-center",
            ),
            class_name="fixed inset-0 z-[10000] bg-black/90 backdrop-blur-md animate-in fade-in duration-200",
            on_click=ShowcaseState.close_lightbox,
        ),
    )


def showcase_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        lightbox(),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "Our Portfolio",
                        class_name=rx.cond(
                            ThemeState.is_dark,
                            "text-3xl sm:text-5xl font-extrabold text-white mb-6",
                            "text-3xl sm:text-5xl font-extrabold text-slate-900 mb-6",
                        ),
                    ),
                    rx.el.p(
                        "Witness the transformation. Hover over our project cards to see the Slide2 & Slide1 results of our expert craftsmanship.",
                        class_name=rx.cond(
                            ThemeState.is_dark,
                            "text-lg text-slate-400 max-w-2xl mx-auto",
                            "text-lg text-slate-600 max-w-2xl mx-auto",
                        ),
                    ),
                    class_name="text-center py-12",
                ),
                rx.el.div(
                    rx.foreach(ShowcaseState.categories, category_filter_button),
                    class_name="flex flex-wrap justify-center gap-3 mb-12",
                ),
                rx.el.div(
                    rx.foreach(ShowcaseState.filtered_items, Slide1_Slide2_card),
                    class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8",
                ),

                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-20",
            ),
            class_name="flex-grow",
        ),
        footer(),
        sticky_buttons(),
        class_name=rx.cond(
            ThemeState.is_dark,
            "min-h-screen flex flex-col bg-slate-900 font-['Lato'] transition-colors duration-300",
            "min-h-screen flex flex-col bg-slate-50 font-['Lato'] transition-colors duration-300",
        ),
    )