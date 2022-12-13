# import tkinter module
from tkinter import *

# make a window
window = Tk()

# specify it's size
window.geometry("700x600")




# function to calculate the
# price of all the orders
def calculate():

		# dic for storing the
	# food quantity and price
	dic = {'Soap': [e1, 27],
		'Toothbrush': [e2, 5],
		'Detergent': [e3, 150],
		'Copy': [e4, 50],
		'Practical File': [e5, 70],
		'Pilot Pen': [e6, 33.25],
        'Lotte Choco Pie':[e7,25],
        'Britania Cake':[e8,60]}
	total = 0
	for key, val in dic.items():
		if val[0].get() != "":
			total += float(val[0].get())*val[1]
			

	label166 = Label(window,
					text="Your Total Bill is - "+str(total),
					font="times 18")

	# position it
	label166.place(x=20, y=490)
	label166.after(1000, label166.destroy)
	window.after(1000, calculate)

	button12 = Button(window,text="Pay",font="times 18")
	button12.place(x=10,y=520)
	button12.configure(command=new_customer)


label8 = Label(window,
			text="Akshay Super Market",
			font="times 28 bold")
label8.place(x=350, y=20, anchor="center")


label1 = Label(window,
			text="Catalogue",
			font="times 28 bold")

label1.place(x=520, y=40)

label2 = Label(window, text="Toileteries \
", font="times 22 bold")

label2.place(x=450, y=120)

label3 = Label(window, text="Soap \
Rs 30", font="times 18")

label3.place(x=450, y=150)

label4 = Label(window, text="ToothBrush Rs 5"	\
, font="times 18")
label4.place(x=450, y=180)

label5 = Label(window, text="Detergent \
Rs 150", font="times 18")

label5.place(x=450, y=210)

label6 = Label(window, text="Stationary \
", font="times 22 bold")

label6.place(x=450, y=240)

label7 = Label(window, text="Copy \
Rs 50(20%off)", font="times 18")

label7.place(x=450, y=270)

label8 = Label(window, text="Practical File \
Rs 70", font="times 18")

label8.place(x=450, y=300)

label9 = Label(window, text="Pilot Pen \
Rs 35", font="times 18")

label9.place(x=450, y=330)

label10 = Label(window, text="Eateries \
", font="times 22 bold")

label10.place(x=450, y=360)

label11 = Label(window, text="Lotte Choco Pie \
Rs 25", font="times 18")

label11.place(x=450, y=390)

label12 = Label(window, text="Britania Cake \
Rs 30", font="times 18")

label12.place(x=450, y=420)

label13 = Label(window, text="Cocacola \
Rs 40", font="times 18")

label13.place(x=450, y=450)


# billing section
label14 = Label(window, text="Select the items",
			font="times 18")
label14.place(x=115, y=70)

label15 = Label(window,
				text="Soap",
				font="times 18")
label15.place(x=20, y=120)

e1 = Entry(window)
e1.place(x=20, y=150)

label166 = Label(window, text="ToothBrush",
				font="times 18")
label166.place(x=20, y=200)

e2 = Entry(window)
e2.place(x=20, y=230)

label17 = Label(window, text="Detergent",
				font="times 18")
label17.place(x=20, y=280)

e3 = Entry(window)
e3.place(x=20, y=310)

label18 = Label(window,
				text="Copy",
				font="times 18")
label18.place(x=20, y=360)

e4 = Entry(window)
e4.place(x=20, y=390)

label19 = Label(window,
				text="Practical File",
				font="times 18")
label19.place(x=250, y=120)

e5 = Entry(window)
e5.place(x=250, y=150)

label20 = Label(window,
				text="Pilot Pen",
				font="times 18")

label20.place(x=250, y=200)

e6 = Entry(window)
e6.place(x=250, y=230)

label21 = Label(window,
				text="Lotte Choco Pie",
				font="times 18")

label21.place(x=250, y=280)

e7 = Entry(window)
e7.place(x=250, y=310)


label22 = Label(window,
				text="Britania Cake",
				font="times 18")

label22.place(x=250, y=360)

e8 = Entry(window)
e8.place(x=250, y=390)


label23 = Label(window,
				text="Cocacola",
				font="times 18")

label23.place(x=250, y=410)

e9 = Entry(window)
e9.place(x=250, y=450)

# execute calculate function after 1 second
window.after(1000, calculate)



def new_customer():
    window = Tk()
    window.title("New Customer")
    window.geometry("400x200")

    lbl_name = Label(window, text="Name: ")
    lbl_name.grid(row=0, column=0)
    entry_name = Entry(window)
    entry_name.grid(row=0, column=1)

    lbl_id = Label(window, text="ID: ")
    lbl_id.grid(row=1, column=0)
    entry_id = Entry(window)
    entry_id.grid(row=1, column=1)

    btn_save = Button(window, text="Save")
    btn_save.grid(row=2, column=1)
    btn_save.configure(command=payement)

    window.mainloop()


