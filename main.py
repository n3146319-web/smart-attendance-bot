import asyncio
import logging
from aiogram import Bot, Dispatcher, types

TOKEN = "9240279789:AAHkXqMOnumNt2Tjp--g7zbovQ9AfcQ29DYZ"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="📍 Jonli lokatsiyani yuborish", request_location=True))
    
    await message.answer(
        "Assalomu alaykum! Xodimlar davomat botiga xush kelibsiz.\n"
        "Ishga kelganingizni qayd etish uchun pastdagi tugmani bosing va lokatsiyangizni yuboring.",
        reply_markup=keyboard
    )

@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    date_time = message.date.strftime("%Y-%m-%d %H:%M:%S")
    
    await message.answer(
        f"✅ Lokatsiyangiz qabul qilindi!\n"
        f"🕒 Vaqt: {date_time}\n"
        f"🌐 Kenglik: {lat}\n"
        f"🌐 Uzunlik: {lon}"
    )

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())