
from pyrogram import Client, filters
import os

API_ID = 21157143
API_HASH = "e141697e7aa2c2232f7ceeb7eea2b210"
BOT_TOKEN = "8120283130:AAHZs97OxhYC97vOBxcR4-1xqGWNPT9oq68"

app = Client("MovieBhaiClone", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.document | filters.video | filters.audio)
async def gen_link(client, message):
    file = message.reply_to_message or message
    username = (await client.get_me()).username
    link = f"https://t.me/{username}?start={file.message_id}"
    await message.reply_text(f"✅ Download Link Generated:

🔗 {link}")

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    if len(message.command) > 1:
        msg_id = int(message.command[1])
        try:
            await client.copy_message(
                chat_id=message.chat.id,
                from_chat_id=message.chat.id,
                message_id=msg_id
            )
        except Exception as e:
            await message.reply_text("⚠️ File not found.")
    else:
        await message.reply_text("👋 Send me a file and I'll give you a download link.")

app.run()
