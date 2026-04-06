import reflex as rx
from app.components.navbar import navbar
from app.components.footer import footer


def terms_page() -> rx.Component:
    return rx.el.div(
        rx.el.title("VisionEdge | Terms of Service"),
        navbar(),
        rx.el.main(
            rx.el.h1("Terms of Service", class_name="text-3xl font-bold mb-4"),
            rx.el.p("By using our services, you agree to our terms."),
            class_name="container mx-auto px-4 py-16",
        ),
        footer(),
    )