from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Railway env var se lega

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot chal raha hai Railway pe!")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
