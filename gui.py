from datetime import datetime
from tkinter import *
from tkinter import messagebox


def get_date_time():
    """Return current date and time as a string."""
    date_time = datetime.now()
    date_time_string = date_time.strftime("%b-%d-%Y (%H:%M:%S)")
    return date_time_string


def save():
    """Write user's input to text file upon submit."""
    # open file and append, if it doesn't exist then create it.
    with open('journal_entries.txt', 'a+') as f:
        # .get the input in text widget at the first line, '0th' character, then read until the end
        f.write("\n" + get_date_time())
        for i in range(len(entries)):
            string = entries[i].get('1.0', 'end-1c')
            if string:
                f.write("\n" + string)


def popup():
    """Display popup message confirming submission."""
    msg = messagebox.askyesno('Warning', 'Are you sure you would like to submit?')
    if msg:  # if user clicked yes
        save()
        root.destroy()


# initialize tkinter
root = Tk()
root.geometry('510x500')

# initialize canvas to use scrollbar
canvas = Canvas(root)
scroll_y = Scrollbar(root, orient='vertical', command=canvas.yview)

# initialize frame to pack widgets into
frame = Frame(root, bd='25', padx='75')

# initialize questions and text boxes
entries = []
i = 0
with open('questions.txt', 'r') as f:
    for line in f:
        q1 = Label(frame, text=line[:-1])  # cut last char from line b/c it's '\n'
        q1.pack()
        entries.append(Text(frame, height=6, width=35, borderwidth=5,
                            relief="groove", font=("Times", 14), wrap=WORD))
        entries[i].pack()
        i += 1

# initialize submit button
button = Button(frame, text="Submit", padx=35, command=popup)

# create new window, put frame in canvas
canvas.create_window(0, 0, anchor='nw', window=frame)
canvas.update_idletasks()  # not sure what this really does but not having it breaks the program
canvas.configure(scrollregion=canvas.bbox('all'),
                 yscrollcommand=scroll_y.set)

# add widgets to gui
canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', side='right')
button.pack(side="bottom")

# Loop script to constantly update and keep running
root.mainloop()
