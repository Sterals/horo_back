# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging

import json
import logging

# Импортируем подмодули Flask для запуска веб-сервиса.
from flask import Flask, request
application = Flask(__name__)



app = Flask(__name__)
app.debug = True

logging.basicConfig(level=logging.DEBUG)

sessionStorage = {}

@app.route("/")
def hello():
	return "Welcome to my page"

@app.route('/index')
def index():
	return'<h1>Heroku Deploy</h1>'

@app.route("/marusya", methods=['POST', 'GET'])
def marusya():
	return "Marusya"

@app.route("/sequence", methods=['POST'])
def main():
	logging.info("Request: %r", request.json)
	card = {}
	buttons = []

	if request.json['session']['new']:
		text = "Привет!"
	elif request.json['request']['command'] == 'on_interrupt':
		text = 'Пока!'

	elif request.json['request']['command'] == 'привет':
		text = 'Привет!'

	elif request.json['request']['command'] == 'картинка':
		text = 'Картиночка'
		card = {
          "type":"BigImage",
          "image_id":457239019,
          # "title": "Заголовок для изображения",
          # "description": "Описание изображения"
		} 

	elif request.json['request']['command'] == 'карусель':
		text = 'Каруселечка'
		card = {
			"type": "ItemsList",
			"items": [{"image_id":457239018}, {"image_id":457239019}, {"image_id":457239017}],
			# "title": "Заголовок для изображения",
			# "description": "Описание изображения"
		} 

	elif request.json['request']['command'] == 'кнопки':
		text = 'Кнопочки'
		buttons = [{'title':"blue pill"}, {"title":"red pill"}]

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