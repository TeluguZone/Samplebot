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
    print("START Command")


@TeluguZone.on_message(filters.command("help"))
async def help_cmd(client, message):
    print("HELP Command")


print("Bot was Started")

TeluguZone.run()
  
