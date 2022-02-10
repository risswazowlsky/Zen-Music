from typing import Dict, List, Union

from Yukki import BOT_ID, app


def PermissionCheck(mystic):
    async def wrapper(_, message):
        if message.chat.type == "private":
            return await mystic(_, message)
        a = await app.get_chat_member(message.chat.id, BOT_ID)
        if a.status != "administrator":
            return await message.reply_text(
                "Saya harus menjadi admin agar bisa musikan:\n"
                + "\n- **Berikan Saya Izin Mengelola VCG/OS:**"
                + "\n- **Berikan Saya Izin Menghapus Pesan:**"
                + "\n- **Berikan Saya Izin Add Admin**: Untuk Mengundang Asisten"
            )
        if not a.can_manage_voice_chats:
            await message.reply_text(
                "I don't have the required permission to perform this action."
                + "\n**Permission:** __MANAGE VOICE CHATS__"
            )
            return
        if not a.can_delete_messages:
            await message.reply_text(
                "I don't have the required permission to perform this action."
                + "\n**Permission:** __DELETE MESSAGES__"
            )
            return
        if not a.can_invite_users:
            await message.reply_text(
                "I don't have the required permission to perform this action."
                + "\n**Permission:** __INVITE USERS VIA LINK__"
            )
            return
        return await mystic(_, message)

    return wrapper
