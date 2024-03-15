import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Student Information System")
window.geometry("800x600")

tk.Frame(window, width = 100, height = 100)
tk.Label(window, text = "This is a Label")


def onClick():
    messagebox.showinfo(message="Button 1 clicked")
tk.Button(window, text = "Button 1", command = onClick)

onClick()

def show_message_box():
    messagebox.showinfo("Annoucement", "This is a small message box!")

button = tk.Button(window, text="Click here", command=show_message_box)
button.pack(pady=20)

icts = ["ICT", "I See Tea", "Icy Tea", "Ice City"]
listbox = tk.Listbox(window)
for i in icts:
    listbox.insert(icts.index(i), i)
tk.Frame(window, width = 100, bg="red").pack()
tk.Frame(window, width = 50, bg="green").pack()
tk.Frame(window, width = 25, bg="blue").pack()


window.mainloop()
