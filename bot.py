from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Token bot Telegram Anda
TOKEN = '7815701443:AAFa5ncS1X1cnTxuUlmFhhC0eo_tZAfIfGY'

# Fungsi untuk memulai bot
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Halo, ada yang bisa saya bantu?')

# Inisialisasi bot dan tambahkan handler
def main():
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))

    # Mulai bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
