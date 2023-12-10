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


@TeluguZone.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_photo(
        photo="https://graph.org/file/3dc0d36c2bab91936a26b.jpg",
        caption="This Is A Advanced @Daemon990 Bot")


                         




print("Bot was Started")

TeluguZone.run()
  
