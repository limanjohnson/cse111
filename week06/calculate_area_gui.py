# Liam Nell 2025

import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
from math import pi

def populate_main_window(frm_main):
    """
    populate the main window of this program.
    """
    lbl_radius = Label(frm_main, text="Radius:")

    # Create an integer entry box where the user will enter her age.
    lbl_radius = IntEntry(frm_main, width=4, lower_bound=1)

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Create labels that will display the results.
    lbl_area = Label(frm_main, text="Area:")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_radius.grid(row=0, column=0, padx=3, pady=3)
    lbl_area.grid(row=1, column=0, padx=3, pady=3)
    lbl_radius.grid(row=0, column=1, padx=3, pady=3)
    btn_clear.grid(row=2, column=0, padx=3, pady=3)
    lbl_area.grid(row=1, column=1, padx=3, pady=3)
    btn_clear.grid(row=2, column=0, padx=3, pady=3)
    # Bind the button to the function that calculates the area.
    btn_clear.bind("<Button-1>", lambda event: calculate_area(lbl_radius, lbl_area))
    # Bind the button to the function that clears the entry boxes.
    btn_clear.bind("<Button-1>", lambda event: clear(lbl_radius, lbl_area))

    def calculate_area(event):
        """
        Calculate the area of a circle given the radius.
        """
        try:
            radius = float(lbl_radius.get())
            area = pi * radius ** 2
            lbl_area.config(text=f"{area:.2f}")

        except ValueError:
            lbl_area.config(text="")

    def clear():
        """
        Clear the entry boxes and labels.
        """
        btn_clear.focus()
        lbl_radius.clear()
        lbl_area.config(text="")
        lbl_radius.focus()

    # Bind the calculate function to the age entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    lbl_radius.bind("<KeyRelease>", calculate_area)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    lbl_radius.focus()

def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tKinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Calculate Area")
    frm_main.pack(padx=6, pady=6, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
