import logging
from telegram import Update
from telegram.ext import Application, Updater, CommandHandler, MessageHandler, filters, ContextTypes
from PIL import Image
import telegram
import pytesseract

TOKEN = "" #Insert the TOKEN of your telegram bot
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  
app = Application.builder().token(TOKEN).build()
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
user_language = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Этот бот предназначен для распознавания текста на изображениях. "
                              "Используй команду /setlang для выбора языка.")

async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        user_language[update.message.from_user.id] = context.args[0]
        await update.message.reply_text(f"Язык установлен на {context.args[0]}")
    else:
        await update.message.reply_text("Используй команду в формате /setlang eng")

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    language = user_language.get(user_id, 'rus')  # По умолчанию устанавливаем русский язык
    await update.message.reply_text(f"Текущий язык распознавания: {language}. Отправь изображение для распознавания.")

async def image_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    language = user_language.get(user_id, 'rus')

    file_id = update.message.photo[-1].file_id
    file = await context.bot.getFile(file_id)
    await file.download_to_drive(f"{file_id}.jpg")

    # Распознавание текста с использованием Tesseract OCR
    try:
        image = Image.open(f"{file_id}.jpg")
        text = pytesseract.image_to_string(image, lang=language)
        await update.message.reply_text(f"Распознанный текст:\n{text}")
    except Exception as e:
        await update.message.reply_text(f"Произошла ошибка при обработке изображения: {str(e)}")

start_handler = CommandHandler('start', start)
set_language_handler = CommandHandler('setlang', set_language)
text_message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler)
image_message_handler = MessageHandler(filters.PHOTO, image_handler)
    
app.add_handler(start_handler)
app.add_handler(set_language_handler)
app.add_handler(text_message_handler)
app.add_handler(image_message_handler)

app.run_polling(allowed_updates=Update.ALL_TYPES)
