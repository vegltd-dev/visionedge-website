import reflex as rx
from app.states.theme_state import ThemeState
from typing import TypedDict


class ServiceItem(TypedDict):
    title: str
    description: str
    icon: str
    color_class: str


def service_card(item: ServiceItem) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(item["icon"], class_name="w-8 h-8 text-white"),
            class_name=f"w-14 h-14 rounded-2xl flex items-center justify-center mb-6 {item['color_class']} shadow-lg",
        ),
        rx.el.h3(
            item["title"],
            class_name=rx.cond(
                ThemeState.is_dark,
                "text-xl font-bold text-white mb-3",
                "text-xl font-bold text-slate-900 mb-3",
            ),
        ),
        rx.el.p(
            item["description"],
            class_name=rx.cond(
                ThemeState.is_dark,
                "text-slate-400 leading-relaxed",
                "text-slate-600 leading-relaxed",
            ),
        ),
        rx.el.a(
            "Learn more",
            rx.icon(
                "arrow-right",
                class_name="w-4 h-4 ml-2 transition-transform group-hover:translate-x-1",
            ),
            href="/showcase",
            class_name="inline-flex items-center mt-6 text-orange-600 font-semibold hover:text-orange-700 group",
        ),
        class_name=rx.cond(
            ThemeState.is_dark,
            "p-8 rounded-2xl bg-slate-800 border border-slate-700 hover:border-orange-500/50 transition-all duration-300 hover:shadow-2xl hover:shadow-orange-900/20 h-full flex flex-col",
            "p-8 rounded-2xl bg-white border border-gray-100 hover:border-orange-200 transition-all duration-300 hover:shadow-xl hover:shadow-orange-100/50 h-full flex flex-col",
        ),
    )


def services() -> rx.Component:
    services_list = [
        {
            "title": "Creative Branding",
            "description": "We craft unique brand identities that resonate with your audience. From logos to full design systems.",
            "icon": "palette",
            "color_class": "bg-purple-500",
        },
        {
            "title": "Professional Painting",
            "description": "Interior and exterior painting services that transform spaces with precision, quality, and vibrant colors.",
            "icon": "paint-roller",
            "color_class": "bg-blue-500",
        },
        {
            "title": "Expert Construction",
            "description": "Reliable construction and renovation services. We build solid foundations for your residential and commercial needs.",
            "icon": "hammer",
            "color_class": "bg-orange-500",
        },
        {
            "title": "Auto Repair",
            "description": "Top-tier automotive maintenance and repair. We keep your vehicles running smoothly and safely.",
            "icon": "wrench",
            "color_class": "bg-emerald-500",
        },
    ]
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Comprehensive Services for Every Need",
                    class_name=rx.cond(
                        ThemeState.is_dark,
                        "text-3xl sm:text-5xl font-black text-white mb-6 tracking-tight",
                        "text-3xl sm:text-5xl font-black text-slate-900 mb-6 tracking-tight",
                    ),
                ),
                rx.el.p(
                    "VisionEdge Group combines multiple disciplines under one roof to provide integrated solutions with consistent quality.",
                    class_name=rx.cond(
                        ThemeState.is_dark,
                        "text-lg text-slate-400 max-w-2xl mx-auto",
                        "text-lg text-slate-600 max-w-2xl mx-auto",
                    ),
                ),
                class_name="text-center mb-16 max-w-3xl mx-auto",
            ),
            rx.el.div(
                rx.foreach(services_list, service_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        id="services",
        class_name=rx.cond(
            ThemeState.is_dark, "py-20 sm:py-32 bg-slate-900", "py-20 sm:py-32 bg-white"
        ),
    )