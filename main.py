import asyncio
import os

import jdatetime
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = "me"

start_date = jdatetime.date(1403, 7, 1)
end_date = jdatetime.date(1405, 7, 1)

def calculate_completed_percentage():
    today = jdatetime.date.today()
    total_days = (end_date.togregorian() - start_date.togregorian()).days
    passed_days = (today.togregorian() - start_date.togregorian()).days
    percentage = (passed_days / total_days) * 100
    return percentage

async def update_bio(client):
    percentage = calculate_completed_percentage()
    new_bio = f"{percentage:.2f}%"
    await client(UpdateProfileRequest(about=new_bio))


async def main():
    async with TelegramClient(session_name, api_id, api_hash) as client:
        await update_bio(client)

asyncio.run(main())
