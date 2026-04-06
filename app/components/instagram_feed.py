import reflex as rx
from app.states.theme_state import ThemeState


def insta_item(img_url: str) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.image(
                src=img_url,
                class_name="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110",
                alt="Instagram post",
            ),
            rx.el.div(
                rx.icon(
                    "instagram",
                    class_name="w-8 h-8 text-white opacity-0 group-hover:opacity-100 transition-opacity duration-300 drop-shadow-lg",
                ),
                class_name="absolute inset-0 bg-black/30 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300",
            ),
            class_name="relative w-full aspect-square overflow-hidden rounded-xl",
        ),
        href="#",
        target="_blank",
        class_name="block group cursor-pointer",
    )


def instagram_feed() -> rx.Component:
    images = [

        # 📸 IMAGE POST
        {
            "type": "image",
            "img": "/instagram/post1.jpg",
            "link": "https://www.instagram.com/reel/DVWpPSqiPER/",
        },

        # 🎬 REEL
        {
            "type": "reel",
            "img": "/instagram/reel1.jpg",  # thumbnail image
            "link": "https://www.instagram.com/reel/DVWpPSqiPER/"
        },
        # More examples
        {
            "type": "image",
            "img": "/instagram/post2.jpg",
            "link": "https://www.instagram.com/p/XXXXX/",
        },
        {
            "type": "reel",
            "img": "/instagram/reel2.jpg",
            "link": "https://www.instagram.com/reel/YYYYY/",
        },
        "https://www.instagram.com/visionedgegroupltd/reel/DVBvEKnCBLV/",
        "https://www.instagram.com/p/DVWpPSqiPER/",
        "https://picsum.photos/id/103/400/400",
        "https://picsum.photos/id/104/400/400",
        "https://picsum.photos/id/106/400/400",
        "https://picsum.photos/id/108/400/400",
    ]
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("instagram", class_name="w-6 h-6 text-orange-600 mr-2"),
                    rx.el.h2(
                        "Follow Us on Instagram",
                        class_name=rx.cond(
                            ThemeState.is_dark,
                            "text-2xl font-bold text-white",
                            "text-2xl font-bold text-slate-900",
                        ),
                    ),
                    class_name="flex items-center justify-center mb-3",
                ),
                rx.el.p(
                    "@VisionEdgeGroup",
                    class_name="text-orange-600 font-medium text-center mb-10",
                ),
                class_name="text-center",
            ),
            rx.el.div(
                rx.foreach(images, insta_item),
                class_name="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4 auto-rows-fr",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full",
        ),
        class_name=rx.cond(
            ThemeState.is_dark,
            "py-20 bg-slate-900 border-t border-slate-800",
            "py-20 bg-slate-50 border-t border-gray-100",
        ),
    )