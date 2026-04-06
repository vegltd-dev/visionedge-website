import reflex as rx


def sticky_buttons() -> rx.Component:
    return rx.el.div(
        rx.el.a(
            rx.icon("message-square-quote", class_name="w-6 h-6 text-white"),
            href="/quote",
            class_name="bg-orange-600 p-3 rounded-full shadow-lg hover:scale-110 transition-transform hover:bg-orange-700 mb-4 flex items-center justify-center group",
            title="Request a Quote",
        ),
        rx.el.a(
            rx.icon("phone", class_name="w-6 h-6 text-white"),
            href="https://wa.me/0787463120",
            target="_blank",
            rel="noopener noreferrer",
            class_name="bg-green-500 p-3 rounded-full shadow-lg hover:scale-110 transition-transform hover:bg-green-600 flex items-center justify-center",
            title="Chat on WhatsApp",
        ),
        class_name=rx.cond(
            rx.State.router.page.path == "/quote",
            "hidden",
            "fixed bottom-6 right-6 z-[9999] flex flex-col items-center animate-in fade-in slide-in-from-bottom-4 duration-1000",
        ),
    )