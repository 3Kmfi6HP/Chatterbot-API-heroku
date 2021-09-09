from requests import post as p
from chatterbotAPI import PORT, config
#from chatterbotAPI import PORT, config
import time
import re
from os import environ
import logging
import json, requests
logging.basicConfig(filename='example.log',level=logging.CRITICAL)
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# sample API_ID from https://github.com/telegramdesktop/tdesktop/blob/f98fdeab3fb2ba6f55daf8481595f879729d1b84/Telegram/SourceFiles/config.h#L220
# or use your own
api_id = 2890925
api_hash = '688f2cb389b367b22ce08844318aacbd'
list_chat_id=[-1001514262324,-1001268770001,-1001174963531,-1001366956442,-1001213526515,-1001150986618,-1001348077844,-1001441167695,-1001321370633]
#list_chat_id=[-1001514262324,-1001268770001]
read_event = {}
# fill in your own details here
phone = 'phone'
session_string = environ.get('SESSION', None)  # use your username if unsure
password = 'YOUR_PASSWORD'  # if you have two-step verification enabled
#trainer.export_for_training('./my_export.json')

if __name__ == '__main__':
    # Create the client and connect
    # use sequential_updates=True to respond to messages one at a time
    client = TelegramClient(StringSession(session_string), api_id, api_hash)
    async def chatbot_group(event):
        from_ = await event.client.get_entity(event.from_id)
        meid = await client.get_peer_id('me')
        # Know reply msg who are sender
        replied = await event.get_reply_message()
        sender = replied.sender_id
        match = (((meid == sender) and re.compile(r'(.|\n)*').search(event.raw_text)) and 1 <= len(event.raw_text) <= 35) and not from_.is_self
        for y in list_chat_id:
            if not from_.bot and (event.message.chat_id==y and match):
                try:
                    chat_from = event.chat if event.chat else (await event.get_chat())  # telegram MAY not send the chat enity
                    chat_title = chat_from.title
                    raw_text = event.message.message
                    req_data = requests.get(f'http://0.0.0.0:{PORT}/?query={raw_text}')
                    req_data = json.loads(req_data.text)
                    req_data = req_data['response']['bot']
                    time_taken = req_data['response']['time_taken']
                    print("-------------------------------")
                    print(time.asctime(), '-', chat_title)
                    print("message:", event.message.message)
                    print("response:", req_data)
                    print("time", time_taken)
                    
                except:
                    continue
            elif (1 <= len(event.raw_text) <= 35 and re.compile(u'[\u4e00-\u9fa5]+').search(event.raw_text)) and event.message.chat_id==y:
                try:
                    chat_from = event.chat if event.chat else (await event.get_chat())  # telegram MAY not send the chat enity
                    chat_title = chat_from.title
                    raw_text = event.message.message
                    req_data = requests.get(f'http://0.0.0.0:{PORT}/?query={raw_text}')
                    req_data = json.loads(req_data.text)
                    req_data = req_data['response']['bot']
                    time_taken = req_data['response']['time_taken']
                    print("-------------------------------")
                    print(time.asctime(), '-', chat_title)
                    print("message:", event.message.message)
                    print("response:", req_data)
                    print("time", time_taken)
                except:
                    continue

    async def chatbot_private(event):
        match = (re.compile(r'(.|\n)*').search(event.raw_text) and event.message.from_id.user_id in [859046909,777000]) and 1 <= len(event.raw_text) <= 35
        if match:
                try:
                    raw_text = event.message.message
                    req_data = requests.get(f'http://0.0.0.0:{PORT}/?query={raw_text}')
                    req_data = json.loads(req_data.text)
                    req_data = req_data['response']['bot']
                    time_taken = req_data['response']['time_taken']
                    print(time.asctime(), '-', event.message.message)  # optionally log time and message
                    print("-----------------------------------------")
                    print("message:", event.message.message)
                    print("response:", req_data)
                    print("time", time_taken)
                except:
                    pass
                
    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        global read_event
        from_ = await event.client.get_entity(event.from_id)  # this lookup will be cached by telethon
        if event.is_private:  # only auto-reply to private chats
            if(event.chat_id, event.id) in read_event:
                return
            read_event[(event.chat_id, event.id)] = True
            if not from_.bot:  # don't auto-reply to bots
                await chatbot_private(event)
        elif event.is_group:
            if(event.chat_id, event.id) in read_event:
                return
            read_event[(event.chat_id, event.id)] = True
            await chatbot_group(event)

    print(time.asctime(), '-', 'Bot-Running...')
    client.start()
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')
