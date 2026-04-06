
import reflex as rx
from app.components.navbar import navbar
from app.components.hero import hero
from app.components.services import services
from app.components.featured_projects import featured_projects
from app.components.footer import footer
from app.components.sticky_buttons import sticky_buttons
from app.components.quote import quote_page
from app.components.instagram_feed import instagram_feed
from app.states.theme_state import ThemeState
from app.states.auth_state import AuthState
from app.states.analytics_state import AnalyticsState
from app.states.hero_state import HeroState
from app.pages.admin_login import admin_login
from app.pages.admin_dashboard import admin_dashboard
from app.pages.admin_content import admin_content
from app.pages.showcase import showcase_page
from app.pages.about import about_page
from app.pages.contact import contact_page
from app.pages.privacy import privacy_page
from app.pages.terms import terms_page
from app.pages.careers import careers_page


def index() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            hero(),
            services(),
            featured_projects(),
            instagram_feed(),
            class_name="flex-grow",
        ),
        footer(),
        sticky_buttons(),
        class_name=rx.cond(
            ThemeState.is_dark,
            "min-h-screen flex flex-col bg-slate-900 font-['Lato'] transition-colors duration-300",
            "min-h-screen flex flex-col bg-white font-['Lato'] transition-colors duration-300",
        ),
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        # ✅ Title
        rx.el.title("VisionEdge"),

        # ✅ Favicon
        rx.el.link(rel="icon", href="/logo.png"),

        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700;900&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(
    index, route="/", on_load=[AnalyticsState.track_visit, HeroState.start_auto_play]
)
app.add_page(quote_page, route="/quote", on_load=AnalyticsState.track_visit)
app.add_page(showcase_page, route="/showcase", on_load=AnalyticsState.track_visit)
app.add_page(admin_login, route="/admin", on_load=AuthState.check_redirect_if_auth)
app.add_page(admin_dashboard, route="/admin/dashboard", on_load=AuthState.check_login)
app.add_page(admin_content, route="/admin/content", on_load=AuthState.check_login)
app.add_page(about_page, route="/about")
app.add_page(contact_page, route="/contact")
app.add_page(privacy_page, route="/privacy")
app.add_page(terms_page, route="/terms")
app.add_page(careers_page, route="/careers")