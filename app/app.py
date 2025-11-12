import reflex as rx
from app.components.header import header
from app.components.hero import hero_section
from app.components.about import about_section
from app.components.projects import projects_section
from app.components.skills import skills_section
from app.components.contact import contact_section
from app.components.footer import footer


def index() -> rx.Component:
    """The main portfolio page."""
    return rx.el.main(
        header(),
        hero_section(),
        about_section(),
        projects_section(),
        skills_section(),
        contact_section(),
        footer(),
        class_name="font-['JetBrains_Mono'] bg-gray-50 text-gray-800",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(
    index,
    route="/",
    title="Alex Doe | Portfolio",
    description="Portfolio of a full-stack developer.",
)