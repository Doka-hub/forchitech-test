from .config import get_settings
from .app import create_app


settings = get_settings()
app = create_app(settings)
