import language_tool_python
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext

TOKEN = "8154441285:AAH3oUjtr6ITikmOYA_O5mGgRa0dmxvB7qU"

tool = language_tool_python.LanguageTool('en-US')

async def handle_message(update: Update, context: CallbackContext):
    user_text = update.message.text
    corrected_text = tool.correct(user_text)  # Correct grammar mistakes
    await update.message.reply_text(corrected_text)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
