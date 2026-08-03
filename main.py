import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from groq import Groq

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
GROQ_KEY = os.environ["GROQ_KEY"]

client = Groq(api_key=GROQ_KEY)

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "تو سعید هستی، دستیار فارسی من."},
            {"role": "user", "content": text}
        ]
    )

    await update.message.reply_text(
        response.choices[0].message.content
    )

app = Application.builder().token(TELEGRAM_TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT, chat)
)

print("Saeed is running...")
app.run_polling()
