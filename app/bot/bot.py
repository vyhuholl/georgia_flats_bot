"""Объект Bot."""

from aiogram import Bot

from app import config

bot = Bot(config.BOT_TOKEN)
