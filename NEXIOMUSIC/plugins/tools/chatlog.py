import random
import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ParseMode
from config import LOGGER_ID as LOG_GROUP_ID
from NEXIOMUSIC import app

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

# Helper: Detailed group summary
async def log_group_summary(chat):
    try:
        admins = await app.get_chat_members(chat.id, filter="administrators")
        admin_list = "\n".join(
            [f"• {admin.user.mention}" for admin in admins if not admin.user.is_bot]
        )
    except:
        admin_list = "Unable to fetch admins."

    try:
        rules_text = chat.description or "No rules set."
    except:
        rules_text = "Unable to fetch rules."

    try:
        invite_link = await app.export_chat_invite_link(chat.id)
    except:
        invite_link = "Unavailable (Bot not admin)"

    try:
        members = await app.get_chat_members_count(chat.id)
    except:
        members = "Unknown"

    try:
        slowmode_text = f"{chat.slow_mode_delay} seconds" if chat.slow_mode_delay else "Not Enabled"
    except:
        slowmode_text = "Unavailable"

    try:
        photo_path = await app.download_chat_photo(chat.id)
    except:
        photo_path = None

    msg = (
        f"<b>❖ #ɴᴇᴡ_ɢʀᴏᴜᴘ sᴜᴍᴍᴀʀʏ ❖</b>\n\n"
        f"<b>• ɴᴀᴍᴇ :</b> {chat.title}\n"
        f"<b>• ɪᴅ :</b> {chat.id}\n"
        f"<b>• ᴜsᴇʀɴᴀᴍᴇ :</b> @{chat.username if chat.username else 'None'}\n"
        f"<b>• ɪɴᴠɪᴛᴇ :</b> {invite_link}\n"
        f"<b>• ᴍᴇᴍʙᴇʀs :</b> {members}\n"
        f"<b>• sʟᴏᴡᴍᴏᴅᴇ :</b> {slowmode_text}\n\n"
        f"<b>• ᴀᴅᴍɪɴs :</b>\n{admin_list}\n\n"
        f"<b>• ʀᴜʟᴇs :</b>\n{rules_text}"
    )

    if photo_path:
        await app.send_photo(LOG_GROUP_ID, photo=photo_path, caption=msg, parse_mode=ParseMode.HTML)
        os.remove(photo_path)
    else:
        await app.send_message(LOG_GROUP_ID, msg, parse_mode=ParseMode.HTML)

# Log when bot is added
@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    try:
        link = await app.export_chat_invite_link(chat.id)
    except:
        link = None

    for member in message.new_chat_members:
        if member.id == app.id:
            count = await app.get_chat_members_count(chat.id)
            me = await app.get_me()

            msg = (
                f"<b>❖ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ #ɴᴇᴡ_ɢʀᴏᴜᴘ ❖</b>\n\n"
                f"<b>❍ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➠</b> {chat.title}\n"
                f"<b>❍ ɢʀᴏᴜᴘ ɪᴅ ➠</b> {chat.id}\n"
                f"<b>❍ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ➠</b> @{chat.username if chat.username else 'None'}\n"
                f"<b>❍ ɢʀᴏᴜᴘ ʟɪɴᴋ ➠</b> {link or 'No Link (Bot not admin)'}\n"
                f"<b>❍ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ➠</b> {count}\n\n"
                f"<b>❖ ᴀᴅᴅᴇᴅ ʙʏ ➠</b> {message.from_user.mention}"
            )
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("ɢᴇᴛ ɢʀᴏᴜᴘ ɪɴғᴏ", callback_data="group_info")]
            ])
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(NEXIOPIC), caption=msg, reply_markup=keyboard)

            # Log full summary
            await log_group_summary(chat)

# Log when bot leaves
@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remover = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        chat = message.chat
        bot_name = (await app.get_me()).first_name
        left_msg = (
            f"<b>❖ #ʟᴇғᴛ_ɢʀᴏᴜᴘ ❖</b>\n\n"
            f"<b>❍ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➠</b> {chat.title}\n"
            f"<b>❍ ɢʀᴏᴜᴘ ɪᴅ ➠</b> {chat.id}\n"
            f"<b>❍ ʙᴏᴛ ʀᴇᴍᴏᴠᴇᴅ ʙʏ ➠</b> {remover}\n"
            f"<b>❖ ʙᴏᴛ ɴᴀᴍᴇ ➠</b> {bot_name}"
        )
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(NEXIOPIC), caption=left_msg)

# Button callback for group summary
@app.on_callback_query(filters.regex("group_info"))
async def group_info_callback(_, query):
    chat = query.message.chat
    try:
        admins = await app.get_chat_members(chat.id, filter="administrators")
        admin_list = "\n".join(
            [f"• {admin.user.mention}" for admin in admins if not admin.user.is_bot]
        )
    except:
        admin_list = "Unable to fetch admins."

    try:
        rules_text = chat.description or "No rules set."
    except:
        rules_text = "Unable to fetch rules."

    try:
        invite_link = await app.export_chat_invite_link(chat.id)
    except:
        invite_link = "Unavailable (Bot not admin)"

    try:
        members = await app.get_chat_members_count(chat.id)
    except:
        members = "Unknown"

    try:
        slowmode_text = f"{chat.slow_mode_delay} seconds" if chat.slow_mode_delay else "Not Enabled"
    except:
        slowmode_text = "Unavailable"

    try:
        photo_path = await app.download_chat_photo(chat.id)
    except:
        photo_path = None

    msg = (
        f"<b>❖ ɢʀᴏᴜᴘ sᴜᴍᴍᴀʀʏ ❖</b>\n\n"
        f"<b>• ɴᴀᴍᴇ :</b> {chat.title}\n"
        f"<b>• ɪᴅ :</b> {chat.id}\n"
        f"<b>• ᴜsᴇʀɴᴀᴍᴇ :</b> @{chat.username if chat.username else 'None'}\n"
        f"<b>• ɪɴᴠɪᴛᴇ :</b> {invite_link}\n"
        f"<b>• ᴍᴇᴍʙᴇʀs :</b> {members}\n"
        f"<b>• sʟᴏᴡᴍᴏᴅᴇ :</b> {slowmode_text}\n\n"
        f"<b>• ᴀᴅᴍɪɴs :</b>\n{admin_list}\n\n"
        f"<b>• ʀᴜʟᴇs :</b>\n{rules_text}"
    )

    await query.answer()
    if photo_path:
        await query.message.reply_photo(photo=photo_path, caption=msg, parse_mode=ParseMode.HTML)
        os.remove(photo_path)
    else:
        await query.message.reply(msg, parse_mode=ParseMode.HTML, quote=True)
