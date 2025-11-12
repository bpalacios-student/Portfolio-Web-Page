import reflex as rx


def about_section() -> rx.Component:
    """The about section of the portfolio."""
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "About Me",
                class_name="text-3xl font-bold text-gray-900 mb-8 text-center",
            ),
            rx.el.div(
                rx.image(
                    src=f"https://api.dicebear.com/9.x/initials/svg?seed=Alex Doe",
                    class_name="w-48 h-48 rounded-full object-cover shadow-lg border-4 border-white",
                ),
                rx.el.div(
                    rx.el.p(
                        "I am a passionate full-stack developer with a love for creating elegant and efficient solutions to complex problems. With a strong foundation in both frontend and backend technologies, I enjoy bringing ideas to life through code.",
                        class_name="text-lg text-gray-600 mb-4",
                    ),
                    rx.el.p(
                        "My journey into technology was driven by a fascination with artificial intelligence. I am constantly exploring new ways to integrate machine learning models into practical applications to create smarter, more intuitive user experiences. When I'm not coding, I enjoy contributing to open-source projects and exploring the great outdoors.",
                        class_name="text-lg text-gray-600",
                    ),
                    class_name="max-w-2xl",
                ),
                class_name="grid md:grid-cols-2 gap-12 items-center",
            ),
            class_name="max-w-screen-xl mx-auto px-4 py-20",
        ),
        id="about",
        class_name="w-full bg-white",
    )