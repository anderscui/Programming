# coding=utf-8
import tkinter as tk
from tkinter import ttk


def main():
    app = Application()
    app.mainloop()


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Hello Tk')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.rowconfigure(0, weight=1)

        frame = InputForm(self)
        frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

        frame2 = InputForm(self)
        frame2.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)


class InputForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.entry = tk.Entry(self)
        self.entry.grid(row=0, column=0, sticky='ew')

        self.entry.bind('<Return>', self.add_to_list)

        self.btn_entry = tk.Button(self, text='add', command=self.add_to_list)
        self.btn_entry.grid(row=0, column=1)

        self.btn_clear = tk.Button(self, text='clear', command=self.clear_list)
        self.btn_clear.grid(row=0, column=2)

        self.lst_text = tk.Listbox(self)
        # sticky: east and west
        self.lst_text.grid(row=1, column=0, columnspan=2, sticky='nsew')

    def add_to_list(self, event=None):
        text = self.entry.get()
        if text:
            self.lst_text.insert(tk.END, text)
            self.entry.delete(0, tk.END)

    def clear_list(self, event=None):
        self.lst_text.delete(0, tk.END)


if __name__ == '__main__':
    main()
