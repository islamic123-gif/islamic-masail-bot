from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# آپ کا BotFather والا Token
TOKEN = "8064099505:AAEX0yY-3RbmtlhcYtmeawWuff7BuT0AbpY"

# /start کمانڈ
def start(update, context):
    update.message.reply_text("السلام علیکم! 🤲 میں آپ کا اسلامی بوٹ ہوں۔ سوال کریں یا سلام کریں۔")

# سوالات کے predefined جواب
def reply(update, context):
    text = update.message.text.lower()

    # سلام
    if any(word in text for word in ["سلام", "السلام علیکم", "وعلیکم السلام"]):
        update.message.reply_text("وعلیکم السلام ورحمة الله وبرکاته 🌸")

    # نماز
    elif "نماز" in text:
        update.message.reply_text(
            "نماز دین کا ستون ہے۔ پانچ وقت کی نماز فرض ہے، اور قضا نماز بھی ادا کریں۔"
        )

    # روزہ
    elif "روزہ" in text:
        update.message.reply_text(
            "روزہ رمضان میں فرض ہے اور اس سے صبر و تقویٰ پیدا ہوتا ہے۔"
        )

    # حج
    elif "حج" in text:
        update.message.reply_text(
            "حج ایک سالانہ عبادت ہے جو اہل استطاعت پر فرض ہے۔ اللہ قبول کرے۔"
        )

    # زکوة
    elif "زکوة" in text:
        update.message.reply_text(
            "زکوة مال کی صفائی ہے، نصاب پورا ہونے پر ہر سال دینا فرض ہے۔"
        )

    # قرآن
    elif "قرآن" in text:
        update.message.reply_text(
            "قرآن پاک اللہ کی آخری کتاب ہے، یہ ہدایت اور روشنی ہے۔"
        )

    # حدیث
    elif "حدیث" in text:
        update.message.reply_text(
            "حدیث نبوی ﷺ ہمیں عمل اور اخلاق سکھاتی ہے۔"
        )

    # عام اسلامی مسائل (نمونہ 100 مسائل کی جگہ، آپ مزید add کر سکتے ہیں)
    elif "نماز جمعہ" in text:
        update.message.reply_text("نماز جمعہ ہفتے میں ایک بار جمعہ کے دن فرض ہے۔")
    elif "روزہ نفل" in text:
        update.message.reply_text("نفل روزے سنت ہیں، رمضان کے علاوہ بھی رکھ سکتے ہیں۔")
    elif "نماز جنازہ" in text:
        update.message.reply_text("نماز جنازہ مردہ کی مغفرت کے لیے پڑھی جاتی ہے۔")
    elif "صدقہ" in text:
        update.message.reply_text("صدقہ غرباء اور محتاجوں کی مدد کے لیے دیا جاتا ہے۔")
    elif "توبہ" in text:
        update.message.reply_text("اللہ کی طرف رجوع کرنا اور گناہوں سے باز آنا توبہ ہے۔")
    elif "دعاء" in text:
        update.message.reply_text("اللّهُمَّ اغْفِرْ لَنَا وَلِلْمُسْلِمِيْنَ 🤲")
    elif "حلال" in text:
        update.message.reply_text("حلال وہ ہے جو شرعی طور پر جائز ہو۔")
    elif "حرام" in text:
        update.message.reply_text("حرام وہ ہے جو شرعی طور پر ممنوع ہو۔")
    elif "جہاد" in text:
        update.message.reply_text("جہاد اللہ کی راہ میں کوشش کرنا ہے، صرف جائز اور دفاعی اصولوں کے تحت۔")
    elif "اخلاق" in text:
        update.message.reply_text("اخلاق حسنہ انسان کی پہچان ہے، صبر اور امانت سکھاتے ہیں۔")

    # باقی 100 مسائل یہاں add کر سکتے ہیں، نمونہ کے طور پر ابھی 10+ رکھ دیے
    else:
        update.message.reply_text("معاف کیجیے، یہ سوال میرے علم میں ابھی نہیں۔")

# مین فنکشن
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
