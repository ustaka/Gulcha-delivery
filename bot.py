import logging
import os
import sys
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Loglarni Render konsolida ko'rish uchun
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    stream=sys.stdout
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot muvaffaqiyatli ishga tushdi! Endi menyuni qo'shishimiz mumkin.")

def main():
    if not TOKEN:
        print("XATO: BOT_TOKEN topilmadi!")
        return

    # DIQQAT: Bu yerda 'Updater' so'zi yo'q. Faqat Application.
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    print("Bot polling rejimida ishga tushmoqda...")
    application.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
