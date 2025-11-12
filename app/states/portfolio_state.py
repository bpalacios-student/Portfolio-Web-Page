import reflex as rx
from typing import TypedDict


class Project(TypedDict):
    title: str
    description: str
    tech_stack: list[str]
    image_url: str
    live_url: str
    github_url: str


class SocialLink(TypedDict):
    name: str
    icon: str
    url: str


class PortfolioState(rx.State):
    """Holds the state for the portfolio page."""

    form_data: dict = {}
    is_submitting: bool = False
    projects: list[Project] = [
        {
            "title": "AI-Powered Task Manager",
            "description": "A smart task management application that uses natural language processing to categorize and prioritize tasks automatically.",
            "tech_stack": ["Python", "Reflex", "NLP", "PostgreSQL"],
            "image_url": "/placeholder.svg",
            "live_url": "#",
            "github_url": "#",
        },
        {
            "title": "Real-Time Data Dashboard",
            "description": "A comprehensive dashboard for visualizing real-time data streams, featuring interactive charts and customizable widgets.",
            "tech_stack": ["React", "TypeScript", "D3.js", "WebSocket"],
            "image_url": "/placeholder.svg",
            "live_url": "#",
            "github_url": "#",
        },
        {
            "title": "E-commerce Platform API",
            "description": "A scalable and secure RESTful API for an e-commerce platform, with support for products, orders, and user authentication.",
            "tech_stack": ["Node.js", "Express", "MongoDB", "JWT"],
            "image_url": "/placeholder.svg",
            "live_url": "#",
            "github_url": "#",
        },
        {
            "title": "Cloud File Storage Service",
            "description": "A serverless file storage solution similar to Dropbox, built on AWS services for high availability and scalability.",
            "tech_stack": ["AWS Lambda", "S3", "API Gateway", "DynamoDB"],
            "image_url": "/placeholder.svg",
            "live_url": "#",
            "github_url": "#",
        },
    ]
    skills: dict[str, list[str]] = {
        "Frontend": [
            "HTML5",
            "CSS3",
            "JavaScript (ES6+)",
            "TypeScript",
            "React",
            "Reflex",
            "Tailwind CSS",
        ],
        "Backend": [
            "Python",
            "Node.js",
            "Express",
            "FastAPI",
            "PostgreSQL",
            "MongoDB",
            "Redis",
        ],
        "DevOps & Cloud": ["Docker", "Git", "GitHub Actions", "AWS", "Vercel", "Linux"],
        "Tools": ["VS Code", "Figma", "Postman", "Jira"],
    }
    social_links: list[SocialLink] = [
        {"name": "GitHub", "icon": "github", "url": "https://github.com"},
        {"name": "LinkedIn", "icon": "linkedin", "url": "https://linkedin.com"},
        {"name": "Twitter", "icon": "twitter", "url": "https://twitter.com"},
    ]

    @rx.event
    async def handle_submit(self, form_data: dict):
        """Handle contact form submission."""
        self.is_submitting = True
        yield
        import asyncio

        await asyncio.sleep(2)
        self.form_data = form_data
        self.is_submitting = False
        yield rx.toast.success("Message sent successfully!", duration=3000)
        yield rx.call_script("document.getElementById('contact-form').reset();")