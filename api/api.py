from flask import Flask, request, send_file
from pdf_struct import PDFStruct
from telegram import Bot
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, MessageHandler, Filters
from telegram.ext import Updater

app = Flask(__name__)
pdf_struct = PDFStruct()

TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

bot = Bot(token=TELEGRAM_BOT_TOKEN)

@app.route('/process_pdf', methods=['POST'])
def process_pdf():
    pdf_file = request.files['pdf']
    processed_pdf = pdf_struct.process(pdf_file)
    processed_pdf.save('processed_pdf.pdf')
    return send_file('processed_pdf.pdf', as_attachment=True)

# Telegram command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the PDF Processing Bot! Send me a PDF file.')

# Telegram message handler
def process_telegram_message(update: Update, context: CallbackContext) -> None:
    # Assuming the user sends a PDF file
    pdf_file = update.message.document.get_file()
    file_id = pdf_file.file_id

    # Download the PDF file from Telegram
    downloaded_pdf = bot.get_file(file_id)
    downloaded_pdf.download('uploaded_pdf.pdf')

    # Send the PDF to your Flask server for processing
    with open('uploaded_pdf.pdf', 'rb') as file:
        files = {'pdf': file}
        response = requests.post('http://localhost:5000/process_pdf', files=files)

    # Send the processed PDF back to the user
    update.message.reply_document(open('processed_pdf.pdf', 'rb'))

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.document, process_telegram_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

