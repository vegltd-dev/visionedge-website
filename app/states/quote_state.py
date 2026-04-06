import reflex as rx
import asyncio
import requests


class QuoteState(rx.State):
    is_loading: bool = False

    @rx.event
    async def handle_submit(self, form_data: dict):
        self.is_loading = True
        await asyncio.sleep(1.5)
        required_fields = ["name", "email", "phone", "message"]
        missing_fields = [
            field for field in required_fields if not form_data.get(field)
        ]
        if missing_fields:
            self.is_loading = False
            yield rx.toast.error(
                f"Please fill in all required fields: {', '.join(missing_fields)}"
            )
            return
        if "@" not in form_data.get("email", ""):
            self.is_loading = False
            yield rx.toast.error("Please enter a valid email address.")
            return
        self.is_loading = False
        yield rx.toast.success("Quote request received! We will contact you shortly.")

        # ✅ Send to Formspree
        try:
            response = requests.post(
                "https://formspree.io/f/mjgppgpe",
                data=form_data,
            )

            if response.status_code in [200, 302]:
                yield rx.toast.success(
                    "✅ Quote request sent! We will contact you shortly."
                )
            else:
                print(response.text)
                yield rx.toast.error("❌ Failed to send message. Try again.")

        except Exception as e:
            print(e)
            yield rx.toast.error("❌ Error sending message.")

        self.is_loading = False