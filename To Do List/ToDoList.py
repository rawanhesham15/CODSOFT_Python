import tkinter 
from tkinter import *

root = Tk()
root.title("To Do List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []


def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("E:/Internships/Codsoft python/Tasks/To Do List/tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")

        task_list.append(task)
        listbox.insert(END, task)


def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("E:/Internships/Codsoft python/Tasks/To Do List/tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")

            listbox.delete(ANCHOR)


def openTaskFile():
    try:
        global task_list
        with open("E:/Internships/Codsoft python/Tasks/To Do List/tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file=open('tasklist.txt', 'w')
        file.close()


def markAsComplete():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        listbox2.insert(END, task)
        task_list.remove(task)
        with open("E:/Internships/Codsoft python/Tasks/To Do List/tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")

            listbox.delete(ANCHOR)

            
# icon
image_icon = PhotoImage(file="E:/Internships/Codsoft python/Tasks/To Do List/task.png")
root.iconphoto(False, image_icon)


#top bar
top_image = PhotoImage(file="E:/Internships/Codsoft python/Tasks/To Do List/topbar.png")
Label(root, image=top_image).pack()

note_image = PhotoImage(file="E:/Internships/Codsoft python/Tasks/To Do List/list.png")
note_image = note_image.subsample(round(note_image.width() / 50), round(note_image.height() / 50))
Label(root, image=note_image, bg="#32405b").place(x=70, y=15)

heading = Label(root, text="To Do List", font="arial 22 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)


#main
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=120)

task=StringVar()
task_entry= Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()
button = Button(frame, text="Add", font="arial 20 bold", width=6, bg="#32405b", fg="#fff", bd=0, command=addTask)
button.place(x=300, y=0)


#listbox
frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(100, 0))

listbox = Listbox(frame1, font=('arial, 12'), width=40, height=10, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

#completed tasks
frame2 = Frame(root, bd=3, width=700, height=150, bg="#32405b")
frame2.pack(pady=(20, 0))
title_label = Label(frame2, text="Completed Tasks", bg="#32405b", fg="white", font=("Arial", 16))
title_label.pack()
listbox2 = Listbox(frame2, font=('arial, 12'), width=40, height=6, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox2.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar=Scrollbar(frame2)
scrollbar.pack(side=RIGHT, fill=BOTH)

#delete
delete_icon = PhotoImage(file="E:/Internships/Codsoft python/Tasks/To Do List/delete.png")
# Button(root, image=delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)
Button(root, image=delete_icon, bd=0, command=deleteTask).place(x=130, y=580)

#mark as complete
correct_icon = PhotoImage(file="E:/Internships/Codsoft python/Tasks/To Do List/correct.png")
correct_icon = correct_icon.subsample(round(correct_icon.width() / 50), round(correct_icon.height() / 50))
Button(root, image=correct_icon, bd=0, command=markAsComplete).place(x=210, y=580)



root.mainloop()