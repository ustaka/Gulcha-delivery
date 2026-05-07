import logging
import os
import sys
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Loglarni Render'da ko'rish uchun
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Yangi servis muvaffaqiyatli ishga tushdi!")

def main():
    if not TOKEN:
        print("XATO: BOT_TOKEN topilmadi!")
        return
    # v20.8 versiyada faqat Application ishlatiladi
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
