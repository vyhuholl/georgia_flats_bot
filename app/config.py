"""Configuration file."""

import os

from dotenv import load_dotenv
from sqlalchemy import URL

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")

DB_USER = os.environ.get("DB_USER", "postgres")
DB_PWD = os.environ.get("DB_PWD", "")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_NAME = os.environ.get("DB_NAME", "test_db")

DB_URL = URL.create(
    "postgresql+psycopg2",
    username=config.DB_USER,
    password=config.DB_PWD,
    host=config.DB_HOST,
    database=config.DB_NAME,
)
