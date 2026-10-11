import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = (
    Path(os.environ.get("MUSIC_API_DATA_DIR", "/tmp/music-api"))
    if os.environ.get("VERCEL") == "1"
    else BASE_DIR
)

DATABASE_PATH = DATA_DIR / "database" / "music.db"
CACHE_DIR = DATA_DIR / "cache"
LOG_DIR = DATA_DIR / "logs"
DOWNLOAD_DIR = DATA_DIR / "downloads"

APP_NAME = "WLZBI Music API"
VERSION = "1.0.0"

HOST = "0.0.0.0"
PORT = 8000

CACHE_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)
DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)