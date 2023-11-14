from tkinter import *
tk = Tk()
tk.title('Pyramid')
canvas = Canvas(tk, width=900, height=700, bg='white')
canvas.pack()

widthMinus = 15
gap = 20

for i in range(30):
    if i < 10:
        canvas.create_line(0 + widthMinus * i,700 - gap * i, 900 - widthMinus * i, 700 - gap * i, width=15, fill="red")
    elif i < 20:
        canvas.create_line(0 + widthMinus * i,700 - gap * i, 900 - widthMinus * i, 700 - gap * i, width=15, fill="yellow")
    elif i < 30:
        canvas.create_line(0 + widthMinus * i,700 - gap * i, 900 - widthMinus * i, 700 - gap * i, width=15, fill="green")

tk.mainloop()