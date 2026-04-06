import reflex as rx


class NavState(rx.State):
    is_mobile_menu_open: bool = False

    @rx.event
    def toggle_mobile_menu(self):
        self.is_mobile_menu_open = not self.is_mobile_menu_open

    @rx.event
    def close_mobile_menu(self):
        self.is_mobile_menu_open = False