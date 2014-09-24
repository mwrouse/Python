"""
    Program......: challenge10_3.py
    Author.......: Michael Rouse
    Date.........: 3/4/14
    Description..: Create a GUI program called Order Up! that simulates an ordering menu
"""
from tkinter import *

class Application(Frame):
    """ Application Class """
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.font = "Arial 12"
        self.total_price = 0.00

        # Variables for Check boxes
        self.hotdog = BooleanVar()
        self.hamburger = BooleanVar()
        self.cheeseburger = BooleanVar()
        self.nachos = BooleanVar()
        self.fries = BooleanVar()
        self.tater_tots = BooleanVar()
        self.small_drink = BooleanVar()
        self.medium_drink = BooleanVar()
        self.large_drink = BooleanVar()
        
        self.create_widgets()

    def create_widgets(self):
        """ Create GUI Widgets """
        # Order Up! Logo
        self.lbl_orderUp = Label(self, text="Order Up!", font="Arial 22", foreground="red")
        self.lbl_orderUp.grid(column=0, row=0, columnspan=10, rowspan=4, sticky=W)

        # Order Up! Sub Text
        self.lbl_subText = Label(self, text="Restaurant Ordering Menu", font=self.font)
        self.lbl_subText.grid(column=10, row=2, columnspan=10, rowspan=2, sticky=W)

        # ==== Food ====
        self.lbl_food = Label(self, text="Food", font=self.font + " underline")
        self.lbl_food.grid(column=5, row=4, columnspan=5, rowspan=1, sticky=W)

        # Hot Dog
        Checkbutton(self, text="Hot Dog - $2.00", variable=self.hotdog, command=self.calculate_total, font=self.font).grid(column=2, row=5, columnspan=10, sticky=W)

        # Hamburger
        Checkbutton(self, text="Hamburger - $2.25", variable=self.hamburger, command=self.calculate_total, font=self.font).grid(column=2, row=6, columnspan=12, sticky=W)

        # Cheeseburger
        Checkbutton(self, text="Cheeseburger - $2.50", variable=self.cheeseburger, command=self.calculate_total, font=self.font).grid(column=2, row=7, columnspan=13, rowspan=1, sticky=W)

        # Nachos
        Checkbutton(self, text="Nachos - $1.75", variable=self.nachos, command=self.calculate_total, font=self.font).grid(column=2, row=9, columnspan=10, sticky=W)
        
        # ==== Sides ====
        self.lbl_sides = Label(self, text="Sides", font=self.font + " underline")
        self.lbl_sides.grid(column=10, row=4, padx=120, columnspan=65, rowspan=1, sticky=W)

        # Fries
        Checkbutton(self, text="Fries - $1.00", variable=self.fries, command=self.calculate_total, font=self.font).grid(column=14, row=5, columnspan=11, sticky=E)

        # Tater Tots
        Checkbutton(self, text="Tater Tots - $1.00", variable=self.tater_tots, command=self.calculate_total, font=self.font).grid(column=14, row=6, columnspan=30, sticky=E)

        # ==== Drinks ====
        self.lbl_drinks = Label(self, text="Drinks", font=self.font + " underline")
        self.lbl_drinks.grid(column=16, row=6, padx=5, pady=20, columnspan=10, rowspan=6, sticky=W)

        # Small Drink
        Checkbutton(self, text="Small - $1.00", variable=self.small_drink, command=self.calculate_total, font=self.font).grid(column=14, row=10, columnspan=11, sticky=E)

        # Medium Drink
        Checkbutton(self, text="Medium - $1.25", variable=self.medium_drink, command=self.calculate_total, font=self.font).grid(column=14, row=11, padx=5, columnspan=20, sticky=E)

        # Large Drink
        Checkbutton(self, text="Large - $1.35", variable=self.large_drink, command=self.calculate_total, font=self.font).grid(column=14, row=12, columnspan=12, sticky=E)

        # ==== Total Price ====
        self.lbl_price = Label(self, text="Cost: $0.00", font="Arial 20 bold", foreground="dark green")
        self.lbl_price.grid(column=1, row=11, columnspan=12, sticky=W)

    def calculate_total(self):
        """ Update The Total """
        self.total_price = 0.00
        
        """
        int(True) = 1
        int(False) = 0
        So if a box is checked it will end up adding (1 * price) otherwise (0 * price)
        """
        # Add Price of Foods
        self.total_price += (int(self.hotdog.get()) * 2.00)
        self.total_price += (int(self.hamburger.get()) * 2.25)
        self.total_price += (int(self.cheeseburger.get()) * 2.50)
        self.total_price += (int(self.nachos.get()) * 1.75)

        # Add Price of Sides
        self.total_price += (int(self.fries.get()) * 1.00)
        self.total_price += (int(self.tater_tots.get()) * 1.00)

        # Add Price of Drinks
        self.total_price += (int(self.small_drink.get()) * 1.00)
        self.total_price += (int(self.medium_drink.get()) * 1.25)
        self.total_price += (int(self.large_drink.get()) * 1.35)

        # Update the Label
        self.lbl_price.config(text="Cost: $" + str("%0.2f" % self.total_price))    
        
def main():
    """ Main Function """
    root = Tk()
    root.title("Order Up!")
    root.geometry("400x300")
    app = Application(root)
    root.mainloop()


main()
