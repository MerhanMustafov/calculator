def click():
    deliminator = [el for el in input_entry.get() if not el.isdigit() and not el.isspace()]
    if deliminator:
        deliminator = deliminator[0]
        first_num, sec_num = input_entry.get().split(deliminator[0])
        first_num.strip(), sec_num.strip()

        if sec_num:
            first_num, sec_num= float(first_num), float(sec_num)

            result = 0
            if deliminator == '*':
                result = first_num * sec_num
            elif deliminator == '+':
                result = first_num + sec_num
            elif deliminator == '-':
                result = first_num - sec_num
            elif deliminator == '/':
                result = first_num / sec_num


            return output.insert(0, result)





from tkinter import *
from tkinter import font

window = Tk(className=" calculator")
window.configure(bg='#74D3FF')
window.geometry('350x300')

myFont = font.Font(family='bold', size=23)
inputFont = font.Font(size=10)

input_entry = Entry(window, border = 5)
input_entry['font'] = inputFont
input_entry.place(x=15, y=40)

output = Entry(window, border = 5)
output['font'] = inputFont
output.place(x=180, y=40)


enterButton = Button(window, text="calculate", font = myFont, border = 5, command=click)
enterButton.place(x=90, y=100)
enterButton['font'] = myFont

window.mainloop()
