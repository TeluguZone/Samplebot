from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton 


API_ID = "24830912"
API_HASH = "a1a1775593531b90850b8b82e3b14940"
BOT_TOKEN = "6433293774:AAGRhgl7a9Oi9XhbZnKE_yzTqc8n1KsymZY"

TeluguZone = Client(
    name="Samplebot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

START_BUTTONS = [[
    InlineKeyboardButton("JOIN MY UPDATES CHANNEL", url="hhtps://t.me/TeluguZone0")
]]
   


@TeluguZone.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text(
        text="You Have To Join My Channel To Use Me",
        reply_markup=InlineKeyboardMarkup(START_BUTTONS) 
    )

print("Bot was Started")

TeluguZone.run()
  
