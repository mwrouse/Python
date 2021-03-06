"""
    Program......: dd56.py
    Author.......: Michael Rouse
    Date.........: 3/5/14
    Description..: Create a GUI called "Math Fun" that asks the user to answer an addition problem
"""
from tkinter import *
from random import randint

# Class for GUI
class Application(Frame):
    """ GUI Application """
    def __init__(self, master):
        # Initialize the frame
        super(Application, self).__init__(master)
        self.grid()
        self.number1 = randint(0, 20)
        self.number2 = randint(0, 20)
        self.answer = self.number1 + self.number2
        self.userAnswer = 0
        self.create_widgets()

    def create_widgets(self):
        # Create buttons, labels, etc...
        self.lbl_problem = Label(self, text=str(self.number1) + " + " + str(self.number2))
        self.lbl_problem.grid(column=13, row=1, pady=10, columnspan=5, rowspan=5)
        
        self.lbl_answer = Label(self, text="Your Answer:")
        self.lbl_answer.grid(column=7, row=6, columnspan=10, sticky=W)

        # Answer Entry Box
        self.ent_answer = Entry(self)
        self.ent_answer.grid(column=17, row=6, columnspan=10)

        # Submit Button
        self.btn_submit = Button(self, text="Submit", command=self.check_answer)
        self.btn_submit.grid(column=13, row=7, pady=10, columnspan=6, rowspan=3)

        # Instructions Label
        self.lbl_instructs = Label(self, text="Type your answer in the box and click \"Submit\"")
        self.lbl_instructs.grid(column=1, row=11, padx=20, pady=10, columnspan=30, rowspan=5)
        
    def check_answer(self):
        text = ""  # New text for label
        color = "" # New color for label
        
        try:
            # Check if answer is valid
            self.userAnswer = int(self.ent_answer.get())
            
        except:
            # Answer invalid, may contain non-integer characters
            text = "The Answer Must Be An Integer!"
            color = "red"
            padding = 40
            
        else:
            # Answer is valid, check if it's correct
            if self.userAnswer == self.answer:
                # Correct Answer
                text = "Hooray!"
                color = "green"
                padding = 119
            
            else:
                # Wrong Answer
                text = "Sorry, Try Again"
                color = "red"
                padding = 93

        # Update the label
        self.lbl_instructs.config(text=text, fg=color, font="Arial 11")
        self.lbl_instructs.grid(column=1, row=11, padx=padding, pady=10, columnspan=30, rowspan=5)

# Main
def main():
    gui = Tk()
    gui.title("Math Fun")
    gui.geometry("300x200")

    app = Application(gui)

    gui.mainloop()


main()
