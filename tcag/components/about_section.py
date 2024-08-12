import reflex as rx

quote_style = {
    "font_size": "2em",
    "color": "green",
    "font_weight": "bold",
    "margin_bottom": "40px"
}

def about_card(title: str, content: str) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading(title, size="7", color="black", weight="medium", margin_bottom="10px",),
            rx.text(content, color="gray", size="5", text_align="justify"),
            align="start",
            spacing="4",
        ),
        height="100%",
        max_width="600px",
        padding="30px",
        border="1px solid #e0e0e0",
        border_radius="8px",
        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
        _hover = {
            "background": "#A8F7D4",
        }
    )

def about_section() -> rx.Component:
    return rx.section(
                rx.vstack(
                    rx.heading(
                        "ABOUT US",
                        size="5",
                        weight="bold",
                        margin_bottom="1em",
                        color="green",
                    ),
                    rx.heading(
                        "Who we are",
                        size="8",
                        weight="medium",
                        color="black",
                        margin_bottom="10px",
                    ),
                    rx.text.quote(
                            "Taking Care of Your Tomorrow", style=quote_style
                        ),
                    rx.grid(
                        about_card(
                            "Background",
                            "We are fascinated by the revolution of genomics with the addition of new and improved DNA sequencing technologies and its capability to bring change in our day-to-day lifestyle and healthcare. We are looking forward to collaborating and contributing to research and innovation with both government and private partners in the genomics application field."
                        ),
                        about_card(
                            "Mission",
                            "For 19 years, we have been a team with experience in genetics, genomics, molecular biology, and bioinformatics, sharing an equal enthusiasm to bring change to humanity. We are passionate about delivering the best services in our industry, not only involving consultation, training, and support but also delivering great value to our esteemed customers."
                        ),
                        columns="2",
                        spacing="5",
                    ),
                    justify_content="center",
                    align_items="center",
                    width="100%",
                ),
                width="100%",
            )