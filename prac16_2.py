from tkinter import *
tk = Tk()
tk.title('Rotating')
canvas = Canvas(tk, width=640, height=480, bg='white')
canvas.pack()

def paint(x1, y1, x2, y2, x3, y3, x4, y4):
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, fill='green', outline='black')
    diapason=1
    while diapason < 50:
        diapason=diapason+1
        canvas.create_line(140,20,140,21)
    tk.update()
    canvas.create_rectangle(x1, 60, 140, 280, fill='white', outline='white')
    canvas.create_line(140,20,140,340)

for x in range(5):
    for x in range(40,240,20):
        paint(x, 240, x, 100, 140, 60, 140, 280)
        for x in range(240,40,-20):
            paint(x, 240, x, 100, 140, 60, 140, 280)
            
canvas.create_polygon(40, 240, 40, 100, 140, 60, 140, 280, fill='green', outline='black')

tk.mainloop()