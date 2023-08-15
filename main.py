from tkinter import *

def add_item(item: Entry, listbox: Listbox):
    entry = new_entry.get()
    with open("tasks.txt", 'w') as new_task:
        new_task.writelines(entry)
        new_task.close()



def delete_item(listbox: Listbox):
    with open("tasks.txt", "r") as delete_line:
        delete = delete_line.readlines()

        if delete:
            delete.pop()
    
    with open("tasks.txt", "w") as file:
        file.writelines(delete)

root = Tk()
root.title("ToDo-Liste")
root.geometry('300x400')
root.resizable(False, False)

listbox = Listbox(root, font=('Calibri', 12), height = 12, width=25)
listbox.place(x=35, y=50)
scrollbar = Scrollbar(root, orient=VERTICAL, command=listbox.yview)
scrollbar.place(x=260, y=50, height=232)
listbox.config(yscrollcommand=scrollbar.set)

with open("tasks.txt", '+r') as tasks_list:
    for task in tasks_list:
        listbox.insert(END, task)
    tasks_list.close()

new_entry = Entry(root, width=37)
new_entry.place(x=35, y=310)

add_btn = Button(root, text="Add Item", width=10, font=("Calibri", 12), command= lambda: add_item(new_entry, listbox))
add_btn.place(x=45, y=350)

delete_btn = Button(root, text="Delete Item", width=10, font=("Calibri", 12), command= lambda: delete_item(listbox))
delete_btn.place(x=150, y=350)

root.update()
root.mainloop()
