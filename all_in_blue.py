
import tkinter as tk


def onclick_1():
    if  (b1['bg']== '#ffffff'):
        b1.config(bg =blue_Colour)
def onclick_2():
    if  (b2['bg']== '#ffffff'):
        b2.config(bg =blue_Colour)
def onclick_3():
    if  (b3['bg']== '#ffffff'):
        b3.config(bg =blue_Colour)
def onclick_4():
    if  (b4['bg']== '#ffffff'):
        b4.config(bg =blue_Colour)
def onclick_5():
    if  (b5['bg']== '#ffffff'):
        b5.config(bg =blue_Colour)
def onclick_6():
    if  (b6['bg']== '#ffffff'):
        b6.config(bg =blue_Colour)
def onclick_7():
    if  (b7['bg']== '#ffffff'):
        b7.config(bg =blue_Colour)
def onclick_8():
    if  (b8['bg']== '#ffffff'):
        b8.config(bg =blue_Colour)
def onclick_9():
    if  (b9['bg']== '#ffffff'):
        b9.config(bg =blue_Colour)


   



        
    

window = tk.Tk()
window.title ("Blue vs Red")
red_Colour= '#f24444'
blue_Colour= '#446df2'





b1= tk.Button(relief= 'solid', width= 7, bg= '#ffffff', height= 3, command= lambda:onclick_1())
b1.grid(column= 0, row= 0)
b2= tk.Button(relief= 'solid', width= 7, bg = '#ffffff', height= 3, command= lambda: onclick_2())
b2.grid(column=1, row=0)
b3= tk.Button(relief= 'solid', width= 7, bg = '#ffffff', height= 3, command= lambda:onclick_3())
b3.grid(column=2, row=0)
b4= tk.Button(relief= 'solid', width= 7, bg= '#ffffff', height= 3, command= lambda:onclick_4())
b4.grid(column= 0, row= 2)
b5= tk.Button(relief= 'solid', width= 7, bg = '#ffffff', height= 3, command= lambda:onclick_5())
b5.grid(column=1, row=2)
b6= tk.Button(relief= 'solid', width= 7, bg = '#ffffff', height= 3, command= lambda:onclick_6())
b6.grid(column=2, row=2)
b7= tk.Button(relief= 'solid', width= 7, bg= '#ffffff', height= 3, command= lambda:onclick_7())
b7.grid(column= 0, row= 3)
b8= tk.Button(relief= 'solid', width= 7, bg = '#ffffff', height= 3, command= lambda:onclick_8())
b8.grid(column=1, row=3)
b9= tk.Button(relief= 'solid', width= 7, bg = '#ffffff', height= 3, command= lambda:onclick_9())
b9.grid(column=2, row=3)


window.mainloop()