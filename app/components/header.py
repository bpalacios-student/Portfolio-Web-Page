import reflex as rx
from app.states.portfolio_state import PortfolioState


def nav_link(text: str, section_id: str) -> rx.Component:
    """A navigation link that smoothly scrolls to a section."""
    return rx.el.a(
        text,
        href=f"#{section_id}",
        on_click=rx.call_script(
            f"document.getElementById('{section_id}').scrollIntoView({{behavior: 'smooth'}});"
        ),
        class_name="text-gray-500 hover:text-teal-500 transition-colors duration-300 font-medium",
    )


def header() -> rx.Component:
    """The sticky header for the portfolio page."""
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.icon("code-xml", class_name="h-7 w-7 text-teal-500"),
                    href="#",
                    class_name="flex items-center gap-2",
                ),
                rx.el.span(
                    "Alex Doe", class_name="font-semibold text-lg text-gray-800"
                ),
            ),
            rx.el.nav(
                nav_link("About", "about"),
                nav_link("Projects", "projects"),
                nav_link("Skills", "skills"),
                nav_link("Contact", "contact"),
                class_name="hidden md:flex items-center gap-8",
            ),
            rx.el.a(
                rx.el.button(
                    "Contact Me",
                    rx.icon("send", class_name="ml-2 h-4 w-4"),
                    on_click=rx.call_script(
                        "document.getElementById('contact').scrollIntoView({behavior: 'smooth'});"
                    ),
                    class_name="hidden md:flex items-center bg-teal-500 text-white px-4 py-2 rounded-lg hover:bg-teal-600 transition-colors duration-300 font-semibold shadow-sm",
                )
            ),
            class_name="flex items-center justify-between max-w-screen-xl mx-auto px-4 py-3",
        ),
        class_name="sticky top-0 z-50 w-full bg-white/80 backdrop-blur-md border-b border-gray-200",
    )