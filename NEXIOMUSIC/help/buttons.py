from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

import config
from NEXIOMUSIC import app

class BUTTONS(object):
    MBUTTON = [
        [
            InlineKeyboardButton("˹ᯓ𓆰𝅃꯭᳚ ⃪ ꯭꯭꯭꯭꯭꯭꯭꯭꯭꯭᪵᪳༎ ꯭⁢⁣⁤⁣⁣⁢⁣⁤⁢⁤⁣⁢⁤⁣⁤᪳᪳🇷꯭ ꯭𝐈‌𝛅꯭꯭ʜ꯭֟፝︢︣𝛖꯭ ꯭꯭🚩𝆺꯭𝅥༎ࠫ𐏓꯭ 𝅃 ˼", url="https://t.me/rishu1286")
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
    
    SBUTTON = [
 
        [
            InlineKeyboardButton("ʀɪsʜυ ", url="https://t.me/ur_rishu_143"),
        ],
        [
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/ur_support07"),
            InlineKeyboardButton(" ᴜᴘᴅᴀᴛᴇ", url="https://t.me/vip_robotz"),
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
