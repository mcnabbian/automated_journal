from tkinter import *

# Create tk object
root = Tk()

# Create desired widgets
question = Label(root, text="What was your favorite part about today?")
text_box = Text(root, height=6, width=35, borderwidth=5, relief="groove", font=("Times", 14))
my_button = Button(root, text="Submit", padx=35)

# Add widgets to window
question.pack()
text_box.pack()
# my_entry.pack()
my_button.pack()

# Loop script to constantly update and keep running
root.mainloop()