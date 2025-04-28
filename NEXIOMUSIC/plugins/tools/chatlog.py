import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import LOGGER_ID as LOG_GROUP_ID
from NEXIOMUSIC import app 
from pyrogram.errors import RPCError
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, aiohttp
from pathlib import Path
from pyrogram.enums import ParseMode

NEXIOPIC = [
"https://graph.org/file/e509753cf069de86e52f8.jpg",
"https://graph.org/file/babb71b593f36549218ce.jpg",
"https://graph.org/file/4a254d425fb4bf09b7470.jpg",
"https://graph.org/file/51f37e3c2d4aaff5cf80e.jpg",
"https://graph.org/file/df01978f91c14b16292f1.jpg",
"https://graph.org/file/a6e3e9d54c8b2e01787b6.jpg",
"https://graph.org/file/49bcbc23be713fbe06bac.jpg",
"https://graph.org/file/809651f9be99ee2bf76ab.jpg",
"https://graph.org/file/134c9f52f4ba0f7691cd1.jpg",
"https://graph.org/file/4b5c2174d7f38b4b4abd7.jpg",
"https://graph.org/file/80feff5bb4a03cf331945.jpg",
"https://graph.org/file/0379defeb51910065beac.jpg",
"https://graph.org/file/323b07bccd5e5e1f81f61.jpg",
"https://graph.org/file/cbe5c31b9ea5220b17969.jpg",
"https://graph.org/file/1a4e7071b3e64c620e003.jpg",
"https://graph.org/file/d37dd94135f355f9b6866.jpg",
]

@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    try:
        link = await app.export_chat_invite_link(chat.id)
    except Exception:
        link = None

    for member in message.new_chat_members:
        if member.id == app.id:
            count = await app.get_chat_members_count(chat.id)
            me = await app.get_me()
            bot_name = me.first_name

            msg = (
                f"<b>❖ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ #ɴᴇᴡ_ɢʀᴏᴜᴘ ❖</b>\n\n"
                f"<b>❍ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➠</b> {chat.title}\n"
                f"<b>❍ ɢʀᴏᴜᴘ ɪᴅ ➠</b> {chat.id}\n"
                f"<b>❍ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ➠</b> @{chat.username if chat.username else 'None'}\n"
                f"<b>❍ ɢʀᴏᴜᴘ ʟɪɴᴋ ➠</b> {link or 'No Link (Bot not admin)'}\n"
                f"<b>❍ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ➠</b> {count}\n\n"
                f"<b>❖ ᴀᴅᴅᴇᴅ ʙʏ ➠</b> {message.from_user.mention}"
            )
            keyboard = None
            if link:
                keyboard = InlineKeyboardMarkup([
                    [InlineKeyboardButton(f"sᴇᴇ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɢʀᴏᴜᴘ", url=link)]
                ])
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(NEXIOPIC), caption=msg, reply_markup=keyboard)

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        chat_id = message.chat.id
        me = await app.get_me()
        bot_name = me.first_name
        left = f"<b>❖ #ʟᴇғᴛ_ɢʀᴏᴜᴘ ᴀ ɢʀᴏᴜᴘ ❖</b>\n\n<b>❍ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➠</b> {title}\n\n<b>❍ ɢʀᴏᴜᴘ ɪᴅ ➠</b> {chat_id}\n\n<b>❍ ʙᴏᴛ ʀᴇᴍᴏᴠᴇᴅ ʙʏ ➠</b> {remove_by}\n\n<b>❖ ʙᴏᴛ ɴᴀᴍᴇ ➠</b> {bot_name}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(NEXIOPIC), caption=left)
