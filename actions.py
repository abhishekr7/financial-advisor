from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

import requests

class ActionStock(Action):
	def name(self):
		return 'action_stock'

	def run(self, dispatcher, tracker, domain):

		 # worldtradingdata api key
		api_token = "WDfwGuk6Te3Gtjwb5dE55IOeF1EfBsSodusSaC65shAn0TRBgWce25Jb48r4"
		symbol_loc = tracker.get_slot('symbol')

		json_obj = requests.get("https://api.worldtradingdata.com/api/v1/stock?symbol="+ symbol_loc + "&api_token="+ api_token)

		json = json_obj.json()

		ticker_symbol = json_obj['data'][0]['symbol']
		company_name = json_obj['data'][0]['name']
		currency = json_obj['data'][0]['currency']
		close = json_obj['data'][0]['price']
		open = json_obj['data'][0]['price_open']
		high = json_obj['data'][0]['day_high']
		low = json_obj['data'][0]['day_low']
		volume = json_obj['data'][0]['volume']

		response = "\t{} \n Company : {} \n currency : {} \n close : {} \n open : {} \n high : {} \n low : {} \n volume : {}"".format(ticker_symbol, company_name, currency, close, open, high, low, volume)

		dispatcher.utter_message(response)

		return [SlotSet('symbol',symbol_loc)]
