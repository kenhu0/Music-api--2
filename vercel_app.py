"""Expose the existing FastAPI application to Vercel without moving it."""

import sys
from pathlib import Path


APP_DIR = Path(__file__).resolve().parent / "music-api"
sys.path.insert(0, str(APP_DIR))

from app import app  # noqa: E402
