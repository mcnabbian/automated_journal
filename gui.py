from datetime import datetime
from tkinter import *
from tkinter import messagebox


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

# Create tk object
root = Tk()

canvas = Canvas(root)  # TODO: What is a canvas and why do I add a frame to it?
scroll_y = Scrollbar(root, orient='vertical', command=canvas.yview)
frame = Frame(root)

# Create desired widgets
with open('questions.txt', 'r') as f:
    for line in f:

        # initialize widgets
        question = Label(frame, text=line[:-1])  # cut last char from string because it's a '/n'
        text_box = Text(frame, height=6, width=35, borderwidth=5,
                        relief="groove", font=("Times", 14), wrap=WORD)

        # add widgets to frame
        question.pack(side="top")
        text_box.pack(side="top")
button = Button(frame, text="Submit", padx=35, command=popup)
button.pack(side="bottom")

# create new window, put frame in canvas
canvas.create_window(0, 0, anchor='nw', window=frame)
canvas.update_idletasks()  # TODO: not really sure what this does
canvas.configure(scrollregion=canvas.bbox('all'),
                 yscrollcommand=scroll_y.set)  # TODO: scroll region currently only on the scroll bar, idk why

canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', side='right')
# Add widgets to window
# question.pack(side="top")
# text_box.pack(side="top")
# scroll.pack(side=RIGHT, fill=Y)
# button = Button(frame, text="Submit", padx=35, command=popup)
# button.pack(side="bottom")

# Loop script to constantly update and keep running
root.mainloop()
