#!/usr/bin/env python

import telebot
bot = telebot.TeleBot("965129932:AAFslbLkrzWhbTY-B3RCovRny6m3fsHwXJU")

keyboardopen = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboardopen.row('Каталог товаров', 'Информация')

keyboardinfo = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboardinfo.row('Вернуться в начало')

keyboard1 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard1.row('Шары из фольги', 'Шары из латекса')

keyboard11 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard11.row('Набор 1','Набор 2','Набор 3','Набор 4','Набор 5')

keyboard12 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard12.row('Связка 1','Связка 2','Связка 3','Связка 4','Связка 5')

keyboard3 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard3.row('1', '2', '3', '4')

user_dict = {}

@bot.message_handler(commands=['start'])
def open_text(message):
    user_dict[message.chat.id] = ['', '', '', '', '']
    bot.send_message(message.chat.id, 'Здравствуйте! У нас самые низкие цены в городе в сочетании с высоким качеством и оперативной доставкой. '                                      'Что вас интересует?', reply_markup=keyboardopen)
    pass



@bot.message_handler(func=lambda message: message.text == "Информация")
def info_message(message):
    bot.send_message(message.from_user.id, 'Бесплатная Доставка осуществляется с интервалом не менее одного часа, круглосуточно, при заказе от 1000 рублей. '
                                           'Прием заказов с 9 до 23 часов по телефону компании, круглосуточно при размещении через сайт или чат-бот Telegram. '
                                           ''
                                           'Способы оплаты: '
                                           '--Наличными: Оплатить заказ товара Вы сможете непосредственно курьеру в руки при получение товара. '
                                           '--Безналичным путем: на карту Сбербанк, ВТБ или с любой карты через сервис Яндекс-касса. '
                                           ''
                                           'Телефон отдела продаж +7 (995) 598-75-22', reply_markup=keyboardinfo)



@bot.message_handler(func=lambda message: message.text == "Вернуться в начало")
def back_message(message):
    bot.send_message(message.from_user.id, 'Вернулись в начало', reply_markup=keyboardopen)
    pass


@bot.message_handler(func=lambda message: message.text == "Каталог товаров")
def Zero_message(message):
    bot.send_message(message.from_user.id, 'Что вас интересует?', reply_markup=keyboard1)
    pass

@bot.message_handler(func=lambda message: message.text == "Шары из фольги")
def One_message(message):
    user_dict[message.chat.id][0] = message.text
    bot.send_photo(message.from_user.id, photo='https://drive.google.com/open?id=12lyrze6Ml_QBOyl9-dthLgR8mKQe-gLO')
    bot.send_photo(message.from_user.id, photo='https://drive.google.com/open?id=1fvq0Nqe3BYlqTV99Bjjhre2BPjvcsY_R')
    bot.send_photo(message.from_user.id, photo='https://drive.google.com/open?id=1jceeeXdSf0nncr1Vy1txwwt0ftXI8Oxf')
    bot.send_photo(message.from_user.id, photo='https://drive.google.com/open?id=1QEkxlULTxvc5cZ7bOSutAyl_ojIVaelQ')
    bot.send_photo(message.from_user.id, photo='https://drive.google.com/open?id=1eZiIhw1FeAhoqCwIDj1UgVtQdvWO2EMC')
    bot.send_message(message.from_user.id, 'Выберите понравившийся набор. Чтобы вернуться в начало нажмите /start.', reply_markup=keyboard11)
    pass



@bot.message_handler(func=lambda message: message.text == "Шары из латекса")
def Two_message(message):
    user_dict[message.chat.id][0] = message.text
    bot.send_photo(message.from_user.id, photo='https://drive.google.com/open?id=12L79XnWVhaONAu5gW3BlFDjvQ_QTyMJf')
    bot.send_photo(message.from_user.id, photo='https://drive.google.com/open?id=1ya2_60VObsrOdpis6RpA34BY2b8du09c')
    bot.send_photo(message.from_user.id, photo='https://drive.google.com/open?id=1vPxopROM1QPNtO7g2PqYAgbOSep9TEIH')
    bot.send_photo(message.from_user.id, photo='https://drive.google.com/open?id=1yuBEY0GzbWeLH50i_syUNQIK0wp5y-_r')
    bot.send_photo(message.from_user.id, photo='https://drive.google.com/open?id=1letAUCWIr7vymtJl6Q-8LgHOTg28740G')
    bot.send_message(message.from_user.id, 'Выберите понравившуюся связку. Чтобы вернуться в начало нажмите /start.', reply_markup=keyboard12)
    pass



