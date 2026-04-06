import reflex as rx
from app.components.admin_sidebar import admin_sidebar
from app.states.content_state import ContentState


def project_row(post: dict) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            post["title"],
            class_name="px-6 py-4 whitespace-nowrap text-sm font-medium text-slate-900",
        ),
        rx.el.td(
            post["category"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-slate-500",
        ),
        rx.el.td(
            rx.el.span(
                post["status"],
                class_name="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-blue-100 text-blue-800",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            post["date"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-slate-500",
        ),
        rx.el.td(
            rx.el.button(
                rx.icon("trash-2", class_name="w-4 h-4"),
                on_click=lambda: ContentState.delete_post(post["id"]),
                class_name="text-red-600 hover:text-red-900 p-2 hover:bg-red-50 rounded-full transition-colors",
            ),
            class_name="px-6 py-4 whitespace-nowrap text-right text-sm font-medium",
        ),
    )


def admin_content() -> rx.Component:
    return rx.el.div(
        admin_sidebar(),
        rx.el.main(
            rx.el.div(
                rx.el.h1(
                    "Content Management",
                    class_name="text-2xl font-bold text-slate-900 mb-8",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h2(
                            "Add New Project",
                            class_name="text-lg font-bold text-slate-900 mb-4",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Project Title",
                                    class_name="block text-sm font-medium text-slate-700 mb-1",
                                ),
                                rx.el.input(
                                    placeholder="Enter project name",
                                    on_change=ContentState.set_new_title,
                                    class_name="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-orange-500 outline-none",
                                    default_value=ContentState.new_title,
                                ),
                                class_name="col-span-2",
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Category",
                                    class_name="block text-sm font-medium text-slate-700 mb-1",
                                ),
                                rx.el.select(
                                    rx.el.option("Construction", value="Construction"),
                                    rx.el.option("Branding", value="Branding"),
                                    rx.el.option("Painting", value="Painting"),
                                    rx.el.option("Car Repair", value="Car Repair"),
                                    value=ContentState.new_category,
                                    on_change=ContentState.set_new_category,
                                    class_name="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-orange-500 outline-none",
                                ),
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Status",
                                    class_name="block text-sm font-medium text-slate-700 mb-1",
                                ),
                                rx.el.select(
                                    rx.el.option("Pending", value="Pending"),
                                    rx.el.option("In Progress", value="In Progress"),
                                    rx.el.option("Completed", value="Completed"),
                                    value=ContentState.new_status,
                                    on_change=ContentState.set_new_status,
                                    class_name="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-orange-500 outline-none",
                                ),
                            ),
                            class_name="grid grid-cols-1 md:grid-cols-4 gap-4 mb-4",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Before Image URL (Optional)",
                                    class_name="block text-sm font-medium text-slate-700 mb-1",
                                ),
                                rx.el.input(
                                    placeholder="https://example.com/before.jpg",
                                    on_change=ContentState.set_new_before_image,
                                    class_name="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-orange-500 outline-none",
                                    default_value=ContentState.new_before_image,
                                ),
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "After Image URL (Optional)",
                                    class_name="block text-sm font-medium text-slate-700 mb-1",
                                ),
                                rx.el.input(
                                    placeholder="https://example.com/after.jpg",
                                    on_change=ContentState.set_new_after_image,
                                    class_name="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-orange-500 outline-none",
                                    default_value=ContentState.new_after_image,
                                ),
                            ),
                            class_name="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6",
                        ),
                        rx.el.button(
                            "Add Project",
                            on_click=ContentState.add_post,
                            class_name="px-6 py-2 bg-orange-600 hover:bg-orange-700 text-white font-bold rounded-lg transition-colors shadow-sm",
                        ),
                        class_name="bg-white p-6 rounded-xl border border-gray-100 shadow-sm mb-8",
                    ),
                    rx.el.div(
                        rx.el.table(
                            rx.el.thead(
                                rx.el.tr(
                                    rx.el.th(
                                        "Project Name",
                                        class_name="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider",
                                    ),
                                    rx.el.th(
                                        "Category",
                                        class_name="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider",
                                    ),
                                    rx.el.th(
                                        "Status",
                                        class_name="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider",
                                    ),
                                    rx.el.th(
                                        "Date Added",
                                        class_name="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider",
                                    ),
                                    rx.el.th(
                                        "Actions",
                                        class_name="px-6 py-3 text-right text-xs font-medium text-slate-500 uppercase tracking-wider",
                                    ),
                                ),
                                class_name="bg-gray-50",
                            ),
                            rx.el.tbody(
                                rx.foreach(ContentState.posts, project_row),
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