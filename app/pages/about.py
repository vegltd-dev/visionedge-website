import reflex as rx
from app.components.navbar import navbar
from app.components.footer import footer
from app.components.sticky_buttons import sticky_buttons


def about_page() -> rx.Component:
    return rx.el.div(
        rx.el.title("VisionEdge | About"),
        navbar(),
        rx.el.main(
            rx.el.h1("About Us", class_name="text-3xl font-bold mb-4"),
            rx.el.p(
                "VisionEdge Group Ltd is a multi-service company specializing in branding, painting, construction, and car repair.",
                class_name="text-lg"
            ),
            class_name="container mx-auto px-4 py-16 flex-grow",
        ),
        footer(),
        sticky_buttons(),
    )