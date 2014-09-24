"""
    Program......: main_menu.py
    Author.......: Michael Rouse
    Date.........: 3/19/14
    Description..: Main menu for DD61
"""
import tkinter

class main_menu_frame(tkinter.Frame):
    """ Frame for main menu """
    def __init__(self, master):
        # Initialize
        super(main_menu_frame, self).__init__(master)
        self.grid()
        self.master = master
        self.font = "Arial 14"
        self.choice = tkinter.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Main Label
        self.lblTitle = tkinter.Label(self, text="Choose Your Class", font="Arial 24")
        self.lblTitle.grid(column=1, columnspan=3, padx=150)

        # Knight Radio Button
        self.rbKnight = tkinter.Radiobutton(self, text="Knight", font=self.font, variable=self.choice, value="1")
        self.rbKnight.grid(column=2, pady=10)
        self.rbKnight.select()

        # Cleric Radio Button
        self.rbCleric = tkinter.Radiobutton(self, text="Cleric", font=self.font, variable=self.choice, value="2")
        self.rbCleric.grid(column=2, pady=10)

        # Thief Radio Button
        self.rbThief = tkinter.Radiobutton(self, text="Thief", font=self.font, variable=self.choice, value="3")
        self.rbThief.grid(column=2, pady=10)

        # Okay Button
        self.btnOkay = tkinter.Button(self, text="OK!", command=self.start_game)
        self.btnOkay.grid(column=2)

    def start_game(self):
        # Close the frame and start the game
        
        self.master.destroy()
        
        
            
        
def display():
    # Show the main menu
    gui = tkinter.Tk()
    gui.title("DD61")
    gui.geometry("640x480")

    app = main_menu_frame(gui)

    app.mainloop()
    return app.choice.get()

# Inform the user if this module has been ran directly
if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")


    


