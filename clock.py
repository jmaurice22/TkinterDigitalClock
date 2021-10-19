from tkinter import *
from datetime import datetime

# Canvas to place widgets
frame = Tk()

# Set canvas title & size
frame.title('Clock')
frame.resizable(1, 1)

# Create clock
clock = Label(frame, font=("Sans-serif", 40, "bold"), fg="red", bg="black")
clock.grid(row=5, column=3)

# Get time
def displayClock():
    localtime = datetime.now()
    # Format time to 12 hour format
    time_text = localtime.strftime("%I:%M:%S")
    clock.configure(text=time_text)
    clock.after(200, displayClock)


# Display clock
displayClock()

# Mainloop
frame.mainloop()
