from tkinter import *
from requests import *


root = Tk()
root.title("motivational msg")
root.geometry("1000x800+50+50")
#root.iconbitmap("santa.ico")
root.configure(bg="red2")
f=("Arial" , 30,"bold")

def gm():
	try:
		url = "https://zenquotes.io/api/random"
		res = get(url)
		if res.status_code == 200:
			data = res.json()
			quote = data[0]['q']
			author = data[0]['a']
			msg = "quote = " + str(quote) + "author =" +str(author)
			lab.configure(text=msg)
		else:	
			lab.configure("issue" + str(res.status_code))
	
	except Exception as e:
		lab.configure("issue" + str(e))
	
btn=Button(root,text="Get Msg",font=f,command=gm)
lab=Label(root,font=f, wraplength=700)
btn.pack(pady=10)
lab.pack(pady=10)


root.mainloop()
	

