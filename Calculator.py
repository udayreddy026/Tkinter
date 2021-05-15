from tkinter import *

main = Tk(screenName='Calculator')

main.title("Calculator")

Enter_num = Label(main, text="Enter Number").grid(row=0, column=0)
text_entry = Entry(main, width=25, font=25)
text_entry.grid(row=0, column=1, columnspan=4, padx=15, pady=20)


res = Label(main, text="Result").grid(row=1, column=0)
res_dis = Entry(main, width=25, font=30)
res_dis.grid(row=1, column=1, columnspan=4, padx=15, pady=20)


def button_click(num):
    enter_value = text_entry.get()
    text_entry.delete(0, END)
    text_entry.insert(0, str(enter_value) + str(num))


def button_clear():
    text_entry.delete(0, END)
    res_dis.delete(0, END)

def button_add():
    first_num = text_entry.get()
    global f_num
    global symbal
    symbal = 'add'
    f_num = int(first_num)
    text_entry.delete(0, END)
    res_dis.delete(0, END)

def button_equal():
    sec_num = text_entry.get()
    s_num = int(sec_num)
    text_entry.delete(0, END)
    if symbal == 'add':
        res_dis.insert(0, f_num + s_num)
    elif symbal == 'sub':
        res_dis.insert(0, f_num - s_num)
    elif symbal == 'mul':
        res_dis.insert(0, f_num * s_num)
    elif symbal == 'div':
        res_dis.insert(0, f_num / s_num)


def button_sub():
    first_num = text_entry.get()
    global f_num
    global symbal
    symbal = 'sub'
    f_num = int(first_num)
    text_entry.delete(0, END)
    res_dis.delete(0, END)


def button_mul():
    first_num = text_entry.get()
    global f_num
    global symbal
    symbal = 'mul'
    f_num = int(first_num)
    text_entry.delete(0, END)
    res_dis.delete(0, END)


def button_div():
    first_num = text_entry.get()
    global f_num
    global symbal
    symbal = 'div'
    f_num = int(first_num)
    text_entry.delete(0, END)
    res_dis.delete(0, END)


button_1 = Button(main,
                  text='1',
                  padx=40,
                  pady=20,
                  command=lambda: button_click(1))
button_2 = Button(main,
                  text='2',
                  padx=40,
                  pady=20,
                  command=lambda: button_click(2))
button_3 = Button(main,
                  text='3',
                  padx=40,
                  pady=20,
                  command=lambda: button_click(3))
button_4 = Button(main,
                  text='4',
                  padx=40,
                  pady=20,
                  command=lambda: button_click(4))
button_5 = Button(main,
                  text='5',
                  padx=40,
                  pady=20,
                  command=lambda: button_click(5))
button_6 = Button(main,
                  text='6',
                  padx=40,
                  pady=20,
                  command=lambda: button_click(6))
button_7 = Button(main,
                  text='7',
                  padx=40,
                  pady=20,
                  command=lambda: button_click(7))
button_8 = Button(main,
                  text='8',
                  padx=40,
                  pady=20,
                  command=lambda: button_click(8))
button_9 = Button(main,
                  text='9',
                  padx=40,
                  pady=20,
                  command=lambda: button_click(9))
button_0 = Button(main,
                  text='0',
                  padx=40,
                  pady=20,
                  command=lambda: button_click(0))
button_clear = Button(main,
                      text='clear',
                      padx=30.5,
                      pady=20,
                      command=button_clear)
button_equal = Button(main,
                      text='=',
                      padx=38.4,
                      pady=20,
                      command=button_equal)
button_add = Button(main,
                    text='+',
                    padx=38.5,
                    pady=20,
                    command=button_add)
button_sub = Button(main,
                    text='-',
                    padx=40,
                    pady=20,
                    command=button_sub)
button_mul = Button(main,
                    text='*',
                    padx=40,
                    pady=20,
                    command=button_mul)
button_div = Button(main,
                    text='/',
                    padx=40,
                    pady=20,
                    command=button_div)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_clear.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_equal.grid(row=5, column=2)

button_add.grid(row=5, column=3)
button_sub.grid(row=4, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=2, column=3)

main.mainloop()


# x = ['ab-1', 'ab-021', 'ab-201', 'ab-011', 'ab-12', 'ab-22']
# my_new_list = [i.split("-")[1] for i in x]
#
# conv_list = list(map(int, my_new_list))
# conv_list.sort()
# a = list(map(str, conv_list))
# print(a)
# final = ['ab-'+i for i in a]
# print(final)


# x = [[21, 14, 32, 5], [3, 24, 7, 43], [67, 11, 9, 1], [13, 17, 19, 23]]
# y = []
# for i in x:
#     for j in i:
#         if j % 2 == 0:
#             pass
#         else:
#             y.append(j)
# y.sort()
# for z in y:
#     print(z, end=" ")


# s = 'Welcome to Cambium Networks'
# x = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
#
# for i in s:
#     # print(i)
#     for j in x:
#         if j is i:
#             pass
#         else:
#             print(j, end=" ")
#             break

# # print(dir(str))
#
# for i in s:
#     if i is :
#         pass
#     else:
#         print(i)
