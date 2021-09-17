#!/usr/bin/env python3
import requests

class bitcoin_price_index:
    def __init__(self):
        # Get request fetching the latest bitcoin price index in json format
        self.response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

    def on_connection(self):
        print(f"""
{self.response['chartName']}
├ {self.response['bpi']['EUR']['code']}
├─ Rate: {self.response['bpi']['EUR']['rate']}
├── Rate Float: {self.response['bpi']['EUR']['rate_float']}
├─ Symbol: {self.response['bpi']['EUR']['symbol']}
└─╼ Desription: {self.response['bpi']['EUR']['description']}  
├ {self.response['bpi']['GBP']['code']}
├─ Rate: {self.response['bpi']['GBP']['rate']}
├── Rate Float: {self.response['bpi']['GBP']['rate_float']}
├─ Symbol: {self.response['bpi']['GBP']['symbol']}
└─╼ Desription: {self.response['bpi']['GBP']['description']}
├ {self.response['bpi']['USD']['code']}
├─ Rate: {self.response['bpi']['USD']['rate']}
├── Rate Float: {self.response['bpi']['USD']['rate_float']}
├─ Symbol: {self.response['bpi']['USD']['symbol']}
└─╼ Desription: {self.response['bpi']['USD']['description']}
├ {self.response['bpi']['GBP']['code']}
├─ Rate: {self.response['bpi']['GBP']['rate']}
├── Rate Float: {self.response['bpi']['GBP']['rate_float']}
├─ Symbol: {self.response['bpi']['GBP']['symbol']}
└─╼ Desription: {self.response['bpi']['GBP']['description']}
├ Updated on: {self.response['time']['updated']}
├─ Updated ISO: {self.response['time']['updatedISO']}
├── Updated UK: {self.response['time']['updateduk']}
└─╼ Disclaimer: {self.response['disclaimer']}""")

if __name__ == "__main__":
	print("Connecting...")
	while True:
		try:
			bitcoin_price_index().on_connection()
			break
			
		except Exception as e:
			print(f"An error occured: {e}")
			print("Reconnecting...")
			
		except KeyboardInterrupt:
			exit()
