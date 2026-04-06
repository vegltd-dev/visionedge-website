import reflex as rx


class ShowcaseState(rx.State):
    selected_category: str = "All"
    is_lightbox_open: bool = False
    selected_image: dict[str, str] = {}
    categories: list[str] = [
        "All",
        "Branding",
        "Painting",
        "Car Repair and Branding",
        "Trading",
        "Partitioning and Construction",
    ]
    items: list[dict[str, str]] = [
        {
            "id": "1",
            "title": "Plascon Wall-Branding",
            "category": "Branding",
            "description": "Outdoor wall branding to visualize there product and show to public how quality there product are.",
            "Slide2": "/photos/plascon1.jpeg",
            "Slide1":"/photos/plascon.jpeg",
        },
        {
            "id": "2",
            "title": "Skol Brewery Limited (SBL)",
            "category": "Painting",
            "description": "Renew and rebuild SBL's brand in society through there outlet upcountry.",
            "Slide2": "/photos/Skol2.jpeg",
            "Slide1": "/photos/skol1.jpeg",
        },
        {
            "id": "3",
            "title": "Mount Meru Group",
            "category": "Branding and Painting",
            "description": "Advertise Mount Meru's various product upcountry through wall-Branding.",
            "Slide2": "/photos/meru2.jpeg",
            "Slide1": "/photos/meru.jpeg",
        },
        {
            "id": "4",
            "title": "Bralirwa Brewery",
            "category": "Branding and Painting",
            "description": "rebuild and remind public best products from Bralirwa Especial AMSTEL BEER.",
            "Slide2": "/photos/bralirwa1.jpeg",
            "Slide1": "/photos/bralirwa.jpeg",
        },
        {
            "id": "5",
            "title": "StarTames",
            "category": "Branding and painting",
            "description": "Expanding StarTime visibility whole country through outdoor wall-Branding ",
            "Slide2": "/photos/startime.jpeg",
            "Slide1": "/photos/startimes.jpeg",
        },
        {
            "id": "6",
            "title": "Airtel",
            "category": "Car Repair and Branding",
            "description": "Visualize Airtel on cars.",
            "Slide2": "#",
            "Slide1": "/photos/airtel.jpeg",
        },
    ]

    @rx.event
    def set_category(self, category: str):
        self.selected_category = category

    @rx.event
    def open_lightbox(self, item: dict[str, str]):
        self.selected_image = item
        self.is_lightbox_open = True

    @rx.event
    def close_lightbox(self):
        self.is_lightbox_open = False

    @rx.var
    def filtered_items(self) -> list[dict[str, str]]:
        if self.selected_category == "All":
            return self.items
        return [
            item for item in self.items if item["category"] == self.selected_category
        ]