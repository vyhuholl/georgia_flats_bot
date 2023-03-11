"""Starts the bot."""

from aiogram import Dispatcher
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram_dialog import DialogRegistry
from aiogram.types import BotCommand
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import config
from app import constants
from app.bot import bot
from app.bot import handlers
from app.bot.dialogues import register_dialogues
from app.db.models import Base

# Storage and dispatcher instances
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
registry = DialogRegistry(dp)


async def startup(dispatcher: Dispatcher) -> None:
    """
    Initializes the bot.

    Args:
        dispatcher: an instance of Dispatcher clas
    """
    logger.info("Registering dialogues...")
    await register_dialogues(registry)

    # Setup handlers
    logger.info("Configuring handlers...")
    handlers.setup(dispatcher)

    logger.info("Configuring database...")
    engine = create_engine(config.DB_URL)
    Session = sessionmaker(bind=engine)
    await Base.metadata.create_all(engine)

    # Set command hints
    await dp.bot.set_my_commands(
        [
            BotCommand(command, description)
            for command, description in constants.COMMANDS.items()
        ],
        language_code="ru",
    )

    logger.info("Start scheduler")
    scheduler.start()

    logger.info("Start polling")


if __name__ == "__main__":
    # Start long-polling mode
    executor.start_polling(dp, on_startup=startup)
