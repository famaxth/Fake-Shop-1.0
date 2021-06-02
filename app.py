# -*- coding: utf8 -*-

#Production by Famaxth
#Telegram - @famaxth


import telebot
import config
import SimpleQIWI
import time
import random
import urllib
import menu
from datetime import datetime
from io import BytesIO
from telebot import types
from time import sleep
from SimpleQIWI import *



bot = telebot.TeleBot(config.token, parse_mode=None)
print("Бот начал работу")


joinedFile = open("joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()


@bot.message_handler(commands=["start"])
def send_welcome(message):
    if not str(message.chat.id) in joinedUsers:
        print("\nБот был запущен. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        joinedFile = open("joined.txt", "a")
        joinedFile.write(str(message.chat.id) + "\n")
        joinedUsers.add(str(message.chat.id))
        bot.send_message(message.chat.id, ""+config.name+"\n\nДобро пожаловать, "+message.chat.first_name+"!\n\n♦️Вы можете совершить покупку и получить свой товар сразу после оплаты.\n♦️Выдача адресов круглосуточно без участия оператора!\n♦️Все безопасно и анонимно\n\n❗️Если возникнут какие-то проблемы - @admin", reply_markup=menu.operator)
        bot.send_message(message.from_user.id, 'Выберите нужный раздел: ', reply_markup=menu.start)
    elif message.chat.id == config.admin_id:
        print("\nБот был запущен. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(config.admin_id, ""+config.name+"\n\nДобро пожаловать, Администратор!\n\n♦️Вы можете совершить покупку и получить свой товар сразу после оплаты.\n♦️Выдача адресов круглосуточно без участия оператора!\n♦️Все безопасно и анонимно\n\n❗️Если возникнут какие-то проблемы - @admin", reply_markup=menu.operator)
        bot.send_message(message.from_user.id, 'Выберите нужный раздел: ', reply_markup=menu.start2)
    else:
        print("\nБот был запущен. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, ""+config.name+"\n\nДобро пожаловать, "+message.chat.first_name+"!\n\n♦️Вы можете совершить покупку и получить свой товар сразу после оплаты.\n♦️Выдача адресов круглосуточно без участия оператора!\n♦️Все безопасно и анонимно\n\n❗️Если возникнут какие-то проблемы - @admin", reply_markup=menu.operator)
        bot.send_message(message.from_user.id, 'Выберите нужный раздел: ', reply_markup=menu.start)


@bot.message_handler(commands=["send"])
def send_sticker(message):
    if message.chat.id == config.admin_id:
        for user in joinedUsers:
            bot.send_message(user, message.text[message.text.find(' '):])
    else:
        bot.send_message(message.chat.id, "❌ В доступе отказано!")


@bot.message_handler(commands=["info"])
def send_info(message):
    if message.chat.id == config.admin_id:
        bot.send_message(message.chat.id, "Добро пожаловать в ЦУМ! :)\n\n-------------------\nМы рады предложить Вам высококачественный товар, быстрый сервис обслуживания и доброжелательную атмосферу.\nУ нас Вы можете приобрести только лучшее качество товара по оптимальным ценам!\nДля постоянных клиентов - автоматическая система СКИДОК от 3-х покупок!\n\nОзнакомиться с бонусами и подарками можно здесь: http://hydrakxbeouow4af.onion/forum/thread/4371\n\n❗️Данный магазин является лишь демонстрацией разработчиков и их возможностей. Никакого отношения к ЦУМ Москва на сайте Hydra - ОН НЕ ИМЕЕТ. Подобные действия противозаконны. Деньги мы не принимаем и ничего не продаем!", reply_markup=menu.start2)
    else:
        bot.send_message(message.chat.id, "Добро пожаловать в ЦУМ! :)\n\n-------------------\nМы рады предложить Вам высококачественный товар, быстрый сервис обслуживания и доброжелательную атмосферу.\nУ нас Вы можете приобрести только лучшее качество товара по оптимальным ценам!\nДля постоянных клиентов - автоматическая система СКИДОК от 3-х покупок!\n\nОзнакомиться с бонусами и подарками можно здесь: http://hydrakxbeouow4af.onion/forum/thread/4371\n\n❗️Данный магазин является лишь демонстрацией разработчиков и их возможностей. Никакого отношения к ЦУМ Москва на сайте Hydra - ОН НЕ ИМЕЕТ. Подобные действия противозаконны. Деньги мы не принимаем и ничего не продаем!", reply_markup=menu.start)


@bot.message_handler(commands=["liu4eg7hok"])
def send_deepweb(message):
    bot.send_message(message.chat.id, "Бот создан разработчиком Berlin.")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'Проверить оплату':
            global order
            qiwiopl = random.randint(1, 4)
            btcopl = random.randint(1, 4)
            paypalopl = random.randint(1, 4)
            bot.send_message(call.message.chat.id, "⏳ Проверка оплаты..")
            time.sleep(qiwiopl)
            bot.send_message(call.message.chat.id, "❌ Оплата не найдена.")



@bot.message_handler(content_types=["text"])
def send_otziv(message):
    if message.text == '📦 Покупки':
        print('Пользователь нажал покупки. ID: '+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, '❌ Покупки отсутствуют ❌')
    elif message.text == '💰Баланс':
        if message.chat.id == config.admin_id:
            api = QApi(token=config.token_qiwi, phone=config.qiwi)
            balance = api.balance[0]
            bot.send_message(config.admin_id, "🥝 Баланс вашего Киви: *"+str(balance)+"* руб", parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, "❌ В доступе отказано!")
    elif message.text == 'Админ-Панель':
        if message.chat.id == config.admin_id:
            bot.send_message(config.admin_id, "☎️ Админ панель", reply_markup=menu.admin)
        else:
            bot.send_message(message.chat.id, "❌ В доступе отказано!")
    elif message.text == '📩 Рассылка':
        if message.chat.id == config.admin_id:
            bot.send_message(config.admin_id, "Выберите нужное действие", reply_markup=menu.krekin)
        else:
            bot.send_message(message.chat.id, "❌ В доступе отказано!")
    elif message.text == 'Отправить новое сообщение':
        if message.chat.id == config.admin_id:
            bot.send_message(config.admin_id, "Начнем!\n\nВы можете отправить подписчикам одно или несколько сообщений, в том числе любые файлы, музыку,картинки и т.д\n\nДля того, чтобы сделать рассылку нажмите /send и введите ваше сообщение.", reply_markup=menu.krekin)
        else:
            bot.send_message(message.chat.id, "❌ В доступе отказано!")
    elif message.text == '👤 Мой кабинет':
        if message.chat.id == config.admin_id:
            print('Пользователь нажал информация. ID: '+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
            bot.send_message(message.chat.id, "Информация об аккаунте\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n💎 Никнейм: "+message.chat.username+"\n💎 Ваш ID: "+str(message.chat.id)+"\n💎 Кэшбек: 0 руб\n💎 Язык: Ru\n➖➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=menu.start2)
        else:
            print('Пользователь нажал кабинет. ID: '+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
            bot.send_message(message.chat.id, "Информация об аккаунте\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n💎 Никнейм: "+message.chat.username+"\n💎 Ваш ID: "+str(message.chat.id)+"\n💎 Кэшбек: 0 руб\n💎 Язык: Ru\n➖➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=menu.start)
    elif message.text == '❔ Информация':
        if message.chat.id == config.admin_id:
            print('Пользователь нажал информация. ID: '+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
            bot.send_message(message.chat.id, "Добро пожаловать в ЦУМ! :)\n\n-------------------\nМы рады предложить Вам высококачественный товар, быстрый сервис обслуживания и доброжелательную атмосферу.\nУ нас Вы можете приобрести только лучшее качество товара по оптимальным ценам!\nДля постоянных клиентов - автоматическая система СКИДОК от 3-х покупок!\n\nОзнакомиться с бонусами и подарками можно здесь: http://hydrakxbeouow4af.onion/forum/thread/4371\n\n❗️Данный магазин является лишь демонстрацией разработчиков и их возможностей. Никакого отношения к ЦУМ Москва на сайте Hydra - ОН НЕ ИМЕЕТ. Подобные действия противозаконны. Деньги мы не принимаем и ничего не продаем!", reply_markup=menu.start2)
        else:
            print('Пользователь нажал информация. ID: '+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
            bot.send_message(message.chat.id, "Добро пожаловать в ЦУМ! :)\n\n-------------------\nМы рады предложить Вам высококачественный товар, быстрый сервис обслуживания и доброжелательную атмосферу.\nУ нас Вы можете приобрести только лучшее качество товара по оптимальным ценам!\nДля постоянных клиентов - автоматическая система СКИДОК от 3-х покупок!\n\nОзнакомиться с бонусами и подарками можно здесь: http://hydrakxbeouow4af.onion/forum/thread/4371\n\n❗️Данный магазин является лишь демонстрацией разработчиков и их возможностей. Никакого отношения к ЦУМ Москва на сайте Hydra - ОН НЕ ИМЕЕТ. Подобные действия противозаконны. Деньги мы не принимаем и ничего не продаем!", reply_markup=menu.start)
    elif message.text == '🌿 Доступный ассортимент':
        print('Пользователь нажал ассортимент. ID: '+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, "Выберите город:", reply_markup=menu.city)
    elif message.text == '🔙Назад':
        if message.chat.id == config.admin_id:
            bot.send_message(config.admin_id, '🔙Вы вернулись в главное меню', reply_markup=menu.start2)
        else:
            bot.send_message(message.chat.id, '🔙Вы вернулись в главное меню', reply_markup=menu.start)
    elif message.text == 'Москва':
        print("Выбрал г. Москва. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_msk)
    elif message.text == 'Санкт-Петербург':
        print("Выбрал г. Санкт-Петербург. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_spb)
    elif message.text == 'Екатеринбург':
        print("Выбрал г. Екатеринбург. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_ekb)
    elif message.text == 'Домодедово':
        print("Выбрал г. Домодедово. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_msk)
    elif message.text == 'Мытищи':
        print("Выбрал г. Мытищи. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_spb)
    elif message.text == 'Зеленоград':
        print("Выбрал г. Зеленоград. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_perm)
    elif message.text == 'Подольск':
        print("Выбрал г. Подольск. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_voronezh)
    elif message.text == 'Челябинск':
        print("Выбрал г. Челябинск. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_voronezh)
    elif message.text == 'Нижний Новгород':
        print("Выбрал г. Нижний Новгород. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_spb)
    elif message.text == 'Иркутск':
        print("Выбрал г. Иркутск. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_msk)
    elif message.text == 'Оренбург':
        print("Выбрал г. Оренбург. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_perm)
    elif message.text == 'Пенза':
        print("Выбрал г. Пенза. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_spb)
    elif message.text == 'Омск':
        print("Выбрал г. Омск. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_voronezh)
    elif message.text == 'Пермь':
        print("Выбрал г. Пермь. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_perm)
    elif message.text == 'Рязань':
        print("Выбрал г. Рязань. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_msk)
    elif message.text in menu.rayon_spisok:
        print('Выбрал район '+message.text+'. ID: '+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        assort = bot.send_message(message.chat.id, '🧨 Ассортимент 🧨', reply_markup=menu.what)
        bot.register_next_step_handler(assort, oplata)
    else:
        bot.send_message(message.chat.id, "Ничего не понятно!")


def oplata(message):
	global assort, tovarka
	tovarka = message.text
	if message.text in menu.what_spisok:
		comment = random.randint(10000, 99999)
		print('Выбрал товар: '+tovarka+'. ID: '+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
		bot.send_message(message.chat.id, '⏳ Создаём заказ..')
		time.sleep(2)
		bot.send_message(message.chat.id, 'Информация об оплате\n➖➖➖➖➖➖➖➖➖➖\nТовар: '+tovarka+'\n\n💰 Оплата Bitcoin: '+config.bitcoin+'\n\n🥝 Оплата Qiwi: '+config.qiwi+'\n\n 📝 Комментарий к переводу: '+str(comment)+'\n➖➖➖➖➖➖➖➖➖➖\nПереводите ту сумму, на которую хотите пополнить баланс! Заполняйте номер телефона и комментарий при переводе внимательно!\n Администрация не несет ответственности за ошибочный перевод, возврата в данном случае не будет! После перевода нажмите кнопку Проверить оплату!', reply_markup=menu.keyboard)


#Start bot
if __name__ == '__main__':
    bot.polling(none_stop=True)
