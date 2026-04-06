import reflex as rx
from app.components.navbar import navbar
from app.components.footer import footer


def privacy_page() -> rx.Component:
    return rx.el.div(
        rx.el.title("VisionEdge | Privacy Policy"),
        navbar(),
        rx.el.main(
            rx.el.h1("Privacy Policy", class_name="text-3xl font-bold mb-4"),
            rx.el.p("We respect your privacy and protect your data."),
            class_name="container mx-auto px-4 py-16",
        ),
        footer(),
    )