from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Sample-start')
root.size()
input_name = Label(root, text='Enter Number:')
input_name.grid(row=0, column=0)

result = Label(root, text='Result:')
result.grid(row=1, column=0)

input_text_box = Entry(root, width=25, font=25, borderwidth=2)
input_text_box.grid(row=0, column=1, columnspan=5, pady=8)

result_text_box = Entry(root, width=25, font=25, borderwidth=2)
result_text_box.grid(row=1, column=1, columnspan=5, pady=2)

info_label = Label(root,
                   text="This calculator will give Prime,Even|Odd,Factorial and Palindrome", padx=20,
                   pady=10).grid(row=2, column=0, columnspan=5)


# -----BackUp Code-----


def clear_btn():
    input_text_box.delete(0, END)
    result_text_box.delete(0, END)


def even_odd():
    global num, num1
    num = input_text_box.get()
    result_text_box.delete(0, END)
    try:
        num1 = int(num)
        if num1 % 2 == 0:
            messagebox.showinfo('Result', f'''{num} is odd Number''')
            result_text_box.insert(0, f'''{num} is Even''')
        elif num1 % 2 != 0:
            messagebox.showinfo('Result', f'''{num} is odd Number''')
            result_text_box.insert(0, f'''{num} is odd''')
        else:
            result_text_box.insert(1, "Enter Valid Number")
        input_text_box.delete(0, END)
    except ValueError:
        result_text_box.insert(0, f'''Please enter valid number...''')


def fact_btn():
    x = input_text_box.get()
    result_text_box.delete(0, END)
    # global num
    try:
        num = int(x)
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        if fact >= 200:
            messagebox.showinfo('Result', f'''Fact of {num} is {fact}''')
        else:
            result_text_box.insert(0, f'''Fact of {num} is {fact}''')
    except ValueError:
        result_text_box.insert(0, f'''Please Enter Valid Number''')


def prime_btn():
    x = input_text_box.get()
    result_text_box.delete(0, END)
    try:
        y = int(x)
        subprime = True
        z = 2
        while z <= y-1:
            if y % z == 0:
                subprime = False
                break
            z = z + 1
        if subprime:
            result_text_box.insert(0, f'''{y} is a prime number''')
        else:
            result_text_box.insert(0, f'''{y} is a not a prime number''')
        input_text_box.delete(0, END)
    except ValueError:
        result_text_box.insert(0, f'''Invalid Number''')
        # for i in range(z, y - 1):
        #     if i % 2 == 0:
        #         subprime = False
        #         break


def palin_btn():
    pick_no = input_text_box.get()
    result_text_box.delete(0, END)
    try:
        pick_num = int(pick_no)
        temp = pick_num
        res = 0
        while pick_num > 0:
            last_num = pick_num % 10
            pick_num = pick_num // 10
            res = (res * 10) + last_num

        if res == temp:
            result_text_box.insert(0, f'''{temp} is palindrome number''')
        else:
            result_text_box.insert(0, f'''{temp} is not palindrome number''')
        input_text_box.delete(0, END)
    except ValueError:
        result_text_box.insert(0, f'''Please Enter Valid Number''')


prime_button = Button(root, text='Prime', padx=20, pady=10, command=prime_btn)
Even_odd_button = Button(root, text='Even_odd', padx=8, pady=10, command=even_odd)
Fact_button = Button(root, text='Fact', padx=26, pady=10, command=fact_btn)
palindrome_button = Button(root, text='Palin', padx=23, pady=10, command=palin_btn)
clear = Button(root, text='Clear', padx=23, pady=10, command=clear_btn)

prime_button.grid(row=3, column=2)
Even_odd_button.grid(row=4, column=1)
clear.grid(row=4, column=2)
Fact_button.grid(row=4, column=3)
palindrome_button.grid(row=5, column=2)

root.mainloop()
