from tkinter import *
from requests import *

root = Tk()
root.title=("currency converter")
root.geometry("800x700+50+50")
f = ("Arial" , 30,"bold")
y=10

def gets():
	try:
		url = "https://api.exchangerate-api.com/v4/latest/USD"
		res= get(url)
		data = res.json()
		USD = data["rates"]["INR"]
		try:
			aid = float(amt.get())
			air = aid * USD
			air = round(air,2)
			msg = "\u20b9"+ str(air)
			labans.configure(text=msg)
		except ValueError:
			lab.configure("issue")
	except Exception as e:
		lab.configure("issue " , str(e))

lab =Label(root,text="enter  amt in $$",font=f)
amt = Entry(root,font=f)
btn = Button(root,text="check",font=f,command=gets)
labans =Label(root,font=f)


lab.pack(pady=y)
amt.pack(pady=y)
btn.pack(pady=y)
labans.pack(pady=y)

root.mainloop()	