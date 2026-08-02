import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

# ==========================
# Telegram
# ==========================
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

# ==========================
# OpenAI
# ==========================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# ==========================
# MongoDB
# ==========================
MONGO_URL = os.getenv("MONGO_URL", "")

DB_NAME = os.getenv("DB_NAME", "leo_ai_bot")

# ==========================
# AI Model
# ==========================
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gpt-4o")

# ==========================
# Validation
# ==========================
if not TELEGRAM_BOT_TOKEN:
    print("❌ TELEGRAM_BOT_TOKEN is missing")

if not OPENAI_API_KEY:
    print("❌ OPENAI_API_KEY is missing")

if not MONGO_URL:
    print("❌ MONGO_URL is missing")