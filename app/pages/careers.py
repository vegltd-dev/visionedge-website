import reflex as rx
from app.components.navbar import navbar
from app.components.footer import footer


def careers_page() -> rx.Component:
    return rx.el.div(
        rx.el.title("VisionEdge | Careers"),
        navbar(),
        rx.el.main(
            rx.el.h1("Careers", class_name="text-3xl font-bold mb-4"),
            rx.el.p("Join our team and grow with VisionEdge."),
            class_name="container mx-auto px-4 py-16",
        ),
        footer(),
    )