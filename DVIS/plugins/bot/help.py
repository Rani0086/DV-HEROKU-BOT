from pyrogram import filters

from DVIS import app


@app.on_message(filters.command(["help"]))
async def start(client, message):
    await message.reply_text(
        f"Hello there! I am heroku control bot\n\nCheck hosted apps: /myhost, /heroku."
    )