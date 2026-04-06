import reflex as rx
from app.components.admin_sidebar import admin_sidebar
from app.states.analytics_state import AnalyticsState
from app.states.auth_state import AuthState


def stat_card(title: str, value: str, icon: str, trend: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(title, class_name="text-sm font-medium text-slate-500"),
                rx.el.h3(value, class_name="text-2xl font-bold text-slate-900 mt-1"),
            ),
            rx.el.div(
                rx.icon(icon, class_name="w-6 h-6 text-orange-600"),
                class_name="p-3 bg-orange-50 rounded-full",
            ),
            class_name="flex justify-between items-start mb-4",
        ),
        rx.el.div(
            rx.el.span(
                trend, class_name="text-green-600 text-sm font-medium flex items-center"
            ),
            rx.el.span("vs last month", class_name="text-slate-400 text-sm ml-2"),
            class_name="flex items-center",
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-100 shadow-sm",
    )


def recent_visit_row(visit: dict) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            visit["page"],
            class_name="px-6 py-4 whitespace-nowrap text-sm font-medium text-slate-900",
        ),
        rx.el.td(
            visit["time"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-slate-500",
        ),
        rx.el.td(
            rx.el.span(
                visit["device"],
                class_name="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-slate-100 text-slate-800",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
    )


def admin_dashboard() -> rx.Component:
    return rx.el.div(
        admin_sidebar(),
        rx.el.main(
            rx.el.div(
                rx.el.h1(
                    "Dashboard Overview",
                    class_name="text-2xl font-bold text-slate-900 mb-8",
                ),
                rx.el.div(
                    stat_card(
                        "Total Visitors",
                        AnalyticsState.total_visits.to_string(),
                        "users",
                        "+12%",
                    ),
                    stat_card(
                        "Today's Views",
                        AnalyticsState.today_visits.to_string(),
                        "eye",
                        "+5%",
                    ),
                    stat_card("Active Projects", "8", "briefcase", "+2"),
                    stat_card("Pending Quotes", "3", "message-square", "-1"),
                    class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8",
                ),
                rx.el.div(
                    rx.el.h2(
                        "Recent Activity",
                        class_name="text-lg font-bold text-slate-900 mb-4",
                    ),
                    rx.el.div(
                        rx.el.table(
                            rx.el.thead(
                                rx.el.tr(
                                    rx.el.th(
                                        "Page Visited",
                                        class_name="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider",
                                    ),
                                    rx.el.th(
                                        "Time",
                                        class_name="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider",
                                    ),
                                    rx.el.th(
                                        "Device",
                                        class_name="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider",
                                    ),
                                ),
                                class_name="bg-gray-50",
                            ),
                            rx.el.tbody(
                                rx.foreach(
                                    AnalyticsState.recent_visits, recent_visit_row
                                ),
                                class_name="bg-white divide-y divide-gray-200",
                            ),
                            class_name="min-w-full divide-y divide-gray-200",
                        ),
                        class_name="bg-white rounded-xl border border-gray-100 shadow-sm overflow-hidden",
                    ),
                ),
                class_name="p-8 max-w-7xl mx-auto",
            ),
            class_name="flex-1 bg-slate-50 overflow-auto h-screen",
        ),
        class_name="flex h-screen w-full",
    )