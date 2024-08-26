import tkinter

window = tkinter.Tk()

window.title('My first GUI App')
window.minsize(width=500, height=300)

# Label
label = 'I am a Label'
my_label = tkinter.Label(text=label, font=('Arial', 24))
my_label.grid(column=0, row=0)

# Button
def button_click():
    my_label.config(text=input.get(), font=('Arial', 24))


button = tkinter.Button(text="Click me", command=button_click)
button.grid(row=1, column=1)
new_button = tkinter.Button(text='New Button')
new_button.grid(row=0,column=2)

# Entry
entry = tkinter.Entry(width=10)
entry.grid(row=2, column=3)




window.mainloop()