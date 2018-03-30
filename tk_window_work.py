import tkinter as tk

class Application(tk.Frame):
    def __init__ (self,master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there ['text']  = 'love me?'
        self.hi_there ['command'] = self.say_yes
        self.hi_there ['fg'] = 'red'
        self.hi_there ['font'] = 'Arial','20','bold'
        self.hi_there ['bg']= 'white'
        self.hi_there ['width'] = '20'
        self.hi_there.grid(row = 0, column = 0, sticky = 'W')
       

        self.quit = tk.Button(self,text = 'QUIT',fg = 'red', 
                              command = self.say_no)
        self.quit.grid(row=0,column = 1)

    def say_no(self):
        self.No_Label = tk.Label(self)
        self.No_Label ['text']  = 'nono'

        self.No_Label ['fg'] = 'white'
        self.No_Label ['font'] = 'Arial','20','bold'
        self.No_Label ['bg']= 'red'
        self.No_Label ['width'] = '20'
        self.No_Label.grid(row=1,column = 0)


    def say_yes(self):
        self.hi_there = tk.Button(self)
        self.hi_there ['text']  = 'Yes'
        self.hi_there ['command'] = self.say_hi
        self.hi_there ['fg'] = 'white'
        self.hi_there ['font'] = 'Arial','20','bold'
        self.hi_there ['bg']= 'red'
        self.hi_there ['width'] = '20'
        self.hi_there.grid(row=1,column = 0)
        
    def say_hi(self):
        self.hi_there = tk.Button(self)
        self.hi_there ['text']  = 'love you too!!'
        self.hi_there ['command'] = self.say_hi
        self.hi_there ['fg'] = 'red'
        self.hi_there ['font'] = 'Arial','20','bold'
        self.hi_there ['bg']= 'white'
        self.hi_there ['width'] = '20'
        self.hi_there.grid(row=2,column = 0)
        



root = tk.Tk()

root.title('My App')
root.geometry('600x500+600+300')

app = Application(master=root)
app.mainloop()

        
        
