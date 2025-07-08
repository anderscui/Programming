# coding=utf-8
import tkinter as tk
from tkinter import ttk


# handlers
# should
def add_to_list(event=None):
    text = entry.get()
    if text:
        lst_text.insert(tk.END, text)
        entry.delete(0, tk.END)


# Tk: Toplevel widget of Tk which represents mostly the main window of an application.
window = tk.Tk()
window.title('Hello Tk')
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

frame = tk.Frame()
frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

entry = tk.Entry(frame)
entry.grid(row=0, column=0, sticky='ew')

entry.bind('<Return>', add_to_list)

btn_entry = tk.Button(frame, text='add', command=add_to_list)
btn_entry.grid(row=0, column=1)

lst_text = tk.Listbox(frame)
# sticky: east and west
lst_text.grid(row=1, column=0, columnspan=2, sticky='nsew')

entry.focus()

window.mainloop()
