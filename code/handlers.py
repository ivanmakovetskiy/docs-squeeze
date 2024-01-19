from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards import pdf_keyboard
from states import RegisterState

async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,'Добро пожаловать в бот! Выберите тип файла, который хотите загрузить', reply_markup=pdf_keyboard )

async def start_dow(message:Message, state: FSMContext):
    await message.delete()
    await message.answer((f'Загрузите PDF файл в бота'))
    await state.set_state(RegisterState.DowPDF)

async def dow_file(message: Message, bot: Bot):
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    dic = r"C:\Users\vladp\NIR_BOT\code\pdf"
    await bot.download_file(file_path, rf'{dic}\{file_id}.pdf')
    await message.answer((f'PDF файл загружен'))