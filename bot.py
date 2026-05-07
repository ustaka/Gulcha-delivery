import logging
import os
import sys
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Loglarni Render konsolida ko'rish uchun
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# O'zgaruvchilarni Render'dan olamiz
TOKEN = os.getenv("BOT_TOKEN")
# Agar ADMIN_ID topilmasa, bot xato bermasligi uchun default 0 qo'yamiz
ADMIN_ID = os.getenv("ADMIN_ID")

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    
    # Adminni tekshirish
    if ADMIN_ID and user_id == str(ADMIN_ID):
        await update.message.reply_text("Salom Admin! Yangi buyurtmalar kutilmoqda...")
    else:
        await update.message.reply_text("Salom! Gulcha-delivery botiga xush kelibsiz!")

def main():
    if not TOKEN:
        print("XATO: BOT_TOKEN topilmadi!")
        return
        
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot ishga tushdi...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
