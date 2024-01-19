from aiogram.types import KeyboardButton,  ReplyKeyboardMarkup


pdf_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Загрузить PDF'
        )
    ]
],resize_keyboard=True,one_time_keyboard=True, input_field_placeholder='Для продолжения нажмите на кнопку ниже')

