# Credits to MetaVoid Team for making this module.

import json
import html
import requests
from NekoRobot.modules.sql import log_channel_sql as logsql
import NekoRobot.modules.mongo.chatbot_mongo as sql
from NekoRobot import AI_API_KEY as api

from time import sleep
from telegram import ParseMode
from telegram import (InlineKeyboardButton,
                      InlineKeyboardMarkup, ParseMode, Update)
from telegram.ext import (CallbackContext, CallbackQueryHandler, CommandHandler, Filters, MessageHandler)
from telegram.utils.helpers import mention_html
from NekoRobot.modules.helper_funcs.chat_status import user_admin, user_admin_no_reply
from NekoRobot import  NEKO_PTB
from NekoRobot.modules.log_channel import gloggable, loggable

bot_name = f"{NEKO_PTB.bot.first_name}"

@user_admin_no_reply
@loggable
@gloggable
def chatbot_status(update: Update, context: CallbackContext):
    query= update.callback_query
    bot = context.bot
    user = update.effective_user
    if query.data == "add_chatbot":
        chat = update.effective_chat
        is_chatbot = sql.is_chatbot(chat.id)
        if not is_chatbot:
            is_chatbot = sql.add_chatbot(chat.id)
            LOG = (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"AI_ENABLE\n"
                f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            )
            log_channel = logsql.get_chat_log_channel(chat.id)
            if log_channel:
                bot.send_message(
                log_channel,
                LOG,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )
            update.effective_message.edit_text(
                f"{bot_name} Chatbot Enabled by {mention_html(user.id, user.first_name)}.",
                parse_mode=ParseMode.HTML,
            )
            return LOG
        elif is_chatbot:
            return update.effective_message.edit_text(
                f"{bot_name} Chatbot Already Enabled.",
                parse_mode=ParseMode.HTML,
            )
        else:
            return update.effective_message.edit_text(
                "Error!",
                parse_mode=ParseMode.HTML,
            )
    elif query.data == "rem_chatbot":
        chat = update.effective_chat
        is_chatbot = sql.is_chatbot(chat.id)
        if is_chatbot:
            is_chatbot = sql.rm_chatbot(chat.id)
            LOG = (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"AI_DISABLE\n"
                f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            )
            log_channel = logsql.get_chat_log_channel(chat.id)
            if log_channel:
                bot.send_message(
                log_channel,
                LOG,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )
            update.effective_message.edit_text(
                f"{bot_name} Chatbot disabled by {mention_html(user.id, user.first_name)}.",
                parse_mode=ParseMode.HTML,
            )
            return LOG
        elif not is_chatbot:
            return update.effective_message.edit_text(
                f"{bot_name} Chatbot Already Disabled.",
                parse_mode=ParseMode.HTML,
            )
        else:
            return update.effective_message.edit_text(
                "Error!",
                parse_mode=ParseMode.HTML,
            )

@user_admin
@loggable
def chatbot(update: Update, context: CallbackContext):
    message = update.effective_message
    msg = "Choose an option"
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text="Enable",
            callback_data=r"add_chatbot")],
       [
        InlineKeyboardButton(
            text="Disable",
            callback_data=r"rem_chatbot")]])
    message.reply_text(
        msg,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )

def bot_message(context: CallbackContext, message):
    reply_message = message.reply_to_message
    if reply_message:
        if reply_message.from_user.id == context.bot.get_me().id:
            return True
    else:
        return False

def chatbot_msg(update: Update, context: CallbackContext):
    message = update.effective_message
    chat_id = update.effective_chat.id
    bot = context.bot
    is_chatbot = sql.is_chatbot(chat_id)
    if not is_chatbot:
        return
	
    if message.text and not message.document:
        if not bot_message(context, message):
            return
        Message = message.text
        bot.send_chat_action(chat_id, action="typing")
        chatbot = requests.get('https://kora-api.vercel.app/chatbot/2d94e37d-937f-4d28-9196-bd5552cac68b/hinatabot/Anonymous/message={message.text' + api + '&message=' + Message)
        Chat = json.loads(chatbot.text)
        Chat = Chat['reply']
        sleep(0.3)
        message.reply_text(Chat, timeout=60)

CHATBOTK_HANDLER = CommandHandler("chatbot", chatbot, run_async = True)
ADD_CHAT_HANDLER = CallbackQueryHandler(chatbot_status, pattern=r"add_chatbot", run_async = True)
RM_CHAT_HANDLER = CallbackQueryHandler(chatbot_status, pattern=r"rem_chatbot", run_async = True)
CHATBOT_HANDLER = MessageHandler(
    Filters.text & (~Filters.regex(r"^#[^\s]+") & ~Filters.regex(r"^!")
                    & ~Filters.regex(r"^\/")), chatbot_msg, run_async = True)

NEKO_PTB.add_handler(ADD_CHAT_HANDLER)
NEKO_PTB.add_handler(CHATBOTK_HANDLER)
NEKO_PTB.add_handler(RM_CHAT_HANDLER)
NEKO_PTB.add_handler(CHATBOT_HANDLER)

__handlers__ = [
    ADD_CHAT_HANDLER,
    CHATBOTK_HANDLER,
    RM_CHAT_HANDLER,
    CHATBOT_HANDLER,
]