@bot.message_handler(func=lambda message: message.text == "Набор 1")
def ThreeOne_message(message):
    user_dict[message.chat.id][1] = message.text
    bot.send_message(message.from_user.id, 'Выберите кол-во', reply_markup=keyboard3)

@bot.message_handler(func=lambda message: message.text == "Набор 2")
def ThreeTwo_message(message):
    user_dict[message.chat.id][1] = message.text
    bot.send_message(message.from_user.id, 'Выберите кол-во', reply_markup=keyboard3)

@bot.message_handler(func=lambda message: message.text == "Набор 3")
def ThreeThree_message(message):
    user_dict[message.chat.id][1] = message.text
    bot.send_message(message.from_user.id, 'Выберите кол-во', reply_markup=keyboard3)

@bot.message_handler(func=lambda message: message.text == "Набор 4")
def ThreeFour_message(message):
    user_dict[message.chat.id][1] = message.text
    bot.send_message(message.from_user.id, 'Выберите кол-во', reply_markup=keyboard3)

@bot.message_handler(func=lambda message: message.text == "Набор 5")
def ThreeFive_message(message):
    user_dict[message.chat.id][1] = message.text
    bot.send_message(message.from_user.id, 'Выберите кол-во', reply_markup=keyboard3)

@bot.message_handler(func=lambda message: message.text == "Связка 1")
def ThreeSix_message(message):
    user_dict[message.chat.id][1] = message.text
    bot.send_message(message.from_user.id, 'Выберите кол-во', reply_markup=keyboard3)

@bot.message_handler(func=lambda message: message.text == "Связка 2")
def ThreeSeven_message(message):
    user_dict[message.chat.id][1] = message.text
    bot.send_message(message.from_user.id, 'Выберите кол-во', reply_markup=keyboard3)

@bot.message_handler(func=lambda message: message.text == "Связка 3")
def ThreeEight_message(message):
    user_dict[message.chat.id][1] = message.text
    bot.send_message(message.from_user.id, 'Выберите кол-во', reply_markup=keyboard3)

@bot.message_handler(func=lambda message: message.text == "Связка 4")
def ThreeNine_message(message):
    user_dict[message.chat.id][1] = message.text
    bot.send_message(message.from_user.id, 'Выберите кол-во', reply_markup=keyboard3)

@bot.message_handler(func=lambda message: message.text == "Связка 5")
def ThreeTen_message(message):
    user_dict[message.chat.id][1] = message.text
    bot.send_message(message.from_user.id, 'Выберите кол-во', reply_markup=keyboard3)





@bot.message_handler(func=lambda message: message.text == "1")
def FourOne_message(message):
    user_dict[message.chat.id][2] = message.text
    bot.send_message(message.from_user.id, 'Напиши своё имя и номер телефона, пожалуйста')

@bot.message_handler(func=lambda message: message.text == "2")
def FourTwo_message(message):
    user_dict[message.chat.id][2] = message.text
    bot.send_message(message.from_user.id, 'Напиши своё имя и номер телефона, пожалуйста')

@bot.message_handler(func=lambda message: message.text == "3")
def FourThree_message(message):
    user_dict[message.chat.id][2] = message.text
    bot.send_message(message.from_user.id, 'Напиши своё имя и номер телефона, пожалуйста')

@bot.message_handler(func=lambda message: message.text == "4")
def FourFour_message(message):
    keyboardopen1 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    user_dict[message.chat.id][2] = message.text
    m = bot.send_message(message.from_user.id, 'Напиши своё имя и номер телефона, пожалуйста', reply_markup=keyboardopen1)
    #bot.send_message(message.from_user.id, message.chat.id)
    bot.register_next_step_handler(m, Five_message)

#@bot.message_handler(content_types=['text'])bot.send_message(message.from_user.id, 'Напиши своё имя и номер телефона, пожалуйста')
def Five_message(message):
    #keyboardopen1 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard= True)
    bot.reply_to(message, "Если всё введено правильно, мы с тобой свяжемся!")
    bot.send_message(message.chat.id, '*FINALLY:*\n'+'\n'.join(user_dict[message.chat.id]), parse_mode='markdown')








if __name__ == '__main__':
     bot.polling(none_stop=True)
