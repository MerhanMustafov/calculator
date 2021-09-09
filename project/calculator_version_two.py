def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def press_equal_result():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = ''
    except:
        equation.set('error')
        expression=''
def press_clear():
    global expression
    expression = ''
    equation.set('')


from tkinter import *
from tkinter import ttk



expression = ''


window = Tk(className=" CALCULATOR")
window.geometry('300x200')
equation = StringVar()

entry_box_one = Entry(window,  textvariable=equation)
entry_box_one.place(x = 5,y=5, width = 155, height = 27)


# TODO Button
button_1 = Button(window, font= 1,text='1', command=lambda : press(1))
button_1.place(x= 6, y=35, width = 40)
button_2 = Button(window,font= 1, text='2', command= lambda : press(2))
button_2.place(x= 47, y=35, width=40)
button_3 = Button(window, font= 1,text='3', command= lambda : press(3))
button_3.place(x= 88, y=35, width=40)

button_4 = Button(window, font= 1,text='4', command= lambda : press(4))
button_4.place(x= 6, y=67, width=40)
button_5 = Button(window,font= 1, text='5', command= lambda : press(5))
button_5.place(x= 47, y=68, width=40)
button_6 = Button(window,font= 1, text='6', command= lambda : press(6))
button_6.place(x= 88, y=68,width=40)

button_7 = Button(window,font= 1, text='7', command= lambda : press(7))
button_7.place(x= 6, y=100, width=40)
button_8 = Button(window,font= 1, text='8', command= lambda : press(8))
button_8.place(x= 47, y=100, width=40)
button_9 = Button(window,font= 1, text='9', command= lambda : press(9))
button_9.place(x= 88, y=100, width=40)

button_0 = Button(window,font= 1, text='0', command= lambda : press(0))
button_0.place(x= 47, y=132, width=40)


separator = ttk.Separator(window, orient='vertical')
separator.place(relx=0.48, rely=0.19, relwidth=1, relheight=0.62)


button_plus = Button(window,font= 1, text='+', command=lambda : press('+'))
button_plus.place(x=162, y = 35, width=40)
button_minus = Button(window,font= 1, text='-', command=lambda : press('-'))
button_minus.place(x=162, y = 68, width=40)
button_multiply = Button(window,font= 1, text='*', command=lambda : press('*'))
button_multiply.place(x=162, y = 100, width=40)
button_divide = Button(window,font=1, text='÷', command=lambda : press('/'))
button_divide.place(x=162, y = 132, width=40)

button_equal = Button(window,font = 1, text = '=', command=press_equal_result)
button_equal.place(x=162, y = 5, width= 40, height= 27)

button_clear = Button(window,font = 1, text = "C", command = press_clear)
button_clear.place(x= 88, y=132, width=40)


window.mainloop()