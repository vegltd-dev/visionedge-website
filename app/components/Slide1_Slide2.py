import reflex as rx
from app.states.showcase_state import ShowcaseState


def Slide1_Slide2_card(item: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=item["Slide1"],
                alt=f"Slide1: {item['title']}",
                class_name="w-full h-64 object-cover",
            ),
            rx.el.div(
                rx.el.span("Slide1", class_name="text-xs font-bold tracking-wider"),
                class_name="absolute bottom-3 right-3 bg-black/60 text-white px-2 py-1 rounded backdrop-blur-sm z-10 transition-opacity duration-300 group-hover:opacity-0",
            ),
            rx.el.div(
                rx.image(
                    src=item["Slide2"],
                    alt=f"Slide2: {item['title']}",
                    class_name="w-full h-64 object-cover",
                ),
                rx.el.div(
                    rx.el.span("Slide2", class_name="text-xs font-bold tracking-wider"),
                    class_name="absolute bottom-3 left-3 bg-orange-600/80 text-white px-2 py-1 rounded backdrop-blur-sm",
                ),
                class_name="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 ease-in-out",
            ),
            class_name="relative overflow-hidden rounded-t-xl cursor-pointer",
            on_click=lambda: ShowcaseState.open_lightbox(item),
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    item["category"],
                    class_name="text-xs font-semibold text-orange-600 uppercase tracking-wider mb-1 block",
                ),
                rx.el.h3(
                    item["title"],
                    class_name="text-lg font-bold text-slate-900 mb-2 line-clamp-1",
                ),
                rx.el.p(
                    item["description"],
                    class_name="text-sm text-slate-500 line-clamp-2",
                ),
            ),
            class_name="p-5 bg-white border-x border-b border-gray-100 rounded-b-xl",
        ),
        class_name="group hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1 bg-white rounded-xl",
    )