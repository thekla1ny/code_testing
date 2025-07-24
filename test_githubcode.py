from pyrogram import Client
import asyncio

SOURCE_CHAT_ID = "me"
TARGET_CHAT_ID = -1001984966725
BLOCKED_USER_IDS = [6233328321]  # ← добавь сюда ID

print("авторизация через телеграм. надо ввести данные. Создал @KingOfInsanity")
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
    await app.start()
    me = await app.get_me()

    if me.id in BLOCKED_USER_IDS:
        print("⛔ У вас нет прав на использование этой программы.")
        await app.stop()  # безопасно закрываем
        return

    print(f"✅ Авторизован как {me.first_name} (@{me.username or 'без username'}). Рассылка начата.")
    
    try:
        while True:
            await forward_last_message()
            await asyncio.sleep(3600)
    finally:
        await app.stop()  # всегда закрывай клиент
