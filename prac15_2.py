from tkinter import *
import imageio
tk = Tk()
tk.title('Rainbow')
canvas = Canvas(tk, width=1250, height=700, bg='white')
canvas.pack()

canvas.create_text(210, 230, text="""
Step forward and meet a new sunrise
A coward is shivering inside
Today, I'll, I'll be a friend of mine
Who swallows suffering with smile
I drew a different reality
With unconditional loyalty
Ego hardly can be piqued
'Cause I'm selfless
                   
Scale armour blaze
Virgin innocence
One being brings life
Another runs for death
Scale armour blaze
Virgin innocence
One being brings life
Another runs for death""",font=("Comic Sans",18))

band = PhotoImage(file="band.png")
canvas.create_image(450, 0, anchor=NW, image=band)
notes = PhotoImage(file="notes.gif")
canvas.create_image(150, 450, anchor=NW, image=notes)

tk.mainloop()