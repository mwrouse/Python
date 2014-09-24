"""
    Program......: dd54.py
    Author.......: Michael Rouse
    Date.........: 2/27/14
    Description..: Create a GUI with two buttons to increase and decrease a label
"""
from tkinter import *


class Application(Frame):
    """ GUI Application """
    def __init__(self, master):
        """ Initialize frame """
        super(Application, self).__init__(master)
        self.grid()
        self.columnconfigure(1, weight=3)
        self.counter = 0 # Counter for the label
        self.create_widgets()

    def create_widgets(self):
        """ Create buttons and labels """
        # Counter label
        self.counterLabel = Label(self, text="0")
        self.counterLabel.pack(padx=90, side=TOP)
        
        
        # Up button
        self.upBtn = Button(self)
        self.upBtn["text"] = "UP"
        self.upBtn["command"] = self.increaseCounter
        self.upBtn.pack(padx=30, side=LEFT, ipadx=10)
        #self.upBtn.grid(column=0, padx=20, ipadx=10)

        # Down button
        self.downBtn = Button(self)
        self.downBtn["text"] = "DOWN"
        self.downBtn["command"] = self.decreaseCounter
        self.downBtn.pack(padx=5, side=LEFT)
        #self.downBtn.grid(s=LEFT)
        
    def increaseCounter(self):
        # Increase the counter by one
        self.counter += 1
        self.updateLabel()

    def decreaseCounter(self):
        # Decrease the counter by one
        self.counter -= 1
        self.updateLabel()

    def updateLabel(self):
        # Update the label with the new counter value
        self.counterLabel.config(text=str(self.counter))

# Main
gui = Tk()
gui.title("DD54")
gui.geometry("190x60")
app = Application(gui)

gui.mainloop()
        
