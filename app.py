# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging

import json
import logging
import pandas as pd

# Импортируем подмодули Flask для запуска веб-сервиса.
from flask import Flask, request
application = Flask(__name__)

app = Flask(__name__)
app.debug = True
logging.basicConfig(level=logging.DEBUG)

sessionStorage = {}


SIGNS = ["овен",
	"телец",
	"близнецы",
	"рак",
	"лев",
	"дева",
	"весы",
	"скорпион",
	"козерог",
	"стрелец",
	"водолей",
	"рыбы",
]

HOROSCOPES = pd.read_csv("horoscopes.csv", sep=";")

# @app.route("/")
# def hello():
# 	return "Welcome to my page"

@app.route('/index')
def index():
	return'<h1>Heroku Deploy</h1>'

@app.route("/marusya", methods=['POST', 'GET'])
def marusya():
	return "Marusya"

@app.route("/", methods=['POST'])
def main():
	logging.info("Request: %r", request.json)
	card = {}
	buttons = []

	if request.json['session']['new']:
		text = "Привет! Это навык AI Гороскоп. Какой у Вас знак зодиака?"
		buttons = [{x,y} for x,y in zip(12*["title"], SIGNS)]
				   
	elif request.json['request']['command'] == 'on_interrupt':
		text = 'Приходи еще!'

	elif request.json['request']['command'] in SIGNS:
		text = 'Гороскоп!'

	# elif request.json['request']['command'] == 'картинка':
	# 	text = 'Картиночка'
	# 	card = {
 #          "type":"BigImage",
 #          "image_id":457239019,
 #          # "title": "Заголовок для изображения",
 #          # "description": "Описание изображения"
	# 	} 

	# elif request.json['request']['command'] == 'карусель':
	# 	text = 'Каруселечка'
	# 	card = {
	# 		"type": "ItemsList",
	# 		"items": [{"image_id":457239018}, {"image_id":457239019}, {"image_id":457239017}],
	# 		# "title": "Заголовок для изображения",
	# 		# "description": "Описание изображения"
	# 	} 

	# elif request.json['request']['command'] == 'кнопки':
	# 	text = 'Кнопочки'
	# 	buttons = [{'title':"blue pill"}, {"title":"red pill"}]

	else:
		text = request.json['request']['command']
	response = {
		"version":request.json['version'],
		'session':request.json['session'],
		"response": {
			"end_session": False,
			"text" : text,
			"card" : card, 
			"buttons" : buttons 
		}

	}
	logging.info("response %r", response)

	return json.dumps (response, ensure_ascii=False, indent=2)


@app.route("/debug", methods=['POST'])
def debug():
	response = {
	"version":request.json['version'],
	'session':request.json['session'],
	"response": {
		"end_session": False,
		"text" : "hi"
	}}
	return response


if __name__ == '__main__':
	app.run(debug=True)