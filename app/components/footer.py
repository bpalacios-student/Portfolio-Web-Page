import reflex as rx
import datetime


def footer() -> rx.Component:
    """The footer for the portfolio page."""
    current_year = datetime.date.today().year
    return rx.el.footer(
        rx.el.div(
            rx.el.p(
                f"© {current_year} Alex Doe. All Rights Reserved.",
                class_name="text-sm text-gray-500",
            ),
            rx.el.p(
                "Built with ",
                rx.el.a(
                    "Reflex",
                    href="https://reflex.dev",
                    target="_blank",
                    class_name="text-teal-500 hover:underline",
                ),
                " & Tailwind CSS.",
                class_name="text-sm text-gray-500",
            ),
            class_name="flex flex-col md:flex-row items-center justify-between max-w-screen-xl mx-auto px-4 py-6 gap-4",
        ),
        class_name="w-full bg-white border-t border-gray-200",
    )