import tkinter as tk;
import tkcalendar;

Window = tk.Tk()  # --> making a instance of tkinter
Window.geometry("400x400")   #  ---> setting sizeof window
Window.title("📅 Date Picker")   #  ---> setting tittle to tk 

#  creating and styling calender
calendar = tkcalendar.Calendar(Window);
calendar.pack(pady=15)


# creating function for getting seleced date
def _get_data():
    output.config(text = f'YOU SELECTED : {calendar.get_date()}');  #  ---> setting label config as selected data


#  creatign and styline button
Button = tk.Button(Window , text="select data" , command = _get_data);
Button.pack(pady=15)

# creating label for output
output = tk.Label(Window , text="");
output.pack(pady=30)

Window.mainloop()