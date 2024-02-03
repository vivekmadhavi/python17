#pip install requests

from requests import *
try:
	url = "https://zenquotes.io/api/random"
	res = get(url)
	if res.status_code == 200:
		data = res.json()
		print(data)
		quote = data[0]['q']
		print("msg = ",quote)
		author = data[0]['a']
		print("author " , author)
	else:	
		print("issue",res.status_code)

except Exception as e:
	print("issue",e)