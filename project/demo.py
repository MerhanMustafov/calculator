# def click():
#     output.delete(0, 'end')
#     deliminator = [el for el in input_entry.get() if not el.isdigit() and not el.isspace()]
#     if deliminator:
#         deliminator = deliminator[0]
#         first_num, sec_num = input_entry.get().split(deliminator[0])
#         first_num.strip(), sec_num.strip()
#
#         if sec_num:
#             first_num, sec_num= float(first_num), float(sec_num)
#
#             result = 0
#             if deliminator == '*':
#                 result = first_num * sec_num
#             elif deliminator == '+':
#                 result = first_num + sec_num
#             elif deliminator == '-':
#                 result = first_num - sec_num
#             elif deliminator == '/':
#                 result = first_num / sec_num
#
#
#             return output.insert(0, result)
#
#
#
#
#
# from tkinter import *
# from tkinter import font
#
# window = Tk(className=" calculator")
# window.configure(bg='#222222')
# window.geometry('350x300')
#
# myFont = font.Font(family='bold', size=23)
# inputFont = font.Font(size=10)
#
# input_entry = Entry(window, border = 5)
# input_entry['font'] = inputFont
# input_entry.place(x=15, y=40)
#
# output = Entry(window, border = 5)
# output['font'] = inputFont
# output.place(x=180, y=40)
#
#
# enterButton = Button(window, text="calculate", font = myFont, border = 5, command=click)
# enterButton.place(x=90, y=100)
# enterButton['font'] = myFont
#
# button_1 = Button(window, text='1', command= click).place(x= 80, y=70, width = 40)
# button_2 = Button(window, text='2', command= click).place(x= 130, y = 70, width=40)
# button_3 = Button(window, text='3', command= click).place(x= 180, y = 70, width=40)
#
# button_4 = Button(window, text='4', command= click).place(x= 80, y = 100, width=40)
# button_5 = Button(window, text='5', command= click).place(x= 130, y = 100, width=40)
# button_6 = Button(window, text='6', command= click).place(x= 180, y = 100,width=40)
#
# button_7 = Button(window, text='7', command= click).place(x= 80, y = 130, width=40)
# button_8 = Button(window, text='8', command= click).place(x= 130, y = 130, width=40)
# button_9 = Button(window, text='9', command= click).place(x= 180, y = 130, width=40)
#
# button_0 = Button(window, text='0', command= click).place(x= 130, y = 160, width=40)
#
#
# window.mainloop()


nums = '5*5'
s = eval(nums)
print(s)