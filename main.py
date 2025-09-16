from telegram.ext import Updater, CommandHandler

# --- Bot credentials ---
TOKEN = "8064099505:AAEX0yY-3RbmtlhcYtmeawWuff7BuT0AbpY"
BOT_USERNAME = "@IslamicMasailBot"

# --- Start command function ---
def start(update, context):
    update.message.reply_text("السلام علیکم 🌹\nمیں Islamic Masail Bot ہوں۔")

# --- Main function ---
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
