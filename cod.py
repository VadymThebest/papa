from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Bot token
BOT_TOKEN = "7915888486:AAGhKsrk2y7jAVCo7XodOKli4vDYyLqXER8"  # Replace with your bot's token

# Source and destination channel IDs
SOURCE_CHANNEL_ID = -1002421555083  # Replace with your source channel ID
DESTINATION_CHANNEL_ID = -1002367061095  # Replace with your destination channel ID

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Forwards messages from the source channel to the destination channel.
    """
    try:
        if update.channel_post and update.channel_post.chat.id == SOURCE_CHANNEL_ID:
            # Forward the message to the destination channel
            await context.bot.forward_message(
                chat_id=DESTINATION_CHANNEL_ID,
                from_chat_id=SOURCE_CHANNEL_ID,
                message_id=update.channel_post.message_id,
            )
            print(f"Message forwarded: {update.channel_post.text}")
    except Exception as e:
        print(f"Error while forwarding message: {e}")

def main():
    # Initialize the bot application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add a handler to listen for messages in the source channel
    application.add_handler(
        MessageHandler(filters.Chat(SOURCE_CHANNEL_ID) & filters.UpdateType.CHANNEL_POST, forward_message)
    )

    # Start the bot
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
print('x')