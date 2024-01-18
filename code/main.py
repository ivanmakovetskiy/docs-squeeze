import asyncio
import logging

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards import get_kb_start, get_ikb
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from conf import TOKEN
from aiogram import Bot, types, Dispatcher

bot = Bot(TOKEN)
str = MemoryStorage()
dp = Dispatcher(bot, storage=str)

class ProfileStatesGroup(StatesGroup):
    start = State()
    select_type = State()
    transform = State()

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


async def cmd_start(message: types.Message, state: FSMContext):
    await bot.send_message(
        chat_id=message.chat.id,
        text='Добро пожаловать в бот! Выберите тип файла, который хотите загрузить',
        reply_markup=get_ikb()
    )
    await ProfileStatesGroup.select_type.set()
def register_command(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start', state='*')
register_command(dp)

@dp.message_handler(Text(startswith='/'))
async def cmd_non(message: types.Message, state: FSMContext) -> None:
    await message.answer('Неизвестная команда. Попробуйте ввести /help')
    await ProfileStatesGroup.start.set()

@dp.callback_query_handler(lambda callback: True, state=ProfileStatesGroup.select_type)
async def model_callback(callback: types.CallbackQuery, state: FSMContext):
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
            await ProfileStatesGroup.transform.set()
        elif callback.data == "<--":
            await callback.message.answer('Возвращаемся назад...')
            await callback.answer()
            await state.finish()
            await bot.send_message(
                chat_id=callback.message.chat.id,
                text='Добро пожаловать в бот! Выберите тип файла, который хотите загрузить',
                reply_markup=get_ikb()
            )
        else:
            await callback.message.delete()
            await callback.answer()
            await state.finish()
            await bot.send_message(
                chat_id=callback.message.chat.id,
                text='Добро пожаловать в бот! Выберите тип файла, который хотите загрузить',
                reply_markup=get_ikb()
            )
    except Exception as e:
        logging.exception(e)

if __name__ == '__main__':
    asyncio.run(main())
