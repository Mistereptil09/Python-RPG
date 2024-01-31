from tkinter import *


root = Tk()
# place a label on the root window
message = Label(root, text="Bonjour", font=("Arial"))
message.pack()
Label(root, text="Hello world", font=("Arial")).pack()
root.title("game.py")

# To get the current title of a window, you use the title() method with no argument:
# title = window.title()

# In the program, the following creates a Label widget placed on the root window:
# message = tk.Label(root, text="Hello, World!")
# Code language: Python (python)
# The following statement positions the Label on the main window:
# message.pack()


# to create a widget : widget = WidgetName(master, **options)
# The master is the parent window or frame where you want to place the widget.
# The options is one or more keyword arguments that specify the configurations of the widget.

# keep the window displaying
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()