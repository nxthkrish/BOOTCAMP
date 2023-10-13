import tkinter
def changer():
    label1.config(text="LOCATION UNKNOWN")
    

window=tkinter.Tk()
window.title("My first GUI application")
window.minsize(400,300)
custom_font1 = ('Times New Roman', 16)
label1=tkinter.Label(window,text="EAST",font=("Comic Sans Ms",20))
label2=tkinter.Label(window,text="WEST",font=("Comic Sans Ms",20))
label3=tkinter.Label(window,text="NORTH",font=("Comic Sans Ms",20))
label4=tkinter.Label(window,text="SOUTH",font=("Comic Sans Ms",20))
label1.pack(side=tkinter.TOP)
label2.pack(side=tkinter.BOTTOM)
label3.pack(side=tkinter.LEFT)
label4.pack(side=tkinter.RIGHT)
click_button = tkinter.Button(window, text="Find Location",command=changer)
click_button.pack(side=tkinter.BOTTOM)



window.mainloop()