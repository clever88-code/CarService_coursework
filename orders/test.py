

import asyncio

from aiogram import Bot, types

API_TOKEN = '5819517876:AAErNVMBQoSyI5DhmVf8ACSQA5LQU-hAcgE'
CHANNEL_ID = '1015269507' 

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)

async def send_message(channel_id: int, text: str):
    await bot.send_message(channel_id, text)
        
        
async def main():
    await send_message(CHANNEL_ID, 'Выполнена работа для заказа!🔥🔥🔥')

if __name__ == '__main__':
    asyncio.run(main())