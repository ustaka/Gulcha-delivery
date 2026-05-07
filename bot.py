import logging
import os
import sys
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Loglarni Render konsolida batafsil ko'rish uchun
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

# Tokenni tekshirish
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot nihoyat ishga tushdi!")

def main():
    try:
        if not TOKEN:
            logger.error("!!! BOT_TOKEN TOPILMADI !!! Render sozlamalarini tekshiring.")
            return

        logger.info("Botni ishga tushirishga urinish...")
        application = Application.builder().token(TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        
        logger.info("Bot pooling rejimida muvaffaqiyatli ishga tushdi.")
        application.run_polling(drop_pending_updates=True)
        
    except Exception as e:
        logger.error(f"Kritik xatolik yuz berdi: {e}")

if __name__ == "__main__":
    main()
