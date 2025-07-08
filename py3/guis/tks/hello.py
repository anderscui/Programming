# coding=utf-8
import tkinter as tk

n_clicked = 0


# handlers
def on_button_click():
    # print('button clicked')
    # n_clicked += 1
    # label.config(text=f'button clicked {n_clicked} times')
    label.config(text=f'button clicked')


# Tk: Toplevel widget of Tk which represents mostly the main window of an application.
window = tk.Tk()
window.title('Hello Tk')

label = tk.Label(window, text='simple label')
# label.grid()
label.grid(row=0, column=0)

# config keys
# print(label.config().keys())

# with a parent widget
button = tk.Button(window, text='click me', command=on_button_click)
# add to the parent, using grid layout
button.grid(row=0, column=1)

window.mainloop()
