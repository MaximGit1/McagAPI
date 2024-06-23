from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

@dataclass
class Settings:
    db_url: str = f'sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3'
    echo: bool = False
    api_v1_prefix: str = '/api/v1'


settings = Settings()

