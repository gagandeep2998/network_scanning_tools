from tkinter import *
from idlelib.tooltip import Hovertip
from tkinter import messagebox


class Scanner:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1366x768")
        self.window.title("Network Scanner")
        self.window.config(padx=20, pady=20)

        self.capture_button_img = PhotoImage(file='assets/images/capture.png')

        self.capture_button = Button(text='Capture Packets',
                                     image=self.capture_button_img)
        self.capture_tip = Hovertip(self.capture_button, "Capture Network Packets")

        self.capture_button.grid(row=0, column=0, padx=5, pady=5)

        self.stop_capture_button_img = PhotoImage(file='assets/images/stopping.png')

        self.stop_capture_button = Button(text='Stop Capture', image=self.stop_capture_button_img)
        self.stop_capture_tip = Hovertip(self.stop_capture_button, "Stop Capturing Network Packets")
        self.stop_capture_button.grid(row=0, column=1, padx=5, pady=5)

        self.trace_route_img = PhotoImage(file='assets/images/distance.png')
        self.trace_route_button = Button(text='Trace Route', image=self.trace_route_img)
        self.trace_route_tip = Hovertip(self.trace_route_button, "Trace Route")
        self.trace_route_button.grid(row=0, column=2, padx=5, pady=5)

        self.list_box = Listbox(height=200, width=200)
        self.list_box.grid(row=1, column=0, columnspan=100, pady=10, padx=5)

        self.window.mainloop()


scanner = Scanner()
