import reflex as rx
from app.states.theme_state import ThemeState
from app.states.hero_state import HeroState


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.foreach(
                HeroState.images,
                lambda item, index: rx.el.div(
                    rx.image(
                        src=item["src"],
                        alt=item["alt"],
                        class_name="w-full h-full object-cover animate-fade-in",
                    ),
                    rx.el.div(
                        class_name="absolute inset-0 bg-gradient-to-b from-black/70 via-black/40 to-black/80"
                    ),
                    class_name=rx.cond(
                        index == HeroState.current_slide,
                        "absolute inset-0 opacity-100 transition-opacity duration-1000 ease-in-out z-10",
                        "absolute inset-0 opacity-0 transition-opacity duration-1000 ease-in-out z-0",
                    ),
                ),
            ),
            class_name="absolute inset-0 w-full h-full overflow-hidden",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Building Dreams,",
                    rx.el.br(),
                    rx.el.span(
                        "Restoring Value",
                        class_name="text-transparent bg-clip-text bg-gradient-to-r from-orange-400 to-orange-600",
                    ),
                    class_name="text-4xl sm:text-6xl md:text-7xl font-black text-white text-center mb-8 drop-shadow-xl leading-tight tracking-tight",
                ),
                rx.el.p(
                    "From precision construction to creative branding, we transform your vision into reality. Experience excellence across every service we provide.",
                    class_name="text-lg sm:text-2xl text-gray-100 text-center mb-12 max-w-3xl drop-shadow-md font-medium leading-relaxed",
                ),
                rx.el.div(
                    rx.el.a(
                        "Explore Services",
                        href="/services",
                        class_name="px-8 py-4 bg-orange-600 hover:bg-orange-700 text-white font-bold rounded-full transition-all transform hover:scale-105 shadow-lg shadow-orange-600/30 border-2 border-orange-600",
                    ),
                    rx.el.a(
                        "View Our Showcase",
                        href="/showcase",
                        class_name="px-8 py-4 bg-white/10 hover:bg-white/20 text-white font-bold rounded-full transition-all transform hover:scale-105 border-2 border-white/80 backdrop-blur-md",
                    ),
                    class_name="flex flex-col sm:flex-row gap-4 sm:gap-6",
                ),
                class_name="relative z-20 flex flex-col items-center justify-center h-full px-4 animate-in fade-in slide-in-from-bottom-8 duration-1000 fill-mode-both",
            ),
            class_name="max-w-7xl mx-auto h-full",
        ),
        rx.el.div(
            rx.foreach(
                rx.Var.range(HeroState.images.length()),
                lambda i: rx.el.button(
                    on_click=lambda: HeroState.set_slide(i),
                    class_name=rx.cond(
                        i == HeroState.current_slide,
                        "w-12 bg-orange-500 h-1.5 rounded-full transition-all duration-300 shadow-lg",
                        "w-3 bg-white/40 hover:bg-white h-1.5 rounded-full transition-all duration-300",
                    ),
                    aria_label="Go to slide",
                ),
            ),
            class_name="absolute bottom-10 left-0 right-0 z-30 flex justify-center space-x-2",
        ),
        class_name="relative h-[800px] w-full bg-slate-900 overflow-hidden",
    )