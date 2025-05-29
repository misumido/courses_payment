from aiogram import Bot, Dispatcher
import asyncio
from bot import bot_router
from database import Base, engine
# TODO токен бота
bot = Bot(token="TOKEN")
dp = Dispatcher()
Base.metadata.create_all(bind=engine)

async def main():
    dp.include_router(bot_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
