import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.exceptions import GroupCallNotFoundError

from config import API_ID, API_HASH, STRING_SESSION, AUTO_LEAVE_TIME

app = Client(name="assistant", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)
call = PyTgCalls(app)

async def leave_empty_groups():
    await app.start()
    await call.start()
    print("Assistant and PyTgCalls started with auto leave.")

    while True:
        left_count = 0
        async for dialog in app.get_dialogs():
            if dialog.chat.type in ["supergroup", "group"]:
                try:
                    members = await app.get_chat_members(dialog.chat.id)
                    if len(members) <= 1:
                        await app.leave_chat(dialog.chat.id)
                        print(f"Left empty group: {dialog.chat.title} ({dialog.chat.id})")
                        left_count += 1
                except Exception as e:
                    print(f"Error checking group {dialog.chat.id}: {e}")

        if left_count == 0:
            print("No empty groups found.")

        await asyncio.sleep(AUTO_LEAVE_TIME * 60)  # X मिनट wait

if __name__ == "__main__":
    asyncio.run(leave_empty_groups())
