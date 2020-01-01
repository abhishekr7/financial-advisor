from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet

from datetime import date, timedelta

import requests

class ActionStock(Action):
	def name(self):
		return 'action_stock'

	def run(self, dispatcher, tracker, domain):

		 # worldtradingdata api key
		api_token = "WDfwGuk6Te3Gtjwb5dE55IOeF1EfBsSodusSaC65shAn0TRBgWce25Jb48r4"
		symbol_loc = tracker.get_slot('symbol')

		json_obj = requests.get("http://api.worldtradingdata.com/api/v1/stock?symbol="+ symbol_loc + "&api_token="+ api_token)

		json = json_obj.json()

		ticker_symbol = json['data'][0]['symbol']
		company_name = json['data'][0]['name']
		currency = json['data'][0]['currency']
		close = json['data'][0]['price']
		open = json['data'][0]['price_open']
		high = json['data'][0]['day_high']
		low = json['data'][0]['day_low']
		volume = json['data'][0]['volume']

		response = """\t{} \n Company : {} \n currency : {} \n close : {} \n open : {} \n high : {} \n low : {} \n volume : {}""".format(ticker_symbol, company_name, currency, close, open, high, low, volume)

		dispatcher.utter_message(response)

		return [SlotSet('symbol',symbol_loc)]

class ActionForex(Action):
	def name(self):
		return 'action_forex'

	def run(self, dispatcher, tracker, domain):

		 # worldtradingdata api key
		api_token = "WDfwGuk6Te3Gtjwb5dE55IOeF1EfBsSodusSaC65shAn0TRBgWce25Jb48r4"
		BASE_loc = tracker.get_slot('base')

		json_obj = requests.get("http://api.worldtradingdata.com/api/v1/forex?base="+ BASE_loc + "&api_token="+ api_token)

		json = json_obj.json()

		USD = None
		GBP = None
		EURO = None
		JPY = None
		CNY = None
		INR = None

		if BASE_loc.casefold() == 'usd':
			GBP = json['data']['GBP']
			EURO = json['data']['EUR']
			JPY = json['data']['JPY']
			CNY = json['data']['CNY']
			INR = json['data']['INR']
			response = """\tUSD \n GBP : {} \n EURO : {} \n JPY : {} \n CNY : {} \n INR : {} \n""".format(GBP, EURO, JPY, CNY, INR)
		elif BASE_loc.casefold() == 'gbp':
			USD = json['data']['USD']
			EURO = json['data']['EUR']
			JPY = json['data']['JPY']
			CNY = json['data']['CNY']
			INR = json['data']['INR']
			response = """\tGBP \n USD : {} \n EURO : {} \n JPY : {} \n CNY : {} \n INR : {} \n""".format(USD, EURO, JPY, CNY, INR)
		elif BASE_loc.casefold() == 'eur':
			USD = json['data']['USD']
			GBP = json['data']['GBP']
			JPY = json['data']['JPY']
			CNY = json['data']['CNY']
			INR = json['data']['INR']
			response = """\tEURO \n USD : {} \n GBP : {} \n JPY : {} \n CNY : {} \n INR : {} \n""".format(USD, GBP, JPY, CNY, INR)
		elif BASE_loc.casefold() == 'jpy':
			USD = json['data']['USD']
			GBP = json['data']['GBP']
			EURO = json['data']['EUR']
			CNY = json['data']['CNY']
			INR = json['data']['INR']
			response = """\tJPY \n USD : {} \n GBP : {} \n EURO : {} \n CNY : {} \n INR : {} \n""".format(USD, GBP, EURO, CNY, INR)
		elif BASE_loc.casefold() == 'cny':
			USD = json['data']['USD']
			GBP = json['data']['GBP']
			EURO = json['data']['EUR']
			JPY = json['data']['JPY']
			INR = json['data']['INR']
			response = """\tCNY \n USD : {} \n GBP : {} \n EURO : {} \n JPY : {} \n INR : {} \n""".format(USD, GBP, EURO, JPY, INR)
		elif BASE_loc.casefold() == 'inr':
			USD = json['data']['USD']
			GBP = json['data']['GBP']
			EURO = json['data']['EUR']
			JPY = json['data']['JPY']
			CNY = json['data']['CNY']
			response = """\tINR \n USD : {} \n GBP : {} \n EURO : {} \n JPY : {} \n CNY : {} \n""".format(USD, GBP, EURO, JPY, CNY)

		dispatcher.utter_message(response)

		return [SlotSet('base',BASE_loc)]

class ActionConvert(Action):
	def name(self):
		return 'action_convert'

	def run(self, dispatcher, tracker, domain):

		 # worldtradingdata api key
		api_token = "WDfwGuk6Te3Gtjwb5dE55IOeF1EfBsSodusSaC65shAn0TRBgWce25Jb48r4"
		src_loc = tracker.get_slot('src')
		dest_loc = tracker.get_slot('dest')

		json_obj = requests.get("http://api.worldtradingdata.com/api/v1/forex?base="+ src_loc + "&api_token="+ api_token)

		json = json_obj.json()

		USD = '1'
		GBP = '1'
		EURO = '1'
		JPY = '1'
		CNY = '1'
		INR = '1'

		if src_loc.casefold() != 'usd':
			USD = json['data']['USD']

		if src_loc.casefold() != 'gbp':
			GBP = json['data']['GBP']

		if src_loc.casefold() != 'eur':
			EUR = json['data']['EUR']

		if src_loc.casefold() != 'jpy':
			JPY = json['data']['JPY']

		if src_loc.casefold() != 'cny':
			CNY = json['data']['CNY']

		if src_loc.casefold() != 'inr':
			INR = json['data']['INR']

		dest = '1'

		if dest_loc.casefold() == 'usd':
			dest = USD
		elif dest_loc.casefold() == 'gbp':
			dest = GBP
		if dest_loc.casefold() == 'eur':
			dest = EUR
		if dest_loc.casefold() == 'jpy':
			dest = JPY
		if dest_loc.casefold() == 'cny':
			dest = CNY
		if dest_loc.casefold() == 'inr':
			dest = INR

		response = """\t 1 {} => {} {}\n""".format( src_loc.upper(), dest, dest_loc.upper())

		dispatcher.utter_message(response)

		return [SlotSet('src',src_loc), SlotSet('dest', dest_loc)]

class ActionHistoric(Action):
	def name(self):
		return 'action_historic'

	def run(self, dispatcher, tracker, domain):

		 # worldtradingdata api key
		api_token = "WDfwGuk6Te3Gtjwb5dE55IOeF1EfBsSodusSaC65shAn0TRBgWce25Jb48r4"
		symbol_loc = tracker.get_slot('symbol')
		days_loc = tracker.get_slot('days')

		days_back = int(days_loc)

		date_to = date.today()
		date_from = date_to - timedelta(days_back)

		json_obj = requests.get("http://api.worldtradingdata.com/api/v1/history?symbol="+ symbol_loc + "&date_from="+ str(date_from) + "&date_to=" + str(date_to) + "&sort=oldest&api_token=" + api_token)

		json = json_obj.json()

		response = ''

		for x,y in json['history'].items():
			response = response + "\n" + response + str(x) + " (close) => " + str(y['close'])

		dispatcher.utter_message(response)

		return [SlotSet('symbol',symbol_loc), SlotSet('days', days_loc)]
