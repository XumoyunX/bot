from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler, ConversationHandler, CallbackQueryHandler
from django.core.management.base import BaseCommand
from myapp.models import Region, District, Post




def start(update: Update, context: CallbackContext):
    button_lang = [
        [KeyboardButton("UZ 🇺🇿"), KeyboardButton("RUS 🇷🇺")]
    ]
    update.message.reply_text("Tilni tanlang",
                            reply_markup=ReplyKeyboardMarkup(button_lang, resize_keyboard=True))



    return 1
def region_button(update, context): 
   
    region = Region.objects.all()
    button_key = []
    for i in region:
        button_key.append([KeyboardButton(f"{i.name_uz}")])
    
    update.message.reply_text("Viloyat birini tanlang",
                            reply_markup=ReplyKeyboardMarkup(button_key, resize_keyboard=True))

    return 2



def category_handler(update, context):
    name = update.message.text
    try:
        category = Region.objects.get(name_uz=name)
    except:
        update.message.reply_text("Viloyat topilmadi")
        return
    product  = District.objects.filter(region=category)

    buttons = []
    for i in product:
        buttons.append([KeyboardButton(f"{i.name_uz}")])
    
    update.message.reply_text("Quyidagilardan tuman tanlang",
                            reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))




    return 3
def post_handler(update, context):

    name = update.message.text
    try:
        tuman = District.objects.get(name_uz=name)
    except:
        update.message.reply_text("Viloyat topilmadi")
        return
    post_all  = Post.objects.filter(district=tuman)

    for i in post_all:

        keyboard = [[InlineKeyboardButton('Locatsiya', callback_data=f"{i.id}")],]
        reply_markup = InlineKeyboardMarkup(keyboard)
        url = "http://192.168.0.130:3000/"
        link = f'<a href="{url}">Bu link siz uchun foydali bo\'lishi mumkin</a>'
        context.bot.send_photo(chat_id=update.effective_user.id,
                                photo=open(i.img.path, "rb"), caption=f"<b>Telefon nomer:</b> {i.number}\n<b>Ish vaqti:</b> {i.vaqt}\n<b>1 soat maydon naxri:</b> {i.price} so'm\n<b>Maydon soni:</b> {i.maydon_soni} ta\n<b>Maydon joylashga arinter:</b><i>{i.text_uz}</i>\n Hello: {link}", 
                                parse_mode="HTML", reply_markup=reply_markup)
        


    return 4
def inline_button(update: Update, context: CallbackContext):
    query = update.callback_query
    data_split = query.data
    post = Post.objects.get(id=int(data_split[0]))
    print(post)
    # location
    update.callback_query.message.reply_location(latitude=post.latitude, longitude=post.longtitude)

  





    # for i in post_all:
    #     if data[0] == "1":
    #         print("1")















  



  










class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        updater = Updater("5893429977:AAElaJHJPzZJXHMZt5NRGUtZ2m55VV24apU")

        all_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states = {
                1: [MessageHandler(Filters.text, region_button)],
                2: [MessageHandler(Filters.text, category_handler)],
                3: [MessageHandler(Filters.text, post_handler)],
                4: [CallbackQueryHandler(inline_button)]

             },
        fallbacks = []
        )


        updater.dispatcher.add_handler(all_handler)
        updater.start_polling()
        updater.idle()















