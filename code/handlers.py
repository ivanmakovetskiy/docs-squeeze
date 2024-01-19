from io import BytesIO
from aiogram.types.input_file import InputFile
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards import pdf_keyboard
from states import RegisterState
from aiogram.types import FSInputFile
import requests

async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,'Добро пожаловать в бот! Выберите тип файла, который хотите загрузить', reply_markup=pdf_keyboard )

async def start_dow(message:Message, state: FSMContext):
    await message.delete()
    await message.answer((f'Загрузите PDF файл в бота'))
    await state.set_state(RegisterState.DowPDF)

async def dow_file(message: Message, bot: Bot, state:FSMContext):
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    dic = r"C:\Users\vladp\NIR_BOT\code\pdf"
    file_local_path = rf'{dic}\{file_id}.pdf'
    await bot.download_file(file_path, rf'{dic}\{file_id}.pdf')
    await message.answer((f'PDF файл загружен'))
    await state.update_data(id_file = file_id)
    # Send the file using requests.post
    with open(file_local_path, 'rb') as file:
        response = requests.post(f"http://localhost:8000/pdf", files={'file': file})
    # Check the response if needed
    if response.status_code == 200:
        # Извлекаем содержимое файла из ответа
        file_content = response.content
        dic_r = r"C:\Users\vladp\NIR_BOT\code\out"
        response_local_path = rf'{dic_r}\{file_id}.txt'
        # Далее можно сохранить содержимое файла или обработать по вашему усмотрению
        with open(response_local_path, 'wb') as output_file:
            output_file.write(file_content)
        doc = FSInputFile(response_local_path)
        await bot.send_document(message.from_user.id, document=doc)
        await message.answer('Файл успешно отправлен пользователю')
    else:
        await message.answer(f'Произошла ошибка при отправке файла. Код ошибки: {response.status_code}')