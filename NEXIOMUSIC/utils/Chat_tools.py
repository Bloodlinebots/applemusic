# utils/chat_tools.py

from pyrogram import Client
from pyrogram.errors import ChatAdminRequired, PeerIdInvalid, RPCError
import logging

logger = logging.getLogger(__name__)

async def check_bot_admin(app: Client, chat_id: int) -> tuple:
    """
    Check if the bot is admin and has required permissions.

    Returns:
        (bool, str) -> (Is_Admin, Reason/Message)
    """
    try:
        chat_member = await app.get_chat_member(chat_id, "me")

        if chat_member.status not in ["administrator", "creator"]:
            return False, "Bot is not an admin in this chat."

        privileges = chat_member.privileges
        if privileges is None:
            return False, "Bot is admin but cannot fetch privileges."

        if not privileges.invite_users:
            return False, "Bot is admin but missing 'Invite Users' permission."

        return True, "Bot has required permissions."

    except ChatAdminRequired:
        return False, "Bot needs to be admin to perform this action."
    except PeerIdInvalid:
        return False, "Invalid chat ID provided."
    except Exception as e:
        logger.error(f"Error checking admin rights: {e}")
        return False, f"Unexpected error: {str(e)}"


async def get_invite_link(app: Client, chat_id: int) -> str:
    """
    Export a permanent invite link for the chat.

    Returns:
        str -> Invite link or error message.
    """
    is_admin, reason = await check_bot_admin(app, chat_id)

    if not is_admin:
        return f"❌ {reason}"

    try:
        invite_link = await app.export_chat_invite_link(chat_id)
        return f"✅ Invite Link: {invite_link}"

    except ChatAdminRequired:
        return "❌ Bot lost admin rights before exporting invite link."
    except PeerIdInvalid:
        return "❌ Invalid chat ID."
    except RPCError as e:
        logger.error(f"Telegram RPC Error: {e}")
        return f"❌ Telegram RPC Error: {str(e)}"
    except Exception as e:
        logger.error(f"Unexpected error during invite link export: {e}")
        return f"❌ Unexpected error: {str(e)}"
