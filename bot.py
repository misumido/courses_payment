
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from states import *
from aiogram.types import Message, BotCommand, CallbackQuery, LabeledPrice
from buttons import *
from database.userservice import *
from all_txt import courses
bot_router = Router()
products_price = {"self_taught": 999000, "advanced": 1999000, "analytics":499000, "premium":9880000}
#TODO все ссылки
links = {"self_taught": "https://t.me/uzumguru_school_bot?start=self_taught",
         "advanced": "https://t.me/uzumguru_school_bot?start=advanced",
         "analytics":"https://t.me/uzumguru_school_bot?start=analytics",
         "premium":"https://t.me/uzumguru_school_bot?start=premium"}
@bot_router.message(CommandStart())
async def start(message: Message, state: FSMContext, command: BotCommand = None):
    if command.args in products_price:
        print(command.args)
        product = command.args
        await message.bot.send_message(chat_id=message.from_user.id, text="Отправьте свой номер телефона через кнопку в меню",
                                       reply_markup= await phone_bt())
        await state.set_data({"product": product})
        await state.set_state(Registration.number_st)
    else:
        await message.bot.send_message(chat_id=message.from_user.id,
                                       text="Для работы с ботом перейдите по ссылке необходимого товара")
@bot_router.message(Registration.number_st)
async def get_number(message: Message, state: FSMContext):
    if message.contact:
        data = await state.get_data()
        number = message.contact.phone_number
        product = data.get("product")
        desc = courses.get(product)
        add_user(tg_id=message.from_user.id, phone_number=number, product=product)
        prices = [LabeledPrice(label="Сум", amount=products_price.get(product)*100)]
        await message.bot.send_message(chat_id=message.from_user.id, text=desc)
        #TODO токен оплаты
        await message.answer_invoice(
            title="Оплата за курс",
            description=f"Оплатите счет по кнопке",
            prices=prices,
            provider_token="TOKEN",
            payload=str(product),
            currency="UZS",
            reply_markup=await payment_keyboard()
        )
        await state.clear()
    else:
        await message.bot.send_message(chat_id=message.from_user.id, text="Номер необходимо отправить через кнопку",
                                       reply_markup= await phone_bt())
        await state.set_state(Registration.number_st)


@bot_router.pre_checkout_query()
async def pre_checkout(query: CallbackQuery):
    await query.answer(ok=True)


@bot_router.message(F.successful_payment)
async def successful_payment(message: Message):
    payment_info = message.successful_payment
    tg_id = message.from_user.id
    product = payment_info.payload
    payment_status(tg_id, product)
    #TODO чат админов
    admin_chat_id = 305896408
    phone = get_phone_db(tg_id)
    await message.bot.send_message(
        chat_id=admin_chat_id,
        text=f"Новый платеж:\n"
             f"Пользователь: {message.from_user.id}\n"
             f"Номер телефона: {phone}\n"
             f"Сумма: {payment_info.total_amount / 100} UZS\n"
             f"Курс: {product}"
    )
    await message.answer("Товар успешно оплачен")