from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
from googletrans import Translator

updater = Updater('5130729987:AAFtfclfnpsee03LBGIRa_KECXpMJ45nbxE',use_context = True )

def start(updater,context):
 updater.message.reply_text('hi baga nagaan dhufte bot kana akka translate itti fayyadamuu dandeessu yeroo gaarii')
 
def echo(updater,context):
 usr_msg =updater.message.text
 translator = Translator()
 translation = translator.translate(usr_msg,dest='am') 
 updater.message.reply_text(translation.text)
 
dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()
