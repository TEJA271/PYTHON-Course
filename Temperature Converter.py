import tkinter as tk

def convert():
    try:
        temp = float(entry.get())
        if var.get() == "Celsius":
            result.config(text=f"{(temp - 32) * 5/9:.2f} °C")
        else:
            result.config(text=f"{(temp * 9/5) + 32:.2f} °F")
    except ValueError:
        result.config(text="Invalid input")

root = tk.Tk()
root.title("Temperature Converter")

tk.Label(root, text="Temperature:").pack()
entry = tk.Entry(root)
entry.pack()

var = tk.StringVar(value="Fahrenheit")
tk.Radiobutton(root, text="To Celsius", variable=var, value="Celsius").pack()
tk.Radiobutton(root, text="To Fahrenheit", variable=var, value="Fahrenheit").pack()

tk.Button(root, text="Convert", command=convert).pack()
result = tk.Label(root, text="Result will appear here")
result.pack()

root.mainloop()

