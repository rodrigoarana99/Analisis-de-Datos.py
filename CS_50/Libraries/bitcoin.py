import sys
import requests


# Make a request to the API
#response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

# Parse the JSON response
#data = response.json()

# Extract the current price of Bitcoin in USD
#bitcoin_price_usd = float(data['bpi']['USD']['rate'].replace(',', ''))
#x= int(input("cuantos bitcions queres:"))
# Print the current price of Bitcoin in USD
#print(f"The current price of Bitcoin in USD is: ${bitcoin_price_usd*x:.2f}")

import sys
import requests

import requests

try:
    request= requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    x= int(input("cuantos bitcions queres:"))
    o= request.json()
    for i in o:
        if i == "bpi":
            for j in o[i]:
                if j == "USD":
                    print(f"The current price of Bitcoin in USD is: ${float(o[i][j]['rate'].replace(',',''))*x:.2f}")
except requests.RequestException:
    print("Error en la solicitud")
    sys.exit(1)