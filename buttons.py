from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder
async def payment_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text=f"Оплатить курс️", pay=True)

    return builder.as_markup()
async def phone_bt():
    buttons = [[KeyboardButton(text="📲Поделиться номером", request_contact=True)]]
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=buttons)
    return kb