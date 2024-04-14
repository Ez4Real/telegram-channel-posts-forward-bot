import os
import re
import asyncio
from dotenv import load_dotenv
from telethon.sync import TelegramClient, events


load_dotenv('.env')


SOURCE_ENTITY_ID = int(os.getenv('SOURCE_ENTITY_ID'))
DESTINATION_ENTITY_ID = int(os.getenv('DESTINATION_ENTITY_ID'))

# API credentials
API_ID = os.getenv('APP_API_ID')
API_HASH = os.getenv('APP_API_HASH')
SESSION_FILE = 'telegram-session.session'


def format_signal_message(message):
    # Define regular expressions to extract relevant information
    signal_type_regex = r'BUY|SELL'
    currency_pair_regex = r'[A-Z]+/[A-Z]+'
    entry_price_regex = r'Entry price\s+([\d.]+)\s*/\s*'
    tp_regex = r'TP\d\s*:\s*([\d.]+)'
    sl_regex = r'SL\s+([\d.]+)'

    # Extract information from the message using regular expressions
    signal_type = re.search(signal_type_regex, message).group()
    currency_pair = re.search(currency_pair_regex, message).group()
    entry_price = re.search(entry_price_regex, message).group(1)
    tp_prices = re.findall(tp_regex, message)
    sl_price = re.search(sl_regex, message).group(1)

    # Construct the formatted output
    formatted_message = f"🔔🔔🔔 NEW SIGNAL 🔔🔔🔔\n\n"
    formatted_message += f"{currency_pair} {signal_type}\n\n"
    formatted_message += f"Entry: {entry_price}\n"
    formatted_message += f"Stop loss: {sl_price}\n"
    for i, tp_price in enumerate(tp_prices, start=1):
        formatted_message += f"Take Profit {i}: {tp_price}\n"
    formatted_message += "\n"
    formatted_message += "Please respect your lot size ⚠️⚠️⚠️"
    
    return formatted_message


async def main():
    async with TelegramClient(SESSION_FILE, API_ID, API_HASH) as client:
        await client.start()

        @client.on(events.NewMessage(chats=[SOURCE_ENTITY_ID]))
        async def handle_new_message(event):
            message = event.message
            formatted_msg = format_signal_message(message.text)
            
            print(message.text)
            print()
            print(formatted_msg)
            
            await client.send_message(DESTINATION_ENTITY_ID, formatted_msg)

        await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())