from tkinter import *


def Even_odd(num):
    if num % 2 == 0:
        return f'''{num} is Even'''
    else:
        return f'''{num} is Odd'''


main = Tk(screenName='Demo', baseName='Demo1')
text_number = Label(main, text='Enter Number').grid(row=0, column=0)
e1 = Entry(main).grid(row=0, column=1)


button1 = Button(main, text='Prime').grid(row=1, column=0)
# button1.pack(side=TOP)
button2 = Button(main, text='EvenORodd', command=Even_odd).grid(row=1, column=1)
# button1.pack(side=TOP)
button3 = Button(main, text='Factorial').grid(row=1, column=2)

# button1.pack(side=TOP)
button4 = Button(main, text='EvenORodd').grid(row=1, column=3)

# button1.pack(side=TOP)


main.mainloop()
