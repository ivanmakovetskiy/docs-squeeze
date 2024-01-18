from aiogram.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup


def get_kb_start() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('/pdf_transform'))
    return kb


def get_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=2)
    ikb.add(InlineKeyboardButton(text='Загрузить PDF', callback_data="PDF"),
            InlineKeyboardButton(text='Загрузить TXT', callback_data="TXT")).add(InlineKeyboardButton(text='<--',callback_data="<--"))

    return ikb
