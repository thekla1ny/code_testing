from pyrogram import Client
import asyncio

# Константы
SOURCE_CHAT_ID = "me"

# Список чатов для рассылки
TARGET_CHAT_IDS = [
    -1002473605725,
    -1002361289229,
    -1002318593167,
    -1002311406040,
    -1002329838424,
    -1001984966725,
    -1001996734240,
    -1002391093375,
    -1002491340826,
    -1002037962968,
    -1002475503071,
    -1002327591798,
    -1002395514384
]

WHITELIST = [7412272825, 5436806218, 7579684665, 6233328321]  

print("авторизация через телеграм. надо ввести данные. Создал @KingOfInsanity. версия 2")
api_id = int(input("Введи свой API ID: "))
api_hash = input("Введи свой API HASH: ")
session_name = "akkaunt_data"


# Проверка ID пользователя
async def get_user_id():
    async with Client(session_name, api_id=api_id, api_hash=api_hash) as app:
        user = await app.get_me()
        print(f"👤 Ваш Telegram ID: {user.id}")
        return user.id


# Основная логика пересылки
async def run_forwarder():
    async with Client(session_name, api_id=api_id, api_hash=api_hash) as app:
        print("✅ Авторизован. Рассылка начата.")
        while True:
            async for message in app.get_chat_history(SOURCE_CHAT_ID, limit=1):
                if message:
                    for target_id in TARGET_CHAT_IDS:
                        try:
                            await app.forward_messages(
                                chat_id=target_id,
                                from_chat_id=SOURCE_CHAT_ID,
                                message_ids=message.id
                            )
                            print(f"📤 Сообщение переслано в {target_id}.")
                        except Exception as e:
                            print(f"❌ Ошибка пересылки в {target_id}: {e}")
                else:
                    print("ℹ️ Нет сообщений в избранном.")
            await asyncio.sleep(3600)  # ждем 1 час


# Главная функция
async def main():
    user_id = await get_user_id()

    if user_id not in WHITELIST:
        print("❌ У вас нет прав на использование программы.")
        while True:
            await asyncio.sleep(3600)  # Висим, не закрываемся
    else:
        await run_forwarder()


# Запуск
if __name__ == "__main__":
    asyncio.run(main())

