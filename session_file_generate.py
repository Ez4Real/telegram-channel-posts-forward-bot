import os
from telethon.sync import TelegramClient
from dotenv import load_dotenv


load_dotenv('.env')

api_id = os.getenv('APP_API_ID')
api_hash = os.getenv('APP_API_HASH')

with TelegramClient('telegram-session', api_id, api_hash) as client:
    client.start()