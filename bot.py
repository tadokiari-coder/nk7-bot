from pyrogram import Client, filters
from pyrogram.types import ChatPrivileges
import asyncio

api_id = 38017821
api_hash = "a6922e6f14cd2ccb1003814d7f7bf469"
bot_token = "8693494918:AAGJXGnqhqj8V3fD3CSmERqph6aPtefFeFY"

app = Client(
    "admin_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

# LIBERAR TEMPORARIAMENTE
@app.on_message(filters.command("liberar"))
async def liberar(client, message):

    if len(message.command) < 3:
        await message.reply(
            "Use: /liberar @usuario minutos"
        )
        return

    username = message.command[1].replace("@", "")
    minutos = int(message.command[2])

    chat_id = message.chat.id

    try:
        user = await client.get_users(username)

        # Adiciona admin limitado
        await client.promote_chat_member(
            chat_id,
            user.id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=False,
                can_manage_video_chats=False,
                can_restrict_members=False,
                can_invite_users=False,
                can_pin_messages=False,
                can_promote_members=False,
                can_change_info=False,
                can_post_messages=False,
                can_edit_messages=False,
                is_anonymous=False
            )
        )

        # Define etiqueta
        await client.set_administrator_title(
            chat_id,
            user.id,
            "Acesso Liberado"
        )

        # Mensagem de acesso
        await message.reply(
            f"✅ | ACESSO LIBERADO\n\n"
            f"👤 Usuário: {user.mention}\n"
            f"⏳ Tempo liberado: {minutos} minuto(s)\n"
            f"🏷 Cargo: Acesso Liberado\n\n"
            f"📌 Utilize seu acesso com responsabilidade.\n"
            f"⚠️ Após o tempo acabar, o acesso será removido automaticamente.\n\n"
            f"🔥 NK7 Security System"
        )

        # Espera o tempo acabar
        await asyncio.sleep(minutos * 60)

        # Remove admin corretamente
        await client.promote_chat_member(
            chat_id,
            user.id,
            privileges=ChatPrivileges(
                can_manage_chat=False,
                can_delete_messages=False,
                can_manage_video_chats=False,
                can_restrict_members=False,
                can_invite_users=False,
                can_pin_messages=False,
                can_promote_members=False,
                can_change_info=False,
                can_post_messages=False,
                can_edit_messages=False,
                is_anonymous=False
            )
        )

        # Mensagem de expiração
        await client.send_message(
            chat_id,
            f"❌ | ACESSO EXPIRADO\n\n"
            f"👤 Usuário: @{username}\n"
            f"🏷 Cargo atual: Sem Acesso\n\n"
            f"⛔ O tempo de utilização terminou.\n"
            f"🔒 O acesso foi removido automaticamente.\n\n"
            f"🔥 NK7 Security System"
        )

    except Exception as e:
        await message.reply(str(e))

app.run()
      
