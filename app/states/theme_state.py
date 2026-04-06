import reflex as rx


class ThemeState(rx.State):
    is_dark: bool = False

    @rx.event
    def toggle_theme(self):
        self.is_dark = not self.is_dark

    @rx.var
    def theme_icon(self) -> str:
        return "moon" if self.is_dark else "sun"

    @rx.var
    def current_bg(self) -> str:
        return "bg-slate-900" if self.is_dark else "bg-white"

    @rx.var
    def current_text(self) -> str:
        return "text-white" if self.is_dark else "text-slate-900"

    @rx.var
    def secondary_text(self) -> str:
        return "text-slate-400" if self.is_dark else "text-slate-600"

    @rx.var
    def card_bg(self) -> str:
        return "bg-slate-800" if self.is_dark else "bg-white"

    @rx.var
    def card_border(self) -> str:
        return "border-slate-700" if self.is_dark else "border-gray-100"