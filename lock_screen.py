from tkinter import *

def lockscreen():
    root = Tk()
    root.geometry('500x500')
    root['bg'] = "black"
    root.attributes('-topmost', True, '-fullscreen', True)
    def epelepsy1():
        root['bg'] = "red"
        root.after(100, epelepsy2)
    def epelepsy2():
        root['bg'] = "green"
        root.after(100, epelepsy3)
    def epelepsy3():
        root['bg'] = "blue"
        root.after(100, epelepsy1)
    root.after(100, epelepsy1)
    root.mainloop()
def lockscreen_pass(gen):
    root = Tk()
    root.geometry('500x500')
    root['bg'] = "black"
    root.attributes('-topmost', True, '-fullscreen', True)
    def exit():
        pass
    def real_exit():
        passwd = ent.get()
        if passwd == gen:
            root.destroy()
    root.protocol("WM_DELETE_WINDOW", exit)
    Label(root, text='Enter password', bg='black', fg='white', font='Area 15').pack()
    ent = Entry(root, bg='white', fg='black', font='Area 15')
    ent.pack()
    Button(root, text='Enter password', bg='black', fg='white', font='Area 15', command=real_exit).pack()
    root.mainloop()