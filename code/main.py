import asyncio
import logging

from conf import TOKEN
from aiogram import Bot, Dispatcher, F
from commands import set_commands
from handlers import get_start, start_dow, dow_file
from aiogram.filters import Command
from states import RegisterState
bot = Bot(TOKEN)
dp = Dispatcher()


async def start():
    logging.basicConfig(level=logging.INFO)
    await set_commands(bot)
    await dp.start_polling(bot , skip_updates=True)

dp.message.register(get_start, Command(commands='start'))
dp.message.register(start_dow, F.text == 'Загрузить PDF')
dp.message.register(dow_file, RegisterState.DowPDF)
"""
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        text='Добро пожаловать в бот! Выберите тип файла, который хотите загрузить',
        reply_markup=get_ikb()
    )
@dp.message(lambda message: message.text.startswith('/'))
async def handle_command(message: types.Message,):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'Неизвестная команда: {message.text}. Выберите тип файла, который хотите загрузить',
        reply_markup=get_ikb()
    )

@dp.message(Tet(startswith='/'))
async def cmd_non(message: types.Message) -> None:
    await message.answer(f'Неизвестная команда: {message.text} Попробуйте ввести /help')



@dp.callback_query(lambda callback: True)
async def model_callback(callback: types.CallbackQuery,):
    try:
        prompt_data = {
            'PDF': 'PDF',
            'TXT': 'TXT'
        }
        if callback.data in prompt_data:
            await callback.message.delete()
            await callback.message.answer(f'Вы выбрали тип файла {callback.data}')
            await bot.send_message(
                chat_id=callback.message.chat.id,
                text='Отправьте файл'
            )

        elif callback.data == "<--":
            await callback.message.answer('Возвращаемся назад...')
            await callback.answer()

            await bot.send_message(
                chat_id=callback.message.chat.id,
                text='Добро пожаловать в бот! Выберите тип файла, который хотите загрузить',
                reply_markup=get_ikb()
            )
        else:
            await callback.message.delete()
            await callback.answer()
            await bot.send_message(
                chat_id=callback.message.chat.id,
                text='Добро пожаловать в бот! Выберите тип файла, который хотите загрузить',
                reply_markup=get_ikb()
            )
    except Exception as e:
        logging.exception(e)
"""
if __name__ == '__main__':
    asyncio.run(start())