def payement():
	window = Tk()
	window.title("Trancsaction")
	window.geometry("700x600")
	label11 = Label(window,text="Choose an option for payement",font="times 28")
	label11.place(x=100,y=100)
	button12 = Button(window,text="Deduct money from swd account",font="times 20")
	button12.configure(command=swd)
	button12.place(x=100,y=180)
	label13 = Button(window,text="UPI",font="times 20")
	label13.place(x=150,y=260)
	label13.configure(command=upi)

	window.mainloop()

def swd():
	window = Tk()
	window.geometry("500x500")
	label123 = Label(window,text="Amount deducted from SWD Acoount",font="times 18 bold")
	label123.place(x=50,y=50)

def upi():
	window = Tk() 
	window.geometry("600x400")
	
	lbl_name = Label(window, text="UPI ID: ")
	lbl_name.grid(row=0, column=0)
	entry_name = Entry(window)
	entry_name.grid(row=0, column=1)

	lbl_id = Label(window, text="PIN: ")
	lbl_id.grid(row=1, column=0)
	entry_id = Entry(window,show="*")
	entry_id.grid(row=1, column=1)

	btn = Button(window,text="Pay")
	btn.grid(row=2,column=0)




bl1 = Label(window, text="Enter item to search",font="times 20 bold")
bl1.place(x=90,y=40)
txt = Entry(window, width=20)
txt.place(x=340,y=50)


def search():

	dic = {'Soap': [e1, 30],
		'Toothbrush': [e2, 5],
		'Detergent': [e3, 150],
		'Copy': [e4, 50],
		'Practical File': [e5, 70],
		'Pilot Pen': [e6, 35],
        'Lotte Choco Pie':[e7,25],
        'Britania Cake':[e8,30]}
	item = txt.get()
	if (item in dic.keys()):
		lbl2 = Label(window, text="The item '" + item + "' is available")
		lbl2.grid(column=1, row=3)
	else:
		lbl2 = Label(window, text="The item '" + item + "' is not available")
		lbl2.grid(column=1, row=3)


btn22 = Button(window, text="Search", command=search)
btn22.place(x=450,y=45)


btn23 = Button(window,text = "Discounts",font="times 25 bold")
btn23.place(x=400,y=500)
#btn23.configure(command=disc)

def disc():
	window=Tk()
	window.geometry("300x200")
	label1234 = Label(window,text="Soap : 20% off\nPilot Pen : 5%off\nBritania Cake: Buy one get one free",font="times 18")
	label1234.place(x=0,y=50)
btn23.configure(command=disc)
# closing the main loop
btn24=Button(window,text="Admin",font="times 18 bold")
btn24.place(x=10,y=0)

def admin():
	window=Tk()
	window.geometry("700x600")
	label1235=Label(window,text="Commodity\t\t\tMRP\t\t\tProfit",font="times 25 bold")
	label1235.place(x=100,y=100)
	label1236=Label(window,text="Soap\t\t\t\t30\t\t\t15",font="times 25 bold")
	label1236.place(x=100,y=180)
	label1237=Label(window,text="ToothBrush\t\t\t5\t\t\t2",font="times 25 bold")
	label1237.place(x=100,y=240)
	label1238=Label(window,text="Detergent\t\t\t150\t\t\t100",font="times 25 bold")
	label1238.place(x=100,y=300)
	label1239=Label(window,text="Copy\t\t\t\t50\t\t\t20",font="times 25 bold")
	label1239.place(x=100,y=360)
	label1240=Label(window,text="Practical File\t\t\t70\t\t\t30",font="times 25 bold")
	label1240.place(x=100,y=420)
	label1241=Label(window,text="Pilot Pen\t\t\t\t35\t\t\t15",font="times 25 bold")
	label1241.place(x=100,y=480)
	label1242=Label(window,text="Lotte Choco Pie\t\t\t25\t\t\t10",font="times 25 bold")
	label1242.place(x=100,y=540)
	label1243=Label(window,text="Britania Cake\t\t\t30\t\t\t15",font="times 25 bold")
	label1243.place(x=100,y=600)
	label1244=Label(window,text="Cocacola\t\t\t\t40\t\t\t15",font="times 25 bold")
	label1244.place(x=100,y=660)



#new admin page

def new_admin():
	window = Tk()
	window.title("Admin Login")
	window.geometry("400x200")

	lbl_pass = Label(window, text="Password: ")
	lbl_pass.grid(row=0, column=0)
	entry_pass = Entry(window, show="*")
	entry_pass.grid(row=0, column=1)

	btn_login = Button(window, text="Login")
	btn_login.grid(row=1, column=1)
	btn_login.configure(command=admin)

	 
	
	



#link admin login button with new admin page
btn24.configure(command=new_admin)








window.mainloop()
