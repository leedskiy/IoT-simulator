import tkinter as tk
from tkinter import *
from AutomationSystem import AutomationSystem
import threading
import time
from Status import Status

class App():
    def __init__(self):
        # AutomationSystem
        self.asys = AutomationSystem()
        self.asys.add_devices()
        self.devices = self.asys.get_devices()

        # root and frame
        self.root = tk.Tk()
        self.root.geometry('700x500')
        self.root.title('IoT simulator RP0KRP')
        self.mainframe = tk.Frame(self.root, background='#dfdfdf')
        self.mainframe.pack(fill='both', expand=True)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # automation
        self.automation_running = False
        self.update_gui()
        self.automation_button = Button(self.mainframe, text="Automation ON/OFF", 
                                        command=self.on_off_automation, padx=10, pady=5)
        self.automation_button.pack()
        self.loop_thread = None
        
        self.text_block = Label(self.mainframe, text = "Automation Status: OFF", background='#dfdfdf', padx=10, pady=10)
        self.text_block.pack()

        # status box
        self.status_box = Text(self.mainframe, height = 3, width = 40, padx=10, pady=10)
        self.status_text = ("Living room light status: OFF\n" +
                            "Living room thermostat status: OFF\n" + 
                            "Front door status: OFF")
        self.status_box.insert("1.0", self.status_text)
        self.status_box.pack()
        
        # light
        self.text_block2 = Label(self.mainframe, text = "Living room light brightness", background='#dfdfdf', padx=10, pady=10)
        self.text_block2.pack()
        self.slider1 = Scale(self.mainframe, from_=0, to=100, orient=HORIZONTAL, background='#dfdfdf', 
                            highlightthickness=0, command=self.change_li_brigt)
        self.slider1.pack()
        light_button = Button(self.mainframe, text="Toggle ON/OFF", 
                            command=self.on_off_light, padx=10, pady=5)
        light_button.pack()
        self.text_block3 = Label(self.mainframe, text = "Living room light - 0%", background='#dfdfdf', padx=10, pady=10)
        self.text_block3.pack()

        self.root.mainloop()

    # automation
    def on_off_automation(self):
        if not self.automation_running:
            self.automation_running = True
            self.text_block.config(text="Automation Status: ON")
            self.loop_thread = threading.Thread(target = self.call_exec_automation_tasks)
            self.loop_thread.start()
        else:
            self.automation_running = False   
            self.text_block.config(text="Automation Status: OFF")

    def call_exec_automation_tasks(self):
        while self.automation_running:
            self.asys.exec_automation_tasks()
            self.update_status_box()
            time.sleep(1)
    
    def on_closing(self):
        if self.loop_thread:
            self.automation_running = False
            self.loop_thread.join()
        self.root.destroy()

    def update_gui(self):
        if self.automation_running:
            self.asys.exec_automation_tasks()
            self.update_status_box()
        self.root.after(1000, self.update_gui)

    # status box
    def update_status_box(self):
        self.status_text = (f"Living room light status: {'ON' if self.devices[0].get_status() == Status.On else 'OFF'}\n" + 
                            f"Living room thermostat status: {'ON' if self.devices[1].get_status() == Status.On else 'OFF'}\n" +
                            f"Front door camera status: {'ON' if self.devices[2].get_status() == Status.On else 'OFF'}")
        self.status_box.delete("1.0", "end")
        self.status_box.insert("1.0", self.status_text)

    # light
    def change_li_brigt(self, num):
        self.devices[0].set_brightness(int(num))
        self.text_block3.config(text=f"Living room light - {self.devices[0].get_brightness()}%")
        self.update_status_box()

    def on_off_light(self):
        if(self.devices[0].get_status() == Status.Off):
            self.devices[0].set_status(Status.On)
        else:
            self.devices[0].set_status(Status.Off)

        self.update_status_box()

if __name__ == '__main__':
    App()