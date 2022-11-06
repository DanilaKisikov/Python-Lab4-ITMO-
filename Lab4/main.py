import tkinter as tk

window = tk.Tk()
window.title('Super key generator')
window.geometry('600x400')
window.resizable(width='False', height='False')


photo = tk.PhotoImage(file='stellaris.png')
back = tk.Label(window, image=photo, bg='grey')
back.place(x=0, y=0, width=600, height=400)

poolOfNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def close():
    window.destroy()


def calc():
    a = FirstPart.get()
    second_part = ''
    third_part = ''

    if len(a) == 5:
        a = str.upper(a)
        for i in a:
            second_part += poolOfNumbers[poolOfNumbers.index(i) + 3]
            third_part += poolOfNumbers[poolOfNumbers.index(i) - 5]
        lbl_roots.configure(text=a + '---' + second_part + '---' + third_part)

    else:
        lbl_roots.configure(text='Введите 5 символов')


lblFirstPart = tk.Label(window, text='First part of key', font=('Arial', 30))
lblFirstPart.place(relx=0.5, rely=0.2, anchor='center')
FirstPart = tk.Entry(window, width=10)
FirstPart.place(relx=0.5, rely=0.4, anchor='center')

lbl_roots = tk.Label(window, text='', font=('Arial', 15))
lbl_roots.place(relx=0.5, rely=0.5, anchor='center')

btn_calc = tk.Button(window, text='Calculate', font=('Arial', 15), command=calc, bg='#952233')
btn_calc.place(relx=0.4, rely=0.6, anchor='center')
btn_exit = tk.Button(window, text=' Cancel  ', font=('Arial', 15), command=close)
btn_exit.place(relx=0.6, rely=0.6, anchor='center')

window.mainloop()
