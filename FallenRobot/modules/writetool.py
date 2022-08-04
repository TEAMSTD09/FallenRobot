import requests
from requests import get
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from FallenRobot import pbot as fallen, BOT_NAME, BOT_USERNAME, SUPPORT_CHAT


@fallen.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if not message.reply_to_message:
        text = message.text.split(None, 1)[1]
        m = await fallen.send_message(
            message.chat.id, "`Please wait...,\n\nWriting your text...`"
        )
        API = "https://api.sdbots.tk/write"
        body = {"text": f"{text}"}
        req = requests.post(
            API, headers={"Content-Type": "application/json"}, json=body
        )
        photo = req.history[1].url
        caption = f"""
Successfully Written Text 💘

✨ **Written By :** [{BOT_NAME}](https://t.me/{BOT_USERNAME})
🥀 **Requested by :** {message.from_user.mention}
❄ **Link :** `{photo}`
"""
        await m.delete()
        await fallen.send_photo(
            message.chat.id,
            photo=photo,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴇʟᴇɢʀᴀᴩʜ •", url=f"{photo}")]]
            ),
        )
    else:
        lol = message.reply_to_message.text
        m = await fallen.send_message(
            message.chat.id, "`Please wait...,\n\nWriting your text...`"
        )
        API = "https://api.sdbots.tk/write"
        body = {"text": f"{lol}"}
        req = requests.post(
            API, headers={"Content-Type": "application/json"}, json=body
        )
        photo = req.history[1].url
        caption = f"""
Successfully Written Text 💘

✨ **Written By :** [{BOT_NAME}](https://t.me/{BOT_USERNAME})
🥀 **Requested by :** {message.from_user.mention}
❄ **Link :** `{photo}`
"""
        await m.delete()
        await fallen.send_photo(
            message.chat.id,
            photo=photo,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴇʟᴇɢʀᴀᴩʜ •", url=f"{photo}")]]
            ),
        )


__mod_name__ = "𝚆𝚛𝚒𝚝𝚎-𝚃𝚘𝚘𝚕"

__help__ = """

 Writes the given text on white page with a pen 🖊

❍ /write <text> *:* Writes the given text.
 """
