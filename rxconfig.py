import reflex as rx

config = rx.Config(
    app_name="tcag",
    db_url="sqlite:///reflex.db",
    api_url="https://tcaglifesciences.com",
    frontend_port=3003,
    backend_port=8003,
    cors_allowed_origins=["*"],
)


