
from tkinter import *
import backend

def get_selected_row(event):
    global selected_item_list
    index=list1.curselection()[0]
    selected_item_list=list1.get(index)
    #print(selected_item_list)
    e1.delete(0,END)
    e1.insert(END,selected_item_list[1])

    e2.delete(0,END)
    e2.insert(END,selected_item_list[2])
    e3.delete(0,END)
    e3.insert(END,selected_item_list[3])
    e4.delete(0,END)
    e4.insert(END,selected_item_list[4])
   
    
    

def list_items():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_items():
    list1.delete(0,END)
    for row in backend.search(e1_title.get(),e2_author.get(),e3_year.get(),e4_isbn.get()):
        list1.insert(END,row)
        
def insert_items():
    backend.insert(e1_title.get(),e2_author.get(),e3_year.get(),e4_isbn.get())
    list1.delete(0,END)
    list1.insert(END,(e1_title.get(),e2_author.get(),e3_year.get(),e4_isbn.get()))
    

def delete_items():
    backend.delete(selected_item_list[2])
  
def update_items():
    backend.update(selected_item_list[0],e1_title.get(),e2_author.get(),e3_year.get(),e4_isbn.get())
    


window=Tk()

window.wm_title("BookStore")

l1=Label(window,text="Title")
l1.grid(row=0,column=1)

l2=Label(window,text="Author")
l2.grid(row=0,column=3)

l3=Label(window,text="Year")
l3.grid(row=1,column=1)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=3)

e1_title=StringVar()
e1=Entry(window,textvariable=e1_title)
e1.grid(row=0,column=2)


e2_author=StringVar()
e2=Entry(window,textvariable=e2_author)
e2.grid(row=0,column=4)

e3_year=StringVar()
e3=Entry(window,textvariable=e3_year)
e3.grid(row=1,column=2)

e4_isbn=StringVar()
e4=Entry(window,textvariable=e4_isbn)
e4.grid(row=1,column=4)

list1=Listbox(window,height=6,width=40)
list1.grid(row=2,column=1,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=3,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="VIEW ALL",width=12,command=list_items)
b1.grid(row=2,column=4)

b2=Button(window,text="SEARCH",width=12,command=search_items)
b2.grid(row=3,column=4)

b3=Button(window,text="ADD BOOK",width=12,command=insert_items)
b3.grid(row=4,column=4)

b4=Button(window,text="UPDATE",width=12,command=update_items)
b4.grid(row=5,column=4)

b5=Button(window,text="DELETE",width=12,command=delete_items)
b5.grid(row=6,column=4)

b6=Button(window,text="CLOSE",width=12,command=window.destroy)
b6.grid(row=7,column=4)


window.mainloop()
 
 
