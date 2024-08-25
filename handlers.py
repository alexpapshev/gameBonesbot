from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from asyncio import sleep
from confir import TOKEN

import keyboard as kb


router = Router()
markup = kb.main_markup

@router.message(CommandStart())
async def start(message: Message):
    if message.from_user is None:
        await message.answer('Error: from_user is None')
        return
    await message.answer(f'Hello, {message.from_user.username} game is start!',
                           reply_markup=markup)
    
    dice1 = await message.answer_dice()
    dice2 = await message.answer_dice()
    await sleep(4)
    if dice1.dice is None or dice2.dice is None:
        await message.answer('Error: dice1 or dice2 is None')
        return
    # print('Dice 1', dice1.dice.value)
    # print('Dice 2', dice2.dice.value)
    if dice1.dice.value > dice2.dice.value:
        await message.answer(f'You win! {dice1.dice.value} > {dice2.dice.value}')
    elif dice1.dice.value < dice2.dice.value:
        await message.answer(f'You lose! {dice1.dice.value} < {dice2.dice.value}')
    else:
        await message.answer(f'Draw! {dice1.dice.value} = {dice2.dice.value}') 
