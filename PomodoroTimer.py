from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

#configure root main window
root = tk.Tk()
root.title("PomodoroTimer")
root.geometry("600x400")


#place and make a main frame
frame = tk.Frame(root)
frame.pack()


#make various widgets
btn_ttk = ttk.Button(frame, text="PomodoroStart", command=print("sss"))

main_label = ttk.Label(frame, text="okokok", font=("MSゴシック", 30, "bold"))


#place various widgets
btn_ttk.grid(row=1, column=0, pady=5)
main_label.grid(row=0, column=0)

root.mainloop()


