from tkinter import *
import tk_tools
from Controller import Controller
from functools import partial
import time
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Twitter Sentiment Analyser")

        for r in range(6):
            self.master.rowconfigure(r, weight=2)    
        for c in range(5):
            self.master.columnconfigure(c, weight=2)
            #Button(master, text="Button {0}".format(c)).grid(row=6,column=c,sticky=E+W)

        Frame1 = Frame(master)
        Frame1.grid(row = 0, column = 2, rowspan = 3, columnspan = 3, sticky = W+E+N+S,  padx=(5,10), pady=(10,5)) 
        Frame2 = Frame(master)
        Frame2.grid(row = 3, column = 2, rowspan = 3, columnspan = 3, sticky = W+E+N+S, padx=(5,10), pady=(5,10))
        Frame3 = Frame(master,bg="lightgrey")
        Frame3.grid(row = 0, column = 0, rowspan = 6, columnspan = 2, sticky = W+E+N+S, padx=(10,5), pady=10)

        #Frame3
        label1 = Label(Frame3, text="Search Tweets", bg="lightgrey",fg="black", font="arial 20 bold" )
        label1.grid(row=0)        
        label1.place(x=190,y=25, anchor="center")


        large_font = ('Verdana',20)
        
        key = Entry(Frame3,width="15",font=large_font)
        key.grid(row=1,rowspan=3)
        key.place(x=190,y=120, anchor="center")
        
        

        label2 = Label(Frame3, text="Apply Filters :", bg="lightgrey",fg="black", font="arial 15 " )
        label2.grid(row=3)
        label2.place(x=120,y=200, anchor="center")

        OPTIONS = ["ALL","IN","AUS"]
        variable = StringVar(Frame3)
        variable.set(OPTIONS[0])
        
        label3 = Label(Frame3, text="Choose a Country", bg="lightgrey",fg="black", font="arial 10" )
        label3.grid(row=4)
        label3.place(x=150,y=270, anchor="center")

        w = OptionMenu(Frame3, variable, *OPTIONS)
        w.grid(row=4)
        w.place(x=250,y=270, anchor="center")
        

        photo = PhotoImage(file = r"C:\Users\sanjana\Pictures\submitbutton.jpg")
        
        
        

        

        
        
        #Frame 1
        gauge = tk_tools.Gauge(Frame1, yellow_low=60, red_low=40, yellow=100, red=90, width=400, height=250, min_value=-1 , max_value=1, label='Polarity', bg="gray94",divisions=20,unit='%')
        gauge.grid(row=0)
        
        gauge.place(x=285,y=143, anchor="center")

        #Frame 2
        table = tk_tools.LabelGrid(Frame2,num_of_columns=2, headers=["Username","Tweet"])
        table.grid(row=0)
        table.place(x=285,y=143, anchor="center")

        keyresult = partial(getSentiment,key,variable,gauge,table)

        btn = Button(Frame3, text = 'Get Results', bd="5", width="10", command=keyresult)
        btn.grid(row=5)
        btn.place(x=190,y=400, anchor="center")
        

        

def getSentiment(skey,loc,g,t):
    keyword = skey.get()
    location = loc.get()
    C = Controller()
    stat = C.search(keyword,location)
    time.sleep(5)
    if(stat):
            res = C.display()
            g.set_value(res[len(res)-1])
            for i in range(0,len(res)-1):
                row = res[i]
                t.add_row(row)
    else:
        print ("status is false")






        


        




        
        

root = Tk()
root.geometry("1000x600")
root.configure(background="white")
app = Application(master=root)
app.mainloop()
