from tkinter import *

window=Tk()
window.geometry("700x500")

menu=Label(window,text="Menu", font="Ariel 25 bold")
menu.place(x=0,y=70)

#Menu

#tea(☕)
tea=Label(window,text="Tea",font="Ariel 16")
tea.place(x=0,y=150)
tea_price=Label(window,text="Rs.5",font="Ariel 12")
tea_price.place(x=100,y=153) 

#coffee(☕)
coffee=Label(window,text="Coffee",font="Ariel 16")
coffee.place(x=0,y=200)
coffee_price=Label(window,text="Rs.7",font="Ariel 12")
coffee_price.place(x=100,y=203)

#samosa()
samosa=Label(window,text="Samosa",font="Ariel 16")
samosa.place(x=0,y=250)
samosa_price=Label(window,text="Rs.12",font="Ariel 12")
samosa_price.place(x=100,y=253)

#French Fries
frenchfries=Label(window,text="Fries",font="Ariel 16")
frenchfries.place(x=0,y=300)
frenchfries_price=Label(window,text="Rs.100",font="Ariel 12")
frenchfries_price.place(x=100,y=303)



#Quantity

#tea
tea_quantity=Label(window,text="Tea", font="Ariel 16")
tea_quantity.place(x=300,y=150)
tea_entry=Entry(window)
tea_entry.place(x=300,y=180)

#coffee
coffee_quantity=Label(window,text="Coffee", font="Ariel 16")
coffee_quantity.place(x=500,y=150)
coffee_entry=Entry(window)
coffee_entry.place(x=500,y=180)

#samosa
samosa_quantity=Label(window,text="Samosa", font="Ariel 16")
samosa_quantity.place(x=300,y=230)
samosa_entry=Entry(window)
samosa_entry.place(x=300,y=260)

#Fries
frenchfries_quantity=Label(window,text="Fries", font="Ariel 16")
frenchfries_quantity.place(x=300,y=310)
frenchfries_entry=Entry(window)
frenchfries_entry.place(x=300,y=340)

def calculate():
    tea_box=int(tea_entry.get())
    coffee_box=int(coffee_entry.get())
    samosa_box=int(samosa_entry.get())
    frenchfries_box= int(frenchfries_entry.get())

    total=str("Rs"),tea_box*5+coffee_box*7+samosa_box*12+frenchfries_box*100
    
    #bill statement
    billed_amt=Label(window,text=total, font="Ariel 25 bold")
    billed_amt.place(x=500,y=400)


#button
bill=Button(window,text="Bill",width=20,command=calculate)
bill.place(x=500,y=300)



#mainloop(dont touch😤)
window.mainloop()