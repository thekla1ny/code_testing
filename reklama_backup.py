from pyrogram import Client
import asyncio

TARGET_CHAT_ID = -1002528469664
SOURCE_CHAT_ID = "me"

print("авторизация через телеграм. надо ввести данные. Создал @KingOfInsanity")

api_id = int(input("Введи свой API ID: "))
api_hash = input("Введи свой API HASH: ")
session_name = "akkaunt_data"

app = Client(session_name, api_id=api_id, api_hash=api_hash)

async def forward_last_message():
    async for message in app.get_chat_history(SOURCE_CHAT_ID, limit=1):
        if message:
            await app.forward_messages(
                chat_id=TARGET_CHAT_ID,
                from_chat_id=SOURCE_CHAT_ID,
                message_ids=message.id
            )
            print("сообщение переслано.")
        else:
            print("нет сообщений в избранном.")

async def main_loop():
    async with app:
        print("авторизован. рассылка начата.")
        while True:
            await forward_last_message()
            await asyncio.sleep(3600)

asyncio.run(main_loop())
