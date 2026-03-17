from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Satellite Ecological Analysis Platform"
    app_version: str = "0.1.0"
    api_prefix: str = "/api"

    # External services
    earth_engine_project: str | None = None
    openai_model: str = "gpt-4.1-mini"

    # Database
    database_url: str = "postgresql+psycopg://postgres:postgres@db:5432/satellite"

    # CORS (comma-separated list in env)
    cors_origins: str = "*"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    def get_cors_origins(self) -> list[str]:
        if self.cors_origins.strip() == "*":
            return ["*"]
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


settings = Settings()
