from pyrogram import Client
import asyncio

SOURCE_CHAT_ID = "me"
TARGET_CHAT_ID = -1001984966725

print("авторизация через телеграм. надо ввести данные. Создал @KingOfInsanity. Hidden Village")
api_id = int(input("Введи свой API ID: "))
api_hash = input("Введи свой API HASH: ")
session_name = "akkaunt_data"

app = Client(session_name, api_id=api_id, api_hash=api_hash)

async def forward_last_message():
    async for message in app.get_chat_history(SOURCE_CHAT_ID, limit=1):
        if message:
            try:
                await app.forward_messages(
                    chat_id=TARGET_CHAT_ID,
                    from_chat_id=SOURCE_CHAT_ID,
                    message_ids=message.id
                )
                print("сообщение переслано.")
            except Exception as e:
                print("ошибка пересылки:", e)
        else:
            print("нет сообщений в избранном.")

async def real_main():
    async with app:
        print("авторизован. рассылка начата.")
        while True:
            await forward_last_message()
            await asyncio.sleep(3600)