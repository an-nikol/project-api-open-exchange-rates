import tkinter as tk

window = tk.Tk()
window.title('Open Exchange Rates App')
window.geometry('650x450')

menu_text = """Menu

Please choose one of the options below:
1. All current currency rates
2. A specific currency rate
3. Convert from USD to another currency
4. Statistics for usage
5. Quit"""


center_label = tk. Label(
    window,
    text=menu_text,
    anchor='e',
    justify='left',
    font=('Times New Roman', 15, 'bold')
)
center_label.place(x=150, y= 20)


input_label = tk.Label(
    window,
    text="Enter your choice (1/2/3/4/5): ",
    font=('Times New Roman', 12, 'bold')
)
input_label.place(x=151, y= 242)
input_field = tk.Entry(window, width=20)
input_field.place(x=370, y=244)




window.mainloop()