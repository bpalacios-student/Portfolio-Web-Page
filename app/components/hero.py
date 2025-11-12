import reflex as rx


def hero_section() -> rx.Component:
    """The hero section of the portfolio."""
    return rx.el.section(
        rx.el.div(
            rx.el.h1(
                "Alex Doe",
                class_name="text-5xl md:text-7xl font-bold text-gray-900 mb-4 tracking-tighter",
            ),
            rx.el.h2(
                "Full-Stack Developer & AI Enthusiast",
                class_name="text-xl md:text-2xl font-medium text-teal-600 mb-8",
            ),
            rx.el.p(
                "Building modern, scalable, and intelligent web applications from concept to deployment.",
                class_name="max-w-2xl text-lg text-gray-600 mb-12 text-center",
            ),
            rx.el.div(
                rx.el.a(
                    "View Projects",
                    rx.icon("arrow-down", class_name="ml-2 h-4 w-4"),
                    href="#projects",
                    on_click=rx.call_script(
                        "document.getElementById('projects').scrollIntoView({behavior: 'smooth'});"
                    ),
                    class_name="flex items-center justify-center bg-teal-500 text-white px-8 py-3 rounded-xl hover:bg-teal-600 transition-all duration-300 font-semibold shadow-lg hover:shadow-xl transform hover:-translate-y-1 w-full md:w-auto",
                ),
                rx.el.a(
                    "Contact Me",
                    rx.icon("mail", class_name="ml-2 h-4 w-4"),
                    href="#contact",
                    on_click=rx.call_script(
                        "document.getElementById('contact').scrollIntoView({behavior: 'smooth'});"
                    ),
                    class_name="flex items-center justify-center bg-gray-100 text-gray-800 px-8 py-3 rounded-xl hover:bg-gray-200 transition-all duration-300 font-semibold shadow-lg hover:shadow-xl transform hover:-translate-y-1 w-full md:w-auto",
                ),
                class_name="flex flex-col md:flex-row items-center gap-4",
            ),
            class_name="flex flex-col items-center justify-center text-center py-20 md:py-32",
        ),
        id="hero",
        class_name="w-full bg-gray-50",
    )