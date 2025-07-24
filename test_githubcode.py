from pyrogram import Client
import asyncio

SOURCE_CHAT_ID = "me"
TARGET_CHAT_ID = -1001984966725

# Замените этот ID на Telegram ID разрешённого пользователя
ALLOWED_USER_ID = 123456789  # ← Узнай через @userinfobot

print("Авторизация через Телеграм. Надо ввести данные. Создал @KingOfInsanity")
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
                print("✅ Сообщение переслано.")
            except Exception as e:
                print("❌ Ошибка пересылки:", e)
        else:
            print("❌ Нет сообщений в избранном.")

async def real_main():
    async with app:
        me = await app.get_me()
        if me.id != ALLOWED_USER_ID:
            print("❌ У вас нет прав на использование этой программы.")
            return  # Не запускать рассылку

        print(f"✅ Авторизован как @{me.username}. Рассылка начата.")
        while True:
            await forward_last_message()
            await asyncio.sleep(3600)

asyncio.run(real_main())
