"""
    Program......: dd58.py
    Author.......: Michael Rouse
    Date.........: 3/7/14
    Description..: Modify dd57 by adding a rolling counter for number of problems correct and attempted
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
        
        # Variables for the Problem
        self.i_number1 = 0
        self.i_number2 = 0
        self.s_answer = "0"
        self.s_userAnswer = "0"

        # Variables for problem counter
        self.i_totalCorrect = 0
        self.i_totalWrong = 0

        # Create Widgets
        self.create_widgets()

        # Generate first problem
        self.new_problem()
        
    def create_widgets(self):
        """ Create Buttons, Labels, etc... """
        # Problem Label
        self.lbl_problem = Label(self, text=str(self.i_number1) + " + " + str(self.i_number2))
        self.lbl_problem.grid(column=13, row=1, pady=10, columnspan=5, rowspan=5)

        # Answer Label
        self.lbl_answer = Label(self, text="Your Answer:")
        self.lbl_answer.grid(column=7, row=6, columnspan=10, sticky=W)

        # Answer Entry Box
        self.ent_answer = Entry(self)
        self.ent_answer.grid(column=17, row=6, columnspan=10)

        # Submit Button
        self.btn_submit = Button(self, text="Submit", command=self.check_answer)
        self.btn_submit.grid(column=13, row=7, pady=10, columnspan=6, rowspan=3)

        # Instructions Label
        self.lbl_instructs = Label(self, text="Type your answer in the box and click \"Submit\"\nYour progress will be displayed below")
        self.lbl_instructs.grid(column=1, row=11, padx=20, columnspan=30, rowspan=2)

        # Total Correct Label
        self.lbl_totalCorrect = Label(self, text="Correct: " + str(self.i_totalCorrect))
        self.lbl_totalCorrect.grid(column=4, row=15, padx=0, pady=10, columnspan=10, rowspan=2, sticky=W)

        # Total Wrong Label
        self.lbl_totalWrong = Label(self, text="Incorrect: " + str(self.i_totalWrong))
        self.lbl_totalWrong.grid(column=20, row=15, padx=0, pady=10, columnspan=10, rowspan=2, sticky=W)
        
    def check_answer(self):
        """ Compare user's answer to correct answer """
        self.s_userAnswer = self.ent_answer.get()

        if self.s_userAnswer == self.s_answer:
            # Correct Answer
            self.i_totalCorrect += 1

            # Update label of total correct
            self.lbl_totalCorrect.config(text="Correct: " + str(self.i_totalCorrect))

        else:
            # Wrong Answer
            self.i_totalWrong += 1
            
            # Update label of total wrong
            self.lbl_totalWrong.config(text="Incorrect: " + str(self.i_totalWrong))

        # Get a new problem
        self.new_problem()

    def new_problem(self):
        """ Reset all for a new problem """
        i_old_number1 = self.i_number1
        i_old_number2 = self.i_number2

        # Generate new numbers
        while i_old_number1 == self.i_number1 and i_old_number2 == self.i_number2:
            self.i_number1 = randint(0, 20)
            self.i_number2 = randint(0, 20)

        # Get the new answer
        self.s_answer = str(self.i_number1 + self.i_number2)

        # Reset the problem label
        self.lbl_problem.config(text=str(self.i_number1) + " + " + str(self.i_number2))

        # Reset the entry box
        self.ent_answer.delete(0, END)


        

# Main
def main():
    gui = Tk()
    gui.title("Math Fun")
    gui.geometry("300x200")

    app = Application(gui)

    gui.mainloop()


main()
