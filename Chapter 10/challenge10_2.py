"""
    Program......: challenge10_2.py
    Auhtor.......: Michael Rouse
    Date.........: 3/4/14
    Description..: Guess My Number game with a GUI
"""
from tkinter import *
from random import randint



class Application(Frame):
    def __init__(self, master):
        """ Frame initializer """
        super(Application, self).__init__(master)
        self.grid()
        self.font = "Arial 12"
        self.number = randint(1, 100)
        self.create_widgets()

    def create_widgets(self):
        """ Create GUI Widgets """
        # Instructions
        self.lbl_instructions = Label(self, text="Guess a Number Between 1 and 100 \n Then Click \"Submit\"", font=self.font)
        self.lbl_instructions.grid(column=0, row=0, padx=10, pady=10, columnspan=20, rowspan=3)

        # Guess Label
        self.lbl_guess = Label(self, text="Guess: ", font=self.font)
        self.lbl_guess.grid(column=4, row=4, padx=0, pady=10, columnspan=6, rowspan=3)

        # Guess Input Box
        self.inp_guess = Entry(self, width=8, font=self.font)
        self.inp_guess.grid(column=8, row=4, padx=0, pady=10, columnspan=8, rowspan=3)

        # Submit Button
        self.btn_submit = Button(self, text="Submit", command=self.get_results, font=self.font)
        self.btn_submit.grid(column=7, row=7, columnspan=6, rowspan=2)

        # Result Label
        self.lbl_results = Label(self, text="", font=self.font)

    def get_results(self):
        """ Check the User's Guess """
        text = ""       # New Text for Result Label
        color = ""      # New font color for Result Label
        column = 3      # New column for the Result Label
        columnspan = 14 # New column span for the Result Label

        try:
            # Check if the guess is a valid number
            guess = int(self.inp_guess.get())
            column = 8
            columnspan = 4
            
        except:
            # Not a number
            text = "Invalid Guess, Try Again!"
            color = "red"

        else:
            # Valid Number
            if guess == self.number:
                # User Guessed the Number
                text = "Correct!"
                color = "green"

                # Modify the Submit button to start a new game
                self.btn_submit["text"] = "Play Again"
                self.btn_submit["command"] = self.reset_game

            elif guess > self.number:
                # User Guessed Too High
                text = "Lower!"
                color = "red"

            elif guess < self.number:
                # User Guessed Too Low
                text = "Higher!"
                color = "red"

            else:
                # An Unknown Error Occured
                text = "Oops! Try Again"
                color = "red"
            
        # Update the label
        self.lbl_results.config(text=text, foreground=color)
        self.lbl_results.grid(column=column, row=10, padx=0, pady=15, columnspan=columnspan)
        
    def reset_game(self):
        """ Reset the Button and get a new number """
        # Reset the Submit Button
        self.btn_submit["text"] = "Submit"
        self.btn_submit["command"] = self.get_results

        # Generate a new random number
        old_number = self.number

        while old_number == self.number:
            # Will loop until a different number is generated
            self.number = randint(1, 100)
        
        # Reset the Result Label
        self.lbl_results.config(text="")
        self.lbl_results.grid(column=6, row=10, padx=0, pady=15, columnspan=4)

        # Clear the Guess Entry box
        self.inp_guess.delete(0, END)
        
        
def main():
    """ Main Function """
    root = Tk()
    root.title("Guess My Number")
    root.geometry("282x200")
    app = Application(root)
    root.mainloop()

main()
