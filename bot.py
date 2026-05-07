import logging
import os
import sys
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Loglarni Render konsolida ko'rish uchun
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot muvaffaqiyatli ishlamoqda!")

def main():
    if not TOKEN:
        print("XATO: BOT_TOKEN topilmadi!")
        return

    # v20.8 da Updater o'rniga Application ishlatiladi
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot ishga tushdi...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
