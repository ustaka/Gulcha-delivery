import logging
import os
import sys
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Loglarni Render konsolida aniq ko'rish uchun
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

# O'zgaruvchilarni Render Environment Variables bo'limidan oladi
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    
    # Adminni tekshirish logikasi
    if ADMIN_ID and user_id == str(ADMIN_ID):
        await update.message.reply_text("Salom Admin! Tizim muvaffaqiyatli ishga tushdi va sizni tanidi ✅")
    else:
        await update.message.reply_text("Salom! Gulcha-delivery botiga xush kelibsiz! Tez orada menyuni yuklaymiz.")

def main():
    if not TOKEN:
        logger.error("XATO: BOT_TOKEN topilmadi! Render Environment Variables bo'limini tekshiring.")
        return

    # DIQQAT: v20.8 versiyada faqat Application ishlatiladi, Updater emas!
    application = Application.builder().token(TOKEN).build()
    
    # Start buyrug'ini ulaymiz
    application.add_handler(CommandHandler("start", start))
    
    logger.info("Bot ishga tushmoqda...")
    # Render'da doimiy ishlashi uchun pooling rejimi
    application.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
