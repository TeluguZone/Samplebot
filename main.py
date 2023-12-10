from pyrogram import Client,filters


API_ID = "24830912"
API_HASH = "a1a1775593531b90850b8b82e3b14940"
BOT_TOKEN = "6433293774:AAGRhgl7a9Oi9XhbZnKE_yzTqc8n1KsymZY"

TeluguZone = Client(
    name="Samplebot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@Client.on_message(filters.command("start"))
async def start_cmd(_, message):
    await message.reply_text("This Is A Advanced daemon Bot")                             


@TeluguZone.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_text("Contact my father my father @Daemon90")                            


print("Bot was Started")

TeluguZone.run()
  
