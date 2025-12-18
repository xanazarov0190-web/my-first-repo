from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    CommandHandler,
    filters,
)

TOKEN = "8261523562:AAF0xtiStFKyTZajyXLmbpxRW7_kd3CzUl8"
ADMIN_ID = 8003105513

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum!\nSavolingizni yozing, operator tez orada javob beradi."
    )

# Xabarlar bilan ishlash
async def user_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    # Admin reply qilsa — foydalanuvchiga yuboriladi
    if msg.from_user.id == ADMIN_ID and msg.reply_to_message:
        user_id = msg.reply_to_message.forward_from.id
        await context.bot.send_message(chat_id=user_id, text=msg.text)
        return

    # Foydalanuvchi yozsa — adminga forward qilinadi
    if msg.from_user.id != ADMIN_ID:
        await context.bot.forward_message(
            chat_id=ADMIN_ID,
            from_chat_id=msg.chat_id,
            message_id=msg.message_id,
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, user_message))

    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
