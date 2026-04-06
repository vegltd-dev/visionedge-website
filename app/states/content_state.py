import reflex as rx


class ContentState(rx.State):
    posts: list[dict[str, str]] = [
        {
            "id": "1",
            "title": "Modern Villa Renovation",
            "category": "Construction",
            "status": "Completed",
            "date": "2024-01-15",
            "before_img": "https://images.unsplash.com/photo-1484154218962-a1c002085d2f?q=80&w=500",
            "after_img": "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?q=80&w=500",
        },
        {
            "id": "2",
            "title": "TechStartup Rebrand",
            "category": "Branding",
            "status": "In Progress",
            "date": "2024-02-01",
            "before_img": "",
            "after_img": "",
        },
        {
            "id": "3",
            "title": "Luxury Apartment Painting",
            "category": "Painting",
            "status": "Pending",
            "date": "2024-02-10",
            "before_img": "",
            "after_img": "",
        },
    ]
    new_title: str = ""
    new_category: str = "Construction"
    new_status: str = "Pending"
    new_before_image: str = ""
    new_after_image: str = ""

    @rx.event
    def set_new_before_image(self, value: str):
        self.new_before_image = value

    @rx.event
    def set_new_after_image(self, value: str):
        self.new_after_image = value

    @rx.event
    def add_post(self):
        if self.new_title == "":
            return rx.toast.error("Title is required")
        new_id = str(len(self.posts) + 1)
        self.posts.insert(
            0,
            {
                "id": new_id,
                "title": self.new_title,
                "category": self.new_category,
                "status": self.new_status,
                "date": "2024-02-20",
                "before_img": self.new_before_image,
                "after_img": self.new_after_image,
            },
        )
        self.new_title = ""
        self.new_before_image = ""
        self.new_after_image = ""
        return rx.toast.success("Project added successfully")

    @rx.event
    def delete_post(self, post_id: str):
        self.posts = [post for post in self.posts if post["id"] != post_id]
        return rx.toast.success("Project deleted")