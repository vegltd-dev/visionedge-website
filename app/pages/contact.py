import reflex as rx
from app.components.navbar import navbar
from app.components.footer import footer
from app.components.sticky_buttons import sticky_buttons


def contact_page() -> rx.Component:
    return rx.el.div(
        rx.el.title("VisionEdge Group Ltd | Contact"),
        navbar(),
        rx.el.main(
            rx.el.h1("Contact Us", class_name="text-3xl font-bold mb-4"),
            rx.el.p("Email: visionedgegrp@gmail.com"),
            rx.el.p("Phone: +250 787 463 120"),
            class_name="container mx-auto px-4 py-16 flex-grow",
        ),
        footer(),
        sticky_buttons(),
    )