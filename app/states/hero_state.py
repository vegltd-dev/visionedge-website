import reflex as rx
import asyncio


class HeroState(rx.State):
    current_slide: int = 0
    images: list[dict[str, str]] = [
        {
            "src": "https://images.unsplash.com/photo-1541888946425-d81bb19240f5?auto=format&fit=crop&w=1600&q=80",
            "alt": "Construction site with crane",
            "title": "Expert Construction",
        },
        {
            "src": "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?auto=format&fit=crop&w=1600&q=80",
            "alt": "Creative branding team meeting",
            "title": "Strategic Branding",
        },
        {
            "src": "https://images.unsplash.com/photo-1562259949-e8e7689d7828?auto=format&fit=crop&w=1600&q=80",
            "alt": "Professional painting service",
            "title": "Precision Painting",
        },
        {
            "src": "https://images.unsplash.com/photo-1486006920555-c77dcf18193c?auto=format&fit=crop&w=1600&q=80",
            "alt": "Car mechanic repairing vehicle",
            "title": "Automotive Care",
        },
        {
            "src": "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=1600&q=80",
            "alt": "Modern architecture design",
            "title": "Architectural Design",
        },
        {
            "src": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=1600&q=80",
            "alt": "Digital marketing strategy",
            "title": "Digital Marketing",
        },
        {
            "src": "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?auto=format&fit=crop&w=1600&q=80",
            "alt": "Detailed construction blueprint",
            "title": "Detailed Planning",
        },
        {
            "src": "https://images.unsplash.com/photo-1487754180451-c456f719a1fc?auto=format&fit=crop&w=1600&q=80",
            "alt": "Auto detailing service",
            "title": "Premium Detailing",
        },
    ]
    _is_running: bool = False

    @rx.event
    def set_slide(self, index: int):
        self.current_slide = index

    @rx.event(background=True)
    async def start_auto_play(self):
        if self._is_running:
            return
        async with self:
            self._is_running = True
        while True:
            await asyncio.sleep(4)
            async with self:
                self.current_slide = (self.current_slide + 1) % len(self.images)