from requests import *

try:
	url = "https://api.exchangerate-api.com/v4/latest/USD"
	res= get(url)
	data = res.json()
	USD = data["rates"]["INR"]
	try:
		aid = float(input("enter amt in $$"))
		air = aid * USD
		air = round(air,2)
		msg = "\u20b9"+ str(air)
		print(msg)
	except ValueError:
		print(" u shud enter number only ")
except Exception as e:
	print("issue " , e)