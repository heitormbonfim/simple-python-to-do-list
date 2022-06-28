from tkinter import *
from tkinter import filedialog
from tkinter.font import Font
from tkinter.filedialog import FileDialog
import pickle

root = Tk()
root.title('To Do List')
# root.iconbitmap('')
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


entry_box = Entry(root, font=('Helvenica', 24), width=24)
entry_box.pack(pady=20)

frame_button = Frame(root)
frame_button.pack(pady=20)


def add_task():
    list_box.insert(END, entry_box.get())
    entry_box.delete(0, END)


def delete_task():
    list_box.delete(ANCHOR)


def cross_off_task():
    list_box.itemconfig(
        list_box.curselection(),
        foreground='#cccccc',
    )
    # get rid of selection bar
    list_box.selection_clear(0, END)


def uncross_task():
    list_box.itemconfig(
        list_box.curselection(),
        foreground='#262626',
    )
    list_box.selection_clear(0, END)


def delete_done_tasks():
    counter = 0
    while counter < list_box.size():
        if list_box.itemcget(counter, 'foreground') == '#cccccc':
            list_box.delete(list_box.index(counter))
        else:
            counter += 1


def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir='/home/heitorthewizard/Documents/studies/python/tkinter/python-todo-list',
        title='Save File',
        filetypes=(('Dat Files', '*.dat'), ('All Files', '*.*'))
    )
    if file_name:
        delete_done_tasks()
        if file_name.endswith('.dat'):
            pass
        else:
            file_name = f'{file_name}.dat'

        tasks = list_box.get(0, END)
        output_file = open(file_name, 'wb')
        pickle.dump(tasks, output_file)


def open_list():
    file_name = filedialog.askopenfilename(
        initialdir='/home/heitorthewizard/Documents/studies/python/tkinter/python-todo-list',
        title='Open File',
        filetypes=(('Dat Files', '*.dat'), ('All Files', '*.*'))
    )

    if file_name:
        list_box.delete(0, END)
        input_file = open(file_name, 'rb')
        tasks = pickle.load(input_file)
        for task in tasks:
            list_box.insert(END, task)


def clear_list():
    list_box.delete(0, END)


menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='File', menu=file_menu)

file_menu.add_command(label='Save List', command=save_list)
file_menu.add_command(label='Open List', command=open_list)
file_menu.add_separator()
file_menu.add_command(label='Clear List', command=clear_list)


add_button = Button(frame_button, text='Add Task', command=add_task)
delete_button = Button(frame_button, text='Delete Task', command=delete_task)
cross_off_button = Button(frame_button, text='Done', command=cross_off_task)
uncross_button = Button(frame_button, text='Undo', command=uncross_task)
delete_done_tasks_button = Button(
    frame_button, text='Delete Done Tasks', command=delete_done_tasks)

add_button.grid(row=0, column=0)
delete_button.grid(row=0, column=1)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3)
delete_done_tasks_button.grid(row=0, column=4)

root.mainloop()
