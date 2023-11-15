import time
from tkinter import *
tk = Tk()
tk.title('Rainbow')
canvas = Canvas(tk, width=500, height=500, bg='white')
canvas.pack()

canvas.create_arc(210, 450, 290, 700,width = 35, outline = "purple", extent = 180, style=ARC)
canvas.create_arc(180, 420, 320, 700,width = 35, outline = "blue", extent = 180, style=ARC)
canvas.create_arc(150, 390, 350, 710,width = 35, outline = "cyan", extent = 180, style=ARC)
canvas.create_arc(120, 360, 380, 720,width = 35, outline = "green", extent = 180, style=ARC)
canvas.create_arc(90, 330, 410, 730,width = 35, outline = "yellow", extent = 180, style=ARC)
canvas.create_arc(60, 300, 440, 740,width = 35, outline = "orange", extent = 180, style=ARC)
canvas.create_arc(30, 270, 470, 750,width = 35, outline = "red", extent = 180, style=ARC)

time.sleep(1)
for i in range(7,0,-1):
    canvas.move(i, 0, -50)
    tk.update()
    time.sleep(1)

for i in range(1, 8):
    canvas.move(i, 0, 50)
    tk.update()
    time.sleep(1)

tk.mainloop()