import tkinter as tk
from tkinter import filedialog

def save_note():
    content = text.get("1.0", tk.END)
    file = filedialog.asksaveasfilename(defaultextension=".md")
    if file:
        with open(file, "w") as f:
            f.write(content)

root = tk.Tk()
root.title("PyNotes")

text = tk.Text(root)
text.pack(expand=True, fill="both")

btn = tk.Button(root, text="Save", command=save_note)
btn.pack()

root.mainloop()
