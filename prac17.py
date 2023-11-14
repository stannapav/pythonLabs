from tkinter import *
import random
tk = Tk()
tk.title('cubes')
canvas = Canvas(tk, width=600, height=600, bg='black')
canvas.pack()

colors = ['red', 'salmon', 'tomato', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 
          'brown1', 'brown2', 'brown3', 'brown4', 'red2', 'red3', 'red4', 'salmon1',
           'salmon2', 'salmon3', 'salmon4', 'salmon', 'indian red']

for i in range(1000):
    color = random.choice(colors)
    x = random.randint(0,600)
    y = random.randint(0,600)
    addx = random.randint(-50, 50)
    addy = random.randint(-50, 50)
    canvas.create_rectangle(x, y, x + addx, y + addy, fill = color, outline = color)

tk.mainloop()