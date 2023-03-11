"""Регистрирует диалоги."""

from aiogram_dialog import DialogRegistry

from .city import city_dialogue
from .price import price_dialogue


async def register_dialogues(registry: DialogRegistry) -> None:
    """
    Регистрирует диалоги.

    Args:
        registry: реестр
    """
    registry.register(language_dialogue)
