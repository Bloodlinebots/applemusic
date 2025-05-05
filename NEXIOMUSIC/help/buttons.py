from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

import config
from NEXIOMUSIC import app

class BUTTONS(object):
    MBUTTON = [
        [
            InlineKeyboardButton("˹⎯፝֟፝֟⎯꯭᪵ ⃪ѕα͟ηα͟т͟α͟ηⷽιⷨ͟ 𝆺꯭𝅥⎯꯭🚩", url="https://t.me/ll_RADHE7_ll")
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
    
    SBUTTON = [
 
        [
            InlineKeyboardButton("ʙᴏᴛᴍɪɴᴇ-ᴛᴇᴄʜ", url="https://t.me/BOTMINE_TECH"),
        ],
        [
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/BOTMINE_SUPPORT"),
            InlineKeyboardButton(" ᴜᴘᴅᴀᴛᴇ", url="https://t.me/UR_RISHU_143"),
        ],
        [
            InlineKeyboardButton("ᴄʜᴧᴛ ɢᴄ", url="https://t.me/TheFriendsHeaven"),
            InlineKeyboardButton("ʀɪsʜυ ᴀᴘɪ", url="https://t.me/Rishuapi"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
    
    ABUTTON = [
        [
            InlineKeyboardButton("ʜєʟᴘ | ɪηғσ", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton("ʙᴧsɪᴄ ɢυɪᴅє", callback_data="ABOUT_BACK HELP_GUIDE"),
            InlineKeyboardButton("ᴅσηᴧᴛє", callback_data="ABOUT_BACK HELP_DONATE"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
