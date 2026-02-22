from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.base import Base
from app.database.session import engine
from app.core.config import get_settings
from app.users.router import router as users_router
from app.auth.router import router as auth_router

settings = get_settings()


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        debug=settings.DEBUG,
    )

    # ===============================
    # CORS
    # ===============================
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",
            "http://localhost:5173",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # ===============================
    # Routers
    # ===============================
    app.include_router(auth_router)
    app.include_router(users_router)

    # ===============================
    # Routes
    # ===============================
    @app.get("/")
    def root():
        return {"test": "Hello World"}

    return app


app = create_app()

# Create tables
Base.metadata.create_all(bind=engine)
