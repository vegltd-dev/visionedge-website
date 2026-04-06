import reflex as rx
from datetime import datetime


class AnalyticsState(rx.State):
    total_visits: int = 1245
    today_visits: int = 45
    recent_visits: list[dict[str, str]] = [
        {"time": "10:23 AM", "page": "Home", "device": "Desktop"},
        {"time": "10:25 AM", "page": "Services", "device": "Mobile"},
        {"time": "10:28 AM", "page": "Quote", "device": "Tablet"},
        {"time": "10:42 AM", "page": "Home", "device": "Desktop"},
        {"time": "11:05 AM", "page": "About", "device": "Mobile"},
    ]

    @rx.event
    def track_visit(self):
        self.total_visits += 1
        self.today_visits += 1
        now = datetime.now().strftime("%I:%M %p")
        self.recent_visits.insert(0, {"time": now, "page": "Home", "device": "Desktop"})
        if len(self.recent_visits) > 10:
            self.recent_visits.pop()