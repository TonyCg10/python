import tkinter as tk
from tkinter import ttk


def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "DEL":
        entry.delete(len(entry.get()) - 1)
    else:
        entry.insert(tk.END, text)


root = tk.Tk()
root.title("Calculadora Moderna")
root.resizable(False, False)

style = ttk.Style()
style.configure("TButton", padding=10, font=("Helvetica", 12))

entry = tk.Entry(root, width=25, borderwidth=5, font=("Helvetica", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7",
    "8",
    "9",
    "/",
    "4",
    "5",
    "6",
    "*",
    "1",
    "2",
    "3",
    "-",
    ".",
    "0",
    "=",
    "+",
    "C",
    "DEL",
]

row = 1
col = 0
for button_text in buttons:
    button = ttk.Button(root, text=button_text)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", on_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
