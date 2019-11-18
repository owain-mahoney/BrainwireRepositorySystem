from tkinter import *
from tkinter import ttk

login =Tk()
login.title('login')
login.geometry('720x360')
txt_username = ttk.Entry(login, width=25)
txt_username.grid(row = 0, column = 1)
txt_password = ttk.Entry(login, width=25, show="*")
txt_password.grid(row = 1,column = 1)
ttk.Label(login, text="UserName").grid(row=0, padx = 10)
ttk.Label(login, text="pastword").grid(row=1)

button = ttk.Button(login,text= "Login")
button.place( relx = 0.5, rely = 0.5, anchor = CENTER)

checked=IntVar()
checkbutton = ttk.Checkbutton(login,text='terms and condtions click here for more info',variable = checked)
checkbutton.grid(
    


def main():
      
  if checked.get()==1:
      root = Tk()
      root.title('Payrol')
      root.option_add('*tearOff', False)
      menubar = Menu(root)
      root.config(menu = menubar)
      file = Menu(menubar)
      edit = Menu(menubar)
      help_ = Menu(menubar)
      new_win = Menu(menubar)
      menubar.add_cascade(menu = file, label = 'File')
      menubar.add_cascade(menu = edit, label = 'Edit')
      menubar.add_cascade(menu = help_, label = 'Help')
      file.add_command(label = 'New', command = lambda: print('New File'))
      file.add_separator()
      file.add_command(label = 'Open', command = lambda: print('Opening File...'))
      file.add_command(label = 'Save', command = lambda: print('Saving File...'))
      file.add_command(label = 'New_window',command = new_win)
      edit.add_command(label= 'remove',command = lambda:print('Removing File...'))
      root.geometry('640x480+200+200')
      title = ttk.Label(root,text='payrol',font=("Helvetica", 64))
      title.pack()




def callback():    
    if checked.get() ==1:
        win=Tk()
        win.title('lol')
        win.geometry('200x200')
        title=ttk.Label(win,text = 'thanks sir ')
        title.pack()
        

button.config(command = main)

login.mainloop()
