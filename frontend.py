from tkinter import *
import backend
root = Tk()


def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)


def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(),author_text.get(),Year_text.get(),isbn_text.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(title_text.get(), author_text.get(), Year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END,(title_text.get(), author_text.get(), Year_text.get(), isbn_text.get()))

def select_item(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]#it return ans in tuple like(1,) so v need 11st  item so[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END, selected_tuple[4])
        #print(selected_tuple)
    except IndexError:
        pass


def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),Year_text.get(),isbn_text.get())
    print(selected_tuple[0],title_text.get(),author_text.get(),Year_text.get(),isbn_text.get())



l1=Label(root,text="Title")
l1.grid(row=0,column=0)

l2=Label(root,text="Author")
l2.grid(row=0,column=2)

l3=Label(root,text="Year")
l3.grid(row=1,column=0)

l4=Label(root,text="ISBN")
l4.grid(row=1,column=2)


title_text=StringVar()
e1=Entry(root,textvariable=title_text)
e1.grid(row=0,column=1)



author_text=StringVar()
e2=Entry(root,textvariable=author_text)
e2.grid(row=0,column=3)



Year_text=StringVar()
e3=Entry(root,textvariable=Year_text)
e3.grid(row=1,column=1)


isbn_text=StringVar()
e4=Entry(root,textvariable=isbn_text)
e4.grid(row=1,column=3)


list1=Listbox(root,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(root)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set )
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>",select_item)


b1=Button(root,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)

b1=Button(root,text="Search Entry",width=12,command=search_command)
b1.grid(row=3,column=3)

b1=Button(root,text="Add Entry",width=12,command=add_command)
b1.grid(row=4,column=3)

b1=Button(root,text="update",width=12,command=update_command)
b1.grid(row=5,column=3)

b1=Button(root,text="Delete",width=12,command=delete_command)
b1.grid(row=6,column=3)

b1=Button(root,text="Close",width=12,command=root.destroy)
b1.grid(row=7,column=3)

root.mainloop()

