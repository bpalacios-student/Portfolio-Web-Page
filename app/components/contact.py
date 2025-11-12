import reflex as rx
from app.states.portfolio_state import PortfolioState, SocialLink


def social_icon_link(link: SocialLink) -> rx.Component:
    """An icon link for social media."""
    return rx.el.a(
        rx.icon(tag=link["icon"], class_name="h-6 w-6"),
        href=link["url"],
        target="_blank",
        class_name="text-gray-500 hover:text-teal-500 transition-colors duration-300",
    )


def contact_section() -> rx.Component:
    """The contact section with form and social links."""
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Get In Touch",
                class_name="text-3xl font-bold text-gray-900 mb-4 text-center",
            ),
            rx.el.p(
                "Have a project in mind or just want to say hello? I'd love to hear from you.",
                class_name="text-lg text-gray-600 mb-12 text-center max-w-2xl mx-auto",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Contact Information",
                        class_name="text-xl font-semibold text-gray-800 mb-4",
                    ),
                    rx.el.div(
                        rx.icon("mail", class_name="h-5 w-5 mr-3 text-teal-500"),
                        rx.el.a(
                            "alex.doe@example.com",
                            href="mailto:alex.doe@example.com",
                            class_name="text-gray-600 hover:text-teal-600",
                        ),
                        class_name="flex items-center mb-4",
                    ),
                    rx.el.div(
                        rx.icon("phone", class_name="h-5 w-5 mr-3 text-teal-500"),
                        rx.el.span("+1 (555) 123-4567", class_name="text-gray-600"),
                        class_name="flex items-center mb-8",
                    ),
                    rx.el.h3(
                        "Follow Me",
                        class_name="text-xl font-semibold text-gray-800 mb-4",
                    ),
                    rx.el.div(
                        rx.foreach(PortfolioState.social_links, social_icon_link),
                        class_name="flex items-center gap-6",
                    ),
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.input(
                            placeholder="Your Name",
                            name="name",
                            type="text",
                            required=True,
                            class_name="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-shadow",
                        ),
                        rx.el.input(
                            placeholder="Your Email",
                            name="email",
                            type="email",
                            required=True,
                            class_name="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-shadow",
                        ),
                        class_name="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6",
                    ),
                    rx.el.textarea(
                        placeholder="Your Message",
                        name="message",
                        required=True,
                        rows=6,
                        class_name="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-shadow mb-6",
                    ),
                    rx.el.button(
                        rx.cond(
                            PortfolioState.is_submitting,
                            rx.el.div(
                                rx.spinner(class_name="h-5 w-5"),
                                "Sending...",
                                class_name="flex items-center gap-2",
                            ),
                            rx.el.div(
                                "Send Message",
                                rx.icon("send", class_name="ml-2 h-4 w-4"),
                                class_name="flex items-center",
                            ),
                        ),
                        type="submit",
                        disabled=PortfolioState.is_submitting,
                        class_name="w-full bg-teal-500 text-white px-8 py-3 rounded-lg hover:bg-teal-600 transition-colors duration-300 font-semibold shadow-md disabled:bg-teal-300 disabled:cursor-not-allowed",
                    ),
                    on_submit=PortfolioState.handle_submit,
                    id="contact-form",
                ),
                class_name="grid md:grid-cols-2 gap-16 items-start",
            ),
            class_name="max-w-screen-xl mx-auto px-4 py-20",
        ),
        id="contact",
        class_name="w-full bg-gray-50",
    )