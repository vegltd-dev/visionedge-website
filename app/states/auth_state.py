import reflex as rx


class AuthState(rx.State):
    username: str = ""
    password: str = ""
    is_authenticated: bool = False
    error_message: str = ""

    @rx.event
    def login(self, form_data: dict):
        self.username = form_data.get("username", "")
        self.password = form_data.get("password", "")
        if self.username == "admin" and self.password == "admin123":
            self.is_authenticated = True
            self.error_message = ""
            return rx.redirect("/admin/dashboard")
        else:
            self.error_message = "Invalid username or password"

    @rx.event
    def logout(self):
        self.username = ""
        self.password = ""
        self.is_authenticated = False
        return rx.redirect("/admin")

    @rx.event
    def check_login(self):
        if not self.is_authenticated:
            return rx.redirect("/admin")

    @rx.event
    def check_redirect_if_auth(self):
        if self.is_authenticated:
            return rx.redirect("/admin/dashboard")