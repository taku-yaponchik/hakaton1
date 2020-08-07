import telebot
import requests
from telebot import types


token='983189915:AAH1SHYguP5syZ_p6jdf42pXb1mk2xftz7A'
bot=telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    print(message)
    sti = open('123.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, f"Добро пожаловать, {message.from_user.first_name}!\n Я - Pinokio, бот создан чтобы читать статии из VK")
    # start_info='Добро пожаловать Этот помогает читать статьи из вконтакте'
    #  keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("NBA")
    btn2 = types.KeyboardButton("Искусство слова")
    btn3 = types.KeyboardButton("AnimeVost")
    btn4 = types.KeyboardButton("Life-Hack")
        
    markup.add(btn1, btn2,btn3,btn4)
    bot.send_message(message.chat.id,'Выберите один из пунктов из "меню"' ,reply_markup=markup)

    




@bot.message_handler(commands=['info'])
def info(message):
    start_info='Этот бот помогает читать 10 статии не заходя к сайту. Группы такие как: \n1. NBA, \n2. Искусство слова, \n3. AnimeVost, \n4. Life-Hack\nВы можете их открыть в рахделе меню. '

    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)


    bot.send_message(message.chat.id, start_info)



def get_nba_posts():

    token = "664921b4664921b4664921b40c663a7f8566649664921b4396437b5c6e3bf6e41a4e3b8"
    version = 5.122
    domain = 'nba'
    count = 10
    offset = 0
    all_posts = []
    while offset < 10:
        response = requests.get('https://api.vk.com/method/wall.get',
        params={
                'access_token': token,
                'v': version,
                'domain': domain,
                'count': count,
                'offset': offset
        })
        data = response.json()['response']['items']
        offset+=10
        all_posts.extend(data)
    return all_posts


@bot.message_handler(content_types=['text'])
def get_names(message):
    if message.text.lower() == 'nba':
        for post in get_nba_posts():
            # print(post)
            article=post['text']
            try:
                post_video_url=post['attachments'][0]['link']['url']
            except:
                post_video_url=''
            try:
                post_image=post['attachments'][0]['photo']['sizes'][-1]['url']
            except:
                post_image=''
            full_message=f'{article} \n {post_video_url} \n {post_image} '
            bot.send_message(message.chat.id, full_message )

    keyboard = types.InlineKeyboardMarkup()

    ewe10 = types.InlineKeyboardButton("+10 постов", switch_inline_query="Telegram")
    nazad = types.InlineKeyboardButton("Назад", switch_inline_query="Telegram")
    keyboard.add(ewe10, nazad)

    bot.send_message(message.chat.id, "Вы можете посмотреть еще +10 постов, либо отмотать назад.", reply_markup=keyboard)
    
    if keyboard.add(ewe10)==True:
        get_nba_posts()
        

        











bot.polling(none_stop=True)
