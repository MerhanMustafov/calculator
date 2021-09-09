from tkinter import *
from tkinter import ttk, Canvas

# from docutils.nodes import row
from turtle import width

from docutils.nodes import row


def calculate():
    print('Sth')

window = Tk()
window.geometry('500x300')


entry_box_one = Entry(window).grid(row = 1,column=1)
lable_one = Label(window, text='Type in here: ').grid(row=1)
operator = Button(window, text = "Operator should be here", command =calculate).grid(row=1, column= 2)
entry_box_two = Entry(window).grid(row = 1,column=3)
equl_button = Button(window, text = "=", command =calculate).grid(row=1, column= 4)

result_lable = Label(window, font = 1, fg='black',text='Result: ').place(x=5, y= 30)
result_box = Entry(window).place(x = 75,y=30, width = 250, height = 30)

# TODO Button
button_1 = Button(window, text='1').place(x= 80, y=70, width = 40)
button_2 = Button(window, text='2').place(x= 130, y = 70, width=40)
button_3 = Button(window, text='3').place(x= 180, y = 70, width=40)

button_4 = Button(window, text='4').place(x= 80, y = 100, width=40)
button_5 = Button(window, text='5').place(x= 130, y = 100, width=40)
button_6 = Button(window, text='6').place(x= 180, y = 100,width=40)

button_7 = Button(window, text='7').place(x= 80, y = 130, width=40)
button_8 = Button(window, text='8').place(x= 130, y = 130, width=40)
button_9 = Button(window, text='9').place(x= 180, y = 130, width=40)

button_0 = Button(window, text='0').place(x= 130, y = 160, width=40)


separator = ttk.Separator(window, orient='vertical')
separator.place(relx=0.47, rely=0.24, relwidth=0.2, relheight=0.4)


button_plus = Button(window, text='+').place(x= 245, y = 70, width=40)
button_minus = Button(window, text='-').place(x= 245, y = 100, width=40)
button_multiply = Button(window, text='*').place(x= 245, y = 130, width=40)
button_divide = Button(window, text='÷').place(x= 245, y = 160, width=40)


window.mainloop()