from pyrogram import Client
import asyncio

# Константы
SOURCE_CHAT_ID = "me"
TARGET_CHAT_ID = -1001984966725
WHITELIST = [654645645]  # Вставь свой Telegram ID сюда

print("авторизация через телеграм. надо ввести данные. Создал @KingOfInsanity")
api_id = int(input("Введи свой API ID: "))
api_hash = input("Введи свой API HASH: ")
session_name = "akkaunt_data"

# Функция проверки доступа
async def get_user_id():
    async with Client(session_name, api_id=api_id, api_hash=api_hash) as app:
        user = await app.get_me()
        print(f"Проверка...")
        return user.id

# Основная логика пересылки
async def run_forwarder():
    async with Client(session_name, api_id=api_id, api_hash=api_hash) as app:
        print("✅ Авторизован. Рассылка начата.")
        while True:
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
            await asyncio.sleep(3600)

# Основной запуск
async def main():
    user_id = await get_user_id()

    if user_id not in WHITELIST:
        print("❌ У вас нет прав на использование программы.")
    else:
        await run_forwarder()

if __name__ == "__main__":
    asyncio.run(main())
