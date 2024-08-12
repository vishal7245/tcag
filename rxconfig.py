import reflex as rx

config = rx.Config(
    app_name="tcag",
    db_url="sqlite:///reflex.db",
    frontend_port=3003,
    backend_port=8003,
    cors_allowed_origins=["*"],
)


# Create your app instance with this config
app = rx.App(config=config)