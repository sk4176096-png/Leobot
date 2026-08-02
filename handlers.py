import logging
from datetime import datetime

from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes

from ai import generate_ai_response
from database import db

logger = logging.getLogger(__name__)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await db.register_user(
        str(user.id),
        user.username or user.first_name
    )

    text = f"""
👋 Hello {user.first_name}!

🤖 Main *Leo AI Assistant* hoon.

Bas mujhe koi bhi message bhejo aur main reply dunga.

Commands:
/start - Start Bot
/help - Help
/stats - Statistics
"""

    await update.message.reply_text(text)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🤖 Leo AI Assistant Help

• Mujhe koi bhi question pucho.
• Hindi, Hinglish aur English support.
• Main pichhli chats yaad rakhta hoon.
"""

    await update.message.reply_text(text)


async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    users = await db.users.count_documents({})
    chats = await db.messages.count_documents({})

    text = f"""
📊 Bot Statistics

👤 Users : {users}
💬 Messages : {chats}

Status : Online ✅
"""

    await update.message.reply_text(text)


async def persona_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🎭 Persona feature coming soon..."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message:
        return

    if not update.message.text:
        return

    user = update.effective_user

    user_id = str(user.id)

    prompt = update.message.text

    await db.register_user(
        user_id,
        user.username or user.first_name
    )

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING
    )

    try:

        reply = await generate_ai_response(
            prompt=prompt,
            user_id=user_id
        )

        await update.message.reply_text(reply)

    except Exception as e:

        logger.exception(e)

        await update.message.reply_text(
            "❌ Sorry, kuch error aa gaya."
        )