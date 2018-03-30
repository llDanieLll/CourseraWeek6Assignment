import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        ###this function creates two widgets(or buttons), one is the "hi_there" button, another is the "quit" button ###
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        
        ### now is the "quit" button ###

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
        
##以下是要执行的指令，上面都是铺垫##
        
root = tk.Tk()## Tk() function creates the main window of an application. Each instance has its own associated Tcl interpreter.##

##可以为你的主窗口设置名称与大小，初始位置##
root.title('My App')
root.geometry('600x500+600+250')

app = Application(master=root)

app.mainloop()
