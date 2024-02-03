import tkinter

ventana = tkinter.Tk()
ventana.geometry("800x800")

btn1 = tkinter.Button(ventana, text="btn1", width=20, height=10)
btn2 = tkinter.Button(ventana, text="btn2", width=20, height=10)
btn3 = tkinter.Button(ventana, text="btn3", width=20, height=10)

btn1.grid(row=0, column=0)
btn2.grid(row=1, column=0)
btn3.grid(row=2, column=0)

ventana.mainloop()