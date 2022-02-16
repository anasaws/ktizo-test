from config.config import settings
from fastapi import FastAPI
from router import register_login,spotify
from fastapi.middleware.cors import CORSMiddleware

desc = """
This project is a Music application
"""

tags_metadata = [
    {"name": "artist", "description": "This is artist route"},
    {"name": "producer", "description": "This is producer route"},
]

app = FastAPI(
    title=settings.PROJECT_TITLE,
    version=settings.PROJECT_VERSION,
    description=desc,
    openapi_tags=tags_metadata,
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(register_login.app)
app.include_router(spotify.app)
