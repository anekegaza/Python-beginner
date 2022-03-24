#import modules
from tkinter import *
from tkinter import messagebox
from tkinter.font import *
from tkinter import filedialog
import pickle

#create the GUI
window = Tk()
window.geometry('500x500')
window.title('Organise it')
window.config(bg='green')

#create font
my_font = Font(weight='bold', size=10)

#create frame for listbox and scrollbar
listbox_and_scrollbar_frame = Frame(window,)
listbox_and_scrollbar_frame.pack(pady=10)

#create listbox
listbox = Listbox(listbox_and_scrollbar_frame,width="50", height="15", bd=0, activestyle='none',
               highlightthickness=0,bg='lightgrey',
               fg='black', font=my_font, selectbackground='grey'
               )
listbox.pack(side=LEFT, fill=BOTH)

#create scrollbar
scrollbar = Scrollbar(listbox_and_scrollbar_frame)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

welcome_message = ['Hello Dear', 'Welcome to Organise it,' ,'This app was created by Aneke Ifeanyi', 'Delete these texts and start making your list!']
for item in welcome_message:
    listbox.insert(END, item)

entry = Entry(window,width="33", font="Helvetica, 15")
entry.pack(pady=20)

#define functions

def enter_task():
    if entry.get() != "":
        listbox.insert(END, entry.get())
        entry.delete(0, END)
    else:
        messagebox.showwarning('warning!', "You should enter a task!")    

def check_off_task():
    try:
        listbox.itemconfig(listbox.curselection(), fg='#dedede',)
        listbox.selection_clear(0, END)
    except:
        messagebox.showwarning('Warning', 'You should select a task')

def delete_task():
    try:
        task = listbox.curselection()[0]
        listbox.delete(task)
    except:
        messagebox.showwarning('warning', 'You should select a Task!')    


# def un_check_off_task():
#     try:
#         listbox.itemconfig(listbox.curselection(), fg='black',)     (i left this just so it can be added in the updtaed version 
#         listbox.selection_clear(0, END)                                 in case there is a need for it)
#     except:
#         messagebox.showwarning('Warning', 'You should select a task!')

# def clear_checked_off():
#     count = 0
#     while count < listbox.size():
#         if listbox.itemcget(count, 'fg') == '#dedede':
#             listbox.delete(listbox.index(count))                   (this makes my app hang so i commented it out. 
#                                                                             I want to check for a solution)
#     else:
#         count += 1

def save_list():
    list_name = filedialog.asksaveasfilename(
        
        title='Save File', 
        filetypes=(('Dat Files', '*.dat'),('All Files', '*.*'))
    )  

    if list_name:
        if  list_name.endswith('.dat'):                   #add the .dat extenstion to our list
            pass
        else:
            list_name = f'{list_name}.dat'
       

#delete checked off items before saving
    # count = 0
    # while count < listbox.size():
    #     if listbox.itemcget(count, 'fg') == '#dedede':
    #         listbox.delete(listbox.index(count))
    # else:
    #     count += 1

    my_list = listbox.get(0, END)

    output_file = open(list_name, 'wb' )
    pickle.dump(my_list, output_file)  
    messagebox.showwarning('Success', 'List has been saved successfully!')   
 

def load_list():
    listbox.delete(0,END)
    list_name = filedialog.askopenfilename(title='Open File', 
                   filetypes=(('Dat Files', '*.dat'),('All Files', '*.*'),
                   ("Text File", '*.html'))
                   )    

    input_file = open(list_name,'rb')    #load the file/list
    my_list = pickle.load(input_file)

    for items in my_list:
        listbox.insert(END,items)      #show it to the screen

def clear_list():
   listbox.delete(0, END) 
   messagebox.showwarning('Success!', 'List has been cleared sucessfully!')
    
             

#create Menu
menu_bar = Menu(window, font=my_font, fg='white')
window.config(menu=menu_bar,)
menu_bar.config(bg='green',)
#adding files to the menu
file_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='File',menu=file_menu)

#add dropdown items
file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Load List", command=load_list)
file_menu.add_command(label="Clear List", command=clear_list)
# file_menu.add_command(label="Clear Completed", command=clear_checked_off)


#create button frame
button_frame = Frame(window, )
button_frame.pack()
button_frame.config(bg='green')

#create buttons

entry_button = Button(button_frame,text="Enter Task",command=enter_task, font=my_font)
entry_button.grid(row=0, column=0)
entry_button.config(bg='orange')

check_off_button = Button(button_frame,text="Check_off_Task",command=check_off_task, font=my_font)
check_off_button.grid(row=0, column=1, padx=20)
check_off_button.config(bg='orange')

delete_button = Button(button_frame,text="Delete Task",command=delete_task,font=my_font)
delete_button.grid(row=0, column=2,)
delete_button.config(bg='orange',)
# uncheck_off_button = Button(button_frame,text="Uncheck_Task",command=un_check_off_task)
# uncheck_off_button.grid(row=0, column=3)


label = Label(window, text=' Created by Aneke Ifeanyi ')
label.pack(pady=30)


window.mainloop()
''' This is my first application after my python studies. im so glad to have finished it successfully
it is really a thing of joy and i'm very happy about this.
To you the users, thank you!
possibly in the future, i will add more functionality
Finished on Monday 14th March, 2022  23:18 
''' 