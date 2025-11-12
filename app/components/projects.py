import reflex as rx
from app.states.portfolio_state import PortfolioState, Project


def tech_tag(tech: str) -> rx.Component:
    """A tag for a technology used in a project."""
    return rx.el.span(
        tech,
        class_name="bg-teal-100 text-teal-800 text-xs font-medium px-2.5 py-1 rounded-full",
    )


def project_card(project: Project) -> rx.Component:
    """A card for displaying a project."""
    return rx.el.div(
        rx.image(
            src=project["image_url"], class_name="rounded-t-xl h-48 w-full object-cover"
        ),
        rx.el.div(
            rx.el.h3(
                project["title"], class_name="text-xl font-bold text-gray-900 mb-2"
            ),
            rx.el.p(
                project["description"],
                class_name="text-gray-600 mb-4 h-24 overflow-hidden",
            ),
            rx.el.div(
                rx.foreach(project["tech_stack"], tech_tag),
                class_name="flex flex-wrap gap-2 mb-6",
            ),
            rx.el.div(
                rx.el.a(
                    rx.icon("link", class_name="mr-2 h-4 w-4"),
                    "Live Demo",
                    href=project["live_url"],
                    target="_blank",
                    class_name="inline-flex items-center text-teal-600 hover:text-teal-800 font-semibold transition-colors",
                ),
                rx.el.a(
                    rx.icon("github", class_name="mr-2 h-4 w-4"),
                    "Source Code",
                    href=project["github_url"],
                    target="_blank",
                    class_name="inline-flex items-center text-gray-500 hover:text-gray-800 font-semibold transition-colors",
                ),
                class_name="flex items-center justify-between",
            ),
            class_name="p-6",
        ),
        class_name="bg-white rounded-xl shadow-md hover:shadow-xl transition-shadow duration-300 border border-gray-100 flex flex-col justify-between",
    )


def projects_section() -> rx.Component:
    """The projects showcase section."""
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "My Projects",
                class_name="text-3xl font-bold text-gray-900 mb-12 text-center",
            ),
            rx.el.div(
                rx.foreach(PortfolioState.projects, project_card),
                class_name="grid md:grid-cols-2 lg:grid-cols-2 gap-8",
            ),
            class_name="max-w-screen-xl mx-auto px-4 py-20",
        ),
        id="projects",
        class_name="w-full bg-gray-50",
    )