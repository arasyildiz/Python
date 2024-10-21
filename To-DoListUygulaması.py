from tkinter import *

# Backend
myList = []

def add_task():
    task = entry.get()
    if task:
        myList.append(task)
        entry.delete(0, END)
        update_task_list()
        print("Başarıyla eklendi")

def remove_task():
    task = entry.get()
    if task in myList:
        myList.remove(task)
        entry.delete(0, END)
        update_task_list()
        print("Başarıyla silindi")
    else:
        print("Bulunamadı")

def update_task_list():
    task_list.delete(0, END)
    for task in myList:
        task_list.insert(END, task)

# Frontend
root = Tk()
root.title("To-Do List Uygulaması")

frame = Frame(root)
frame.pack(pady=10)

entry = Entry(frame, width=40)
entry.pack(side=LEFT, padx=10)

add_button = Button(frame, text="Görev Ekle", command=add_task)
add_button.pack(side=LEFT)

remove_button = Button(frame, text="Görev Sil", command=remove_task)
remove_button.pack(side=LEFT)

task_list = Listbox(root, width=50, height=10)
task_list.pack(pady=20)

root.mainloop()
