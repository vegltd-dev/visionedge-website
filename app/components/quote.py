import reflex as rx
from app.components.navbar import navbar
from app.components.footer import footer
from app.components.sticky_buttons import sticky_buttons
from app.states.theme_state import ThemeState
from app.states.quote_state import QuoteState


def form_input(
    label: str, name: str, type: str = "text", placeholder: str = ""
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            class_name=rx.cond(
                ThemeState.is_dark,
                "block text-sm font-medium text-slate-300 mb-2",
                "block text-sm font-medium text-slate-700 mb-2",
            ),
        ),
        rx.el.input(
            name=name,
            type=type,
            placeholder=placeholder,
            required=True,
            class_name=rx.cond(
                ThemeState.is_dark,
                "w-full px-4 py-3 rounded-xl bg-slate-800 border border-slate-600 text-white placeholder-slate-500 focus:ring-2 focus:ring-orange-500 focus:border-transparent outline-none transition-all",
                "w-full px-4 py-3 rounded-xl bg-gray-50 border border-gray-200 text-slate-900 placeholder-slate-400 focus:ring-2 focus:ring-orange-500 focus:border-transparent outline-none transition-all",
            ),
        ),
        class_name="mb-6",
    )


def form_select(label: str, name: str, options: list[str]) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            class_name=rx.cond(
                ThemeState.is_dark,
                "block text-sm font-medium text-slate-300 mb-2",
                "block text-sm font-medium text-slate-700 mb-2",
            ),
        ),
        rx.el.div(
            rx.el.select(
                rx.foreach(options, lambda x: rx.el.option(x, value=x)),
                name=name,
                class_name=rx.cond(
                    ThemeState.is_dark,
                    "w-full px-4 py-3 rounded-xl bg-slate-800 border border-slate-600 text-white focus:ring-2 focus:ring-orange-500 focus:border-transparent outline-none transition-all appearance-none",
                    "w-full px-4 py-3 rounded-xl bg-gray-50 border border-gray-200 text-slate-900 focus:ring-2 focus:ring-orange-500 focus:border-transparent outline-none transition-all appearance-none",
                ),
            ),
            rx.icon(
                "chevron-down",
                class_name="absolute right-4 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-500 pointer-events-none",
            ),
            class_name="relative",
        ),
        class_name="mb-6",
    )


def form_textarea(label: str, name: str, placeholder: str = "") -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            class_name=rx.cond(
                ThemeState.is_dark,
                "block text-sm font-medium text-slate-300 mb-2",
                "block text-sm font-medium text-slate-700 mb-2",
            ),
        ),
        rx.el.textarea(
            name=name,
            placeholder=placeholder,
            rows=5,
            required=True,
            class_name=rx.cond(
                ThemeState.is_dark,
                "w-full px-4 py-3 rounded-xl bg-slate-800 border border-slate-600 text-white placeholder-slate-500 focus:ring-2 focus:ring-orange-500 focus:border-transparent outline-none transition-all resize-y",
                "w-full px-4 py-3 rounded-xl bg-gray-50 border border-gray-200 text-slate-900 placeholder-slate-400 focus:ring-2 focus:ring-orange-500 focus:border-transparent outline-none transition-all resize-y",
            ),
        ),
        class_name="mb-6",
    )


def quote_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h1(
                            "Request a Quote",
                            class_name=rx.cond(
                                ThemeState.is_dark,
                                "text-3xl sm:text-4xl font-bold text-white mb-4",
                                "text-3xl sm:text-4xl font-bold text-slate-900 mb-4",
                            ),
                        ),
                        rx.el.p(
                            "Tell us about your project and we'll get back to you with a customized proposal within 24 hours.",
                            class_name=rx.cond(
                                ThemeState.is_dark,
                                "text-lg text-slate-400",
                                "text-lg text-slate-600",
                            ),
                        ),
                        class_name="text-center max-w-2xl mx-auto mb-12",
                    ),
                    rx.el.div(
                        rx.el.form(
                            rx.el.div(
                                rx.el.div(
                                    form_input(
                                        "Full Name", "name", placeholder="John Doe"
                                    ),
                                    form_input(
                                        "Email Address",
                                        "email",
                                        type="email",
                                        placeholder="visionedgegrp@gmail.com",
                                    ),
                                    class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
                                ),
                                rx.el.div(
                                    form_input(
                                        "Phone Number",
                                        "phone",
                                        type="tel",
                                        placeholder="+1 (555) 000-0000",
                                    ),
                                    form_select(
                                        "Service Interest",
                                        "service",
                                        [
                                            "Branding & Design",
                                            "Interior Painting",
                                            "Construction",
                                            "Car Repair",
                                            "Other",
                                        ],
                                    ),
                                    class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
                                ),
                                form_textarea(
                                    "Project Details",
                                    "message",
                                    placeholder="Please describe your project requirements, timeline, and any specific questions you have...",
                                ),
                                rx.el.button(
                                    rx.cond(
                                        QuoteState.is_loading,
                                        rx.el.div(
                                            rx.spinner(
                                                size="2", class_name="text-white mr-2"
                                            ),
                                            "Sending...",
                                            class_name="flex items-center",
                                        ),
                                        rx.el.span("Submit Request"),
                                    ),
                                    type="submit",
                                    disabled=QuoteState.is_loading,
                                    class_name="w-full md:w-auto px-8 py-4 bg-orange-600 hover:bg-orange-700 text-white font-bold "
                                               "rounded-xl transition-all shadow-lg shadow-orange-500/20 hover:shadow-orange-500/40 "
                                               "disabled:opacity-70 disabled:cursor-not-allowed flex justify-center items-center",
                                ),
                            ),
                            on_submit=QuoteState.handle_submit,
                            reset_on_submit=True,
                        ),
                        class_name=rx.cond(
                            ThemeState.is_dark,
                            "bg-slate-900 p-8 sm:p-10 rounded-3xl shadow-xl border border-slate-800",
                            "bg-white p-8 sm:p-10 rounded-3xl shadow-xl border border-gray-100",
                        ),
                    ),
                    class_name="max-w-4xl mx-auto",
                ),
                class_name="container mx-auto px-4 py-16 sm:py-24",
            ),
            class_name="flex-grow",
        ),
        footer(),
        sticky_buttons(),
        class_name=rx.cond(
            ThemeState.is_dark,
            "min-h-screen flex flex-col bg-slate-950 font-['Lato'] transition-colors duration-300",
            "min-h-screen flex flex-col bg-slate-50 font-['Lato'] transition-colors duration-300",
        ),
    )