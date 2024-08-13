from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import datetime
import random

TOKEN = '6997837051:AAFfJxmUhKcXlsGcAXDzUHkUUMjg39n0Iiw'  # you have to enter bot token here
# I gave Aman0926bot username 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your bot.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am here to help! Use /start to begin.")

async def greet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    await update.message.reply_text(f"Hello, {user.first_name}! Nice to meet you.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = ' '.join(context.args)
    if user_input:
        await update.message.reply_text(user_input)
    else:
        await update.message.reply_text("You didn't say anything!")

async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    await update.message.reply_text(f"The current time is {current_time}")

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why don't skeletons fight each other? They don't have the guts."
    ]
    random_joke = random.choice(jokes)
    await update.message.reply_text(random_joke)

if __name__ == '__main__':
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('greet', greet))
    application.add_handler(CommandHandler('echo', echo))
    application.add_handler(CommandHandler('time', time))
    application.add_handler(CommandHandler('joke', joke))

    application.run_polling()
