from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_markup = ReplyKeyboardMarkup(keyboard=[
                                            [KeyboardButton(text="/start")]
                                            ], 
                                            resize_keyboard=True)