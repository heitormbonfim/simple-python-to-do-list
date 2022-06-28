from tkinter import *
from tkinter.font import Font

root = Tk()
root.title('To Do List')
#root.iconbitmap('')
root.geometry('500x500')


font = Font(
    family='Arial',
    size=30,
    weight='bold'
)

frame = Frame(root)
frame.pack()

list_box = Listbox(frame,
    font=font,
    width=25,
    height=5,
    background="#f0f0f0",
    border=0,
    foreground='#262626',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle='none',
)

list_box.pack(side=RIGHT, fill=BOTH)

scrolbar = Scrollbar(frame)
scrolbar.pack(side=RIGHT, fill=BOTH)

list_box.config(yscrollcommand=scrolbar.set)
scrolbar.config(command=list_box.yview)


entry_box = Entry(root, font=('Helvenica', 24))
entry_box.pack(pady=20)

frame_button = Frame(root)
frame_button.pack(pady=20)

def add_item():
    list_box.insert(END, entry_box.get())
    entry_box.delete(0, END)

def delete_item():
    list_box.delete(ANCHOR)

def cross_off_item():
    pass

def uncross_item():
    pass


add_button = Button(frame_button, text='Add Item', command=add_item)
delete_button = Button(frame_button, text='Delete Item', command=delete_item)
cross_off_button = Button(frame_button, text='Cross Off', command=cross_off_item)
uncross_button = Button(frame_button, text='Uncross Off', command=uncross_item)

add_button.grid(row=0, column=0, padx=20)
delete_button.grid(row=0, column=1)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)



root.mainloop()
