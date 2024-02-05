import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6603392903:AAG-iV93IW7jukOrZTU3rM22vNGJknfyRaU")
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(F.text.lower() == "пирожки")
async def without_puree(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Пирожок с мясом",
        callback_data="kor~5~3")
    )
    builder.add(types.InlineKeyboardButton(
        text="Пирожок с повидлом",
        callback_data="kor~5~4")
    )
    await message.answer('Выберите нужную булку', reply_markup=builder.as_markup())
hungry = 10
@dp.callback_query(F.data.startswith("kor"))
async def callbacks_num(callback: types.CallbackQuery):
    global hungry
    data = callback.data.split('~')
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=f"Булочка с корицей\nПараметр голода: {hungry}",
        callback_data="kor~5~3")
    )
    builder.add(types.InlineKeyboardButton(
        text=f"Булочка с маком\nПараметр голода: {hungry}",
        callback_data="kor~5~4")
    )
    builder.adjust(1)
    if data[1] == 'kill_kookier':
        hungry = 10
        await callback.message.edit_text('Вы убили пекаря!')
    if data[1] == '5' and data[2] == '3':
        hungry -= 2
        await callback.message.edit_text(f'Вы съели булочку с корицей!', reply_markup=builder.as_markup())
    if data[1] == '5' and data[2] == '4':
        hungry -= 1
        await callback.message.edit_text(f'Вы съели булочку с маком!', reply_markup=builder.as_markup(resize_keyboard=True))
@dp.message(F.text.lower() == "тортики")
async def without_puree(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Идти ругаться с пекарем",
        callback_data="kor~kill_kookier~3")
    )
    await message.answer('Тортики закончились! Подойтите к пекарю!', reply_markup=builder.as_markup())
@dp.message(F.text.lower() == "булочки")
async def without_puree(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Булочка с корицей",
        callback_data="kor~5~3")
    )
    builder.add(types.InlineKeyboardButton(
        text="Булочка с маком",
        callback_data="kor~5~4")
    )
    await message.answer('Выберите нужную булку', reply_markup=builder.as_markup())
@dp.message(F.text.lower() == "еда")
async def without_puree(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='Пирожки'))
    builder.add(types.KeyboardButton(text='Тортики'))
    builder.add(types.KeyboardButton(text='Булочки'))
    builder.adjust(2)
    await message.answer(
        "Выберите еду:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )
@dp.message(Command("testo"))
async def cmd_testo(message: types.Message):
    await message.answer("Пирожки готовы!")
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())