from datetime import datetime
from tkinter import *
from tkinter import messagebox

# Create tk object
root = Tk()


def get_date_time():
    # Converting datetime object to string
    # TODO: round seconds to nearest whole number
    date_time = datetime.now()
    date_time_string = date_time.strftime("%b-%d-%Y (%H:%M:%S.%f)")
    return date_time_string


def save_entry():
    #  open file and append, if it doesn't exist then create it.
    with open('journal_entries.txt', 'a+') as f:
        # .get the input in text widget at the first line, '0th' character, then read until the end
        f.write("\n" + get_date_time() + "\n" + text_box.get('1.0', 'end-1c'))


def popup():
    msg = messagebox.askyesno('Warning', 'Are you sure you would like to submit?')
    if msg:  # if user clicked yes
        save_entry()
        root.destroy()


# def submit():
#     """Command for the submit button. Ends the script and saves entry to database."""
#     # TODO: Add save entry to database functionality.
#

# Vertical (y) Scroll Bar
scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

# Create desired widgets
# TODO: Add other questions efficiently
question = Label(root, text="What was your favorite part about today?")
text_box = Text(root, height=6, width=35, borderwidth=5,
                relief="groove", font=("Times", 14), wrap=WORD)
my_button = Button(root, text="Submit", padx=35, command=popup)

# Add widgets to window
question.pack()
text_box.pack()
my_button.pack()

# Loop script to constantly update and keep running
root.mainloop()
