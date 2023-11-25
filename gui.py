from tkinter import *

# create the main window of the app
root_win = Tk()
root_win.title('Open Exchange Rates App')

# geometry of the win
root_win.geometry('800x600')

menu_text = """Menu
Please choose one of the options below:
1. All current currency rates
2. A specific currency rate
3. Convert from USD to another currency'
4. Statistics for usage
5. Quit"""

# create a label widget
center_label = Label(
    root_win,
    text=menu_text,
    anchor='e',
    justify='left',
    # width=70,
    font=('Times New Roman', 15, 'bold')
)

# Pack the label widget to display it
center_label.pack()

# fix width and height

center_label.place(relx=0.5, rely=0.5, width=100, height=50)

# Run the application
root_win.mainloop()

# think what is your conception about the app