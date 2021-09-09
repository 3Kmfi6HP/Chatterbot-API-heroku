from telethon.sync import TelegramClient
from telethon.sessions import StringSession
api_id = 2890925
api_hash = '688f2cb389b367b22ce08844318aacbd'
with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())