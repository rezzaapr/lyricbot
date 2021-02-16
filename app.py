import telebot
import requests as r
import json
from lirik import search

API_TOKEN = '1650221173:AAFm0SWAl5i916vb8Uu_olGd5SM3ZbmIqFE'

bot = telebot.TeleBot(API_TOKEN)



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
	if message.text.startswith('/'):
		print('Succes')
	else:
		cari = search(message.text).result()
		bot.reply_to(message,f'<b>{cari}</b>', parse_mode='html')
		
	if message.text == '/start':
		req = r.get('https://mydatabase-7f431-default-rtdb.firebaseio.com/.json')
		if message.from_user.id in req.json():
			nama = message.chat.first_name
			bot.reply_to(message, f'<b>Selamat Datang {nama}! Silahkan Join Channel Untuk Mendapatkan Info Bot Terbaru Lainnya @rzaprbot\n\n/about - Tentang Bot\n/help - Cara Penggunaan\n/stats - Statistic User</b>', parse_mode="html")
		else:
			data = {
			message.from_user.username: {'Nama': message.from_user.first_name}
			}
			req = r.patch('https://mydatabase-7f431-default-rtdb.firebaseio.com/.json', json = data)
			nama = message.chat.first_name
			bot.reply_to(message, f'<b>Selamat Datang {nama}! Silahkan Join Channel Untuk Mendapatkan Info Bot Terbaru Lainnya @rzaprbot\n\n/about - Tentang Bot\n/help - Cara Penggunaan\n/stats - Statistic User</b>', parse_mode="html")

	if message.text == '/help':
		bot.reply_to(message, '<b>Tulis Lirik Lagu Yang Ingin Di Cari\n\nContoh:\n\n1:\nIwan Fals Kota\n2:\nKota\n3:\nKota Iwan Fals</b>', parse_mode='html')

	if message.text == '/stats':
		req = r.get('https://mydatabase-7f431-default-rtdb.firebaseio.com/.json')
		bot.reply_to(message, f'<b>📊Statistic Bot\n\n👥Total Pengguna : {len(req.json())}</b>', parse_mode='html')

	if message.text == '/about':
		bot.reply_to(message, f'<b>@FindLirikBot V1.0\n\nTanggal Dibuat: 16/02/2021\nKontak Admin:\n\n@rzaprrr\n\nBotChannel:\n\n@rzaprbot</b>', parse_mode='html')

bot.polling()