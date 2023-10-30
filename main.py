import tkinter as tk
from tkinter import *
from AutomationSystem import AutomationSystem
import threading
import time

class App():
    def __init__(self):
        # AutomationSystem
        self.asys = AutomationSystem()
        self.asys.addDevices()
        
        # root and frame
        self.root = tk.Tk()
        self.root.geometry('700x500')
        self.root.title('IoT simulator RP0KRP')
        self.mainframe = tk.Frame(self.root, background='#dfdfdf')
        self.mainframe.pack(fill='both', expand=True)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # automation
        self.automation_running = False
        automationButton = Button(self.mainframe, text="Automation ON/OFF", 
            command=self.on_off_automation, padx=10, pady=10)
        automationButton.pack()
        self.loop_thread = None
        
        self.text_block = Label(self.mainframe, text = "Automation Status: OFF", background='#dfdfdf', padx=10, pady=10)
        self.text_block.pack()

        # status box
        self.status_box = Text(self.mainframe, height = 3, width = 40, padx=10, pady=10)
        self.status_text = "Living room light status: OFF\nLiving room thermostat status: OFF\nFront door status: OFF"
        self.status_box.insert("1.0", self.status_text)
        self.status_box.pack()
        
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
            time.sleep(1)
    
    def on_closing(self):
        if self.loop_thread:
            self.automation_running = False
            self.loop_thread.join()
        self.root.destroy()

if __name__ == '__main__':
    App()