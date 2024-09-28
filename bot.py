from telegram import Update
from telegram.ext import Application, CommandHandler
import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Your bot token from BotFather
TOKEN = '7509383883:AAGhYc0CqBsL-GVs1HZmPHqC3tPx9HcpFzw'

# Define the start function
async def start(update: Update, context):
    """Sends a message when the command /start is issued."""
    await update.message.reply_text('bonjour, bienvenue dans la maison de la contrefaçon.')

# Error handling function
async def error(update: Update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Application and pass it your bot's token
    application = Application.builder().token(TOKEN).build()

    # Register the /start command
    application.add_handler(CommandHandler("start", start))

    # Log all errors
    application.add_error_handler(error)

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
