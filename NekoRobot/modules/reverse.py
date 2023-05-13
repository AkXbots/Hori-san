import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext, CommandHandler

from NekoRobot import TOKEN, NEKO_PTB as dispatcher

url = "https://karma-reverse-api2-0.vercel.app/reverse"


def reverse(update: Update, context: CallbackContext):
    if not update.effective_message.reply_to_message:
        update.effective_message.reply_text("Ê€á´‡á´˜ÊŸÊ á´›á´ á´€ á´˜Êœá´á´›á´ á´Ê€ á´€ sá´›Éªá´„á´‹á´‡Ê€.")

    elif update.effective_message.reply_to_message.photo:
        msg = update.effective_message.reply_text("sá´‡á´€Ê€á´„ÊœÉªÉ´É¢ Ò“á´Ê€ Éªá´á´€É¢á´‡.....")

        photo_id = update.effective_message.reply_to_message.photo[-1].file_id
        get_path = requests.post(
            f"https://api.telegram.org/bot{TOKEN}/getFile?file_id={photo_id}"
        ).json()
        file_path = get_path["result"]["file_path"]
        data = {
            "imageUrl": f"https://images.google.com/searchbyimage?safe=off&sbisrc=tg&image_url=https://api.telegram.org/file/bot{TOKEN}/{file_path}"
        }

        response = requests.post(url, json=data)
        result = response.json()
        if response.ok:
            msg.edit_text(
                f"[{result['data']['resultText']}]({result['data']['similarUrl']})",
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Fixed by", url="https://t.me/king_of_ghoul")]]
                ),
            )
        else:
            update.effective_message.reply_text("Fucking…")

    elif update.effective_message.reply_to_message.sticker:
        msg = update.effective_message.reply_text("segsing.....")

        sticker_id = update.effective_message.reply_to_message.sticker.file_id
        get_path = requests.post(
            f"https://api.telegram.org/bot{TOKEN}/getFile?file_id={sticker_id}"
        ).json()
        file_path = get_path["result"]["file_path"]
        data = {
            "imageUrl": f"https://images.google.com/searchbyimage?safe=off&sbisrc=tg&image_url=https://api.telegram.org/file/bot{TOKEN}/{file_path}"
        }

        response = requests.post(url, json=data)
        result = response.json()
        if response.ok:
            msg.edit_text(
                f"[{result['data']['resultText']}]({result['data']['similarUrl']})",
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Fixed by", url="https://t.me/king_of_ghoul")]]
                ),
            )
        else:
            update.effective_message.reply_text("Fucking…")

    else:
        update.effective_message.reply_text("segsing.")


reverse_handler = CommandHandler(
    ["grs", "reverse", "pp", "p", "P"], reverse, run_async=True
)

dispatcher.add_handler(reverse_handler)
