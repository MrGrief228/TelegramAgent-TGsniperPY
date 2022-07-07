from tkinter import *

def run():
    root = Tk()
    root.geometry("450x100")
    root['bg'] = 'gray'
    
    def noclose():
        pass
    def close():
        root.destroy()
    def wtf():
        ftt = open('comment.txt', 'w')
        ftt.write(ent.get())
        ftt.close()
        close()
    
    root.protocol('WM_DELETE_WINDOW', noclose)
    root.attributes('-topmost', True)
    
    Label(root, text='Введите сообщение!', font='Area 15', bg='gray').place(y=0, x=0)
    ent = Entry(root, font='Area 15')
    ent.place(y=50, x=100)
    Button(root, text='Отправить', font='Area 15', bg = 'magenta', command=wtf).place(y=0, x=200)
    
    root.mainloop()