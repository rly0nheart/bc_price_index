#!/usr/bin/env python3

# This is a python implementation of the CoinDesk API
# For getting Bitcoin price index

# Importing required modules
import requests
from pprint import pprint

class PriceIndex:
    def __init__(self):
        # Get request fetching the latest bitcoin price index in json format
        self.response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

    def on_connection(self):
        # The pprint module provides a capability 
        # to “pretty-print” arbitrary Python data 
        # structures in a well-formatted and more readable way.
        pprint(self.response)
        
if __name__ == "__main__":
    # Main loop
	while True:
		try:
			PriceIndex().on_connection()
			break
		except Exception as e:
			print(f"An error occured: {e}")
			print("Retrying...")
		except KeyboardInterrupt:
			exit()
