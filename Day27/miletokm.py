import tkinter

font = ('Arial', 14)
K = 1.609344

def calculate():
    km = int(entry.get()) * K
    label3.config(text=str(round(km)))

window = tkinter.Tk()
window.minsize(width=300, height=200)
window.config(padx=35, pady=35)

label = tkinter.Label(text='')
label.grid(column=0, row=0)

entry = tkinter.Entry(width=10)
entry.grid(column=1, row=0)

label1 = tkinter.Label(text='Miles', font=font)
label1.grid(column=2, row=0)

label2 = tkinter.Label(text='is equal to',  font=font)
label2.grid(column=0,row=1)

label3 = tkinter.Label(text='0',  font=font)
label3.grid(column=1,row=1)

label2 = tkinter.Label(text='Km',  font=font)
label2.grid(column=2,row=1)

button = tkinter.Button(text='CALCULATE', command=calculate)
button.grid(column=1, row=2)

window.mainloop()