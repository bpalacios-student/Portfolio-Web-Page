import reflex as rx
from app.states.portfolio_state import PortfolioState


def skill_card(category: str, skills: list[str]) -> rx.Component:
    """A card to display a category of skills."""
    return rx.el.div(
        rx.el.h3(category, class_name="text-lg font-bold text-gray-800 mb-4"),
        rx.el.div(
            rx.foreach(
                skills,
                lambda skill: rx.el.span(
                    skill,
                    class_name="bg-gray-200 text-gray-700 text-sm font-medium px-3 py-1.5 rounded-md",
                ),
            ),
            class_name="flex flex-wrap gap-3",
        ),
        class_name="bg-white p-6 rounded-xl shadow-sm border border-gray-100",
    )


def skills_section() -> rx.Component:
    """The skills section."""
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Technical Skills",
                class_name="text-3xl font-bold text-gray-900 mb-12 text-center",
            ),
            rx.el.div(
                rx.foreach(
                    PortfolioState.skills.keys(),
                    lambda category: skill_card(
                        category, PortfolioState.skills[category]
                    ),
                ),
                class_name="grid md:grid-cols-2 gap-8",
            ),
            class_name="max-w-screen-xl mx-auto px-4 py-20",
        ),
        id="skills",
        class_name="w-full bg-white",
    )