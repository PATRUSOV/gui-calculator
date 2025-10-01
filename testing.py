import tkinter as tk

root = tk.Tk()
root.title("Testing")
root.geometry("500x400")

entr_frame = tk.Frame(root, background="green", width=300, height=300)
entr_frame.place(relx=0.5, rely=0.5, anchor="center")

lbl1 = tk.Label(entr_frame, text="hello world = 1", bg="black", fg="blue")
lbl1.place(relx=0.5, rely=0.2, anchor="center")

lbl2 = tk.Label(entr_frame, text="hello world = 2", bg="black", fg="blue")
lbl2.place(relx=0.5, rely=0.25, anchor="center", width=100, height=30)

root.mainloop()
