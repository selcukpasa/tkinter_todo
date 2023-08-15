from tkinter import *
import config

path = config.PATH

def add_item(item: Entry, listbox: Listbox):
    #Aus der Inputbox wird der Inhalt gespeichert
    entry = new_entry.get()
    #Solange entry nicht leer, wird am Ende der Listbox entry eingetragen
    # with open(file, 'w') = es wird in die Datei geschrieben, dabei wird ueberschrieben
    # with open(file, 'a') = es wird in die Datei geschrieben, dabei wird der vorherige Inhalt erhalten bleiben 
    if entry:
        listbox.insert(END, entry)
        with open(path, 'w') as new_task:
            new_task.write(entry + '\n')
    #textbox wird geleert
    new_entry.delete(0,END)



def delete_item(listbox: Listbox):
    #Ausgewaehltes Index in Listbox wird gespeichert
    selected_index = listbox.curselection()
    #Solange selected_index nicht leer, wird das ausgewaehlte Element in der Listbox geloescht
    #Danach wird der Rest in tasks.txt eingespeichert
    if selected_index:
        listbox.delete(selected_index)
        with open(path, 'w') as file:
            for i in range(listbox.size()):
                file.write(listbox.get(i) + '\n')

root = Tk()
root.title("ToDo-Liste")
root.geometry('300x400')
root.resizable(False, False)

listbox = Listbox(root, font=('Calibri', 12), height = 12, width=25)
listbox.place(x=35, y=50)
#Scrollbar wird mit den Koordinaten x=260 und y=50 erstellt
scrollbar = Scrollbar(root, orient=VERTICAL, command=listbox.yview)
scrollbar.place(x=260, y=50, height=232)
#Man kann die Listbox scrollen indem man die Scrollbar mit der Listbox verknuepft
listbox.config(yscrollcommand=scrollbar.set)

#Der Inhalt von der Datei wird in die Listbox eingefuegt
with open(path, '+r') as tasks_list:
    for task in tasks_list:
        listbox.insert(END, task)
    tasks_list.close()

new_entry = Entry(root, width=37)
new_entry.place(x=35, y=310)

#Dieser Knopf fuegt Inhalte aus der Inputbox in die Listbox und Datei
add_btn = Button(root, text="Add Item", width=10, font=("Calibri", 12), command= lambda: add_item(new_entry, listbox))
add_btn.place(x=45, y=350)

#Dieser Knopf loescht ein ausgewaehltes Element der Listbox und aus der Datei
delete_btn = Button(root, text="Delete Item", width=10, font=("Calibri", 12), command= lambda: delete_item(listbox))
delete_btn.place(x=150, y=350)

root.update()
root.mainloop()
