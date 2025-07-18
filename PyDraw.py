import tkinter as tk

def paint(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x+4, y+4, fill="black")

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()
canvas.bind("<B1-Motion>", paint)
root.mainloop()
