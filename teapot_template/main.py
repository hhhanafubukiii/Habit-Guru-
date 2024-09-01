# импорт основных библиотек
import asyncio
import logging

# импорт объектов aiogram
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

# импорт модулей проекта
from teapot_template.config_data.config import load_config, Config
from teapot_template.handlers import main_router
from teapot_template.config_data.logging.logging_settings import logging_config
from logging.config import dictConfig


dictConfig(logging_config)
logger = logging.getLogger(__name__)
logger.propagate = False


async def main() -> None:
    logger.info('Starting bot')
    config: Config = load_config('.env')
    storage = MemoryStorage()
    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=storage)
    dp.include_router(main_router)
    dp.workflow_data.update()
    await bot.delete_webhook(drop_pending_updates=True)
    # drop_pending_updates - пропуск накопившихся апдейтов
    await dp.start_polling(bot, allowed_updates=[])


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info('Exit')
