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
        self.root.geometry('1000x700')
        self.root.title('IoT simulator RP0KRP')
        self.mainframe = tk.Frame(self.root, background='#dfdfdf')
        self.mainframe.pack(fill='both', expand=True)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # automation
        self.automation_running = False
        self.update_gui()
        self.automation_button = Button(self.mainframe, text="Automation ON/OFF", 
                                        command=self.on_off_automation, padx=10, pady=2)
        self.automation_button.pack()
        self.loop_thread = None
        
        self.text_block = Label(self.mainframe, text = "Automation Status: OFF", background='#dfdfdf', padx=10, pady=10)
        self.text_block.pack()

        # status box
        self.status_box = Text(self.mainframe, height = 3, width = 40, padx=10, pady=10)
        self.status_text = ("Living room light status: OFF\n" +
                            "Living room thermostat status: OFF\n" + 
                            "Front door camera status: OFF")
        self.status_box.insert("1.0", self.status_text)
        self.status_box.pack()
        
        # light
        self.text_block2 = Label(self.mainframe, text = "Living room light brightness", background='#dfdfdf', padx=10, pady=5)
        self.text_block2.pack()
        self.slider1 = Scale(self.mainframe, from_=0, to=100, orient=HORIZONTAL, background='#dfdfdf', 
                            highlightthickness=0, command=self.change_li_brigt)
        self.slider1.pack()
        self.light_button = Button(self.mainframe, text="Toggle ON/OFF", 
                            command=self.on_off_light, padx=10, pady=2)
        self.light_button.pack()
        self.text_block3 = Label(self.mainframe, text = "Living room light - 0%", background='#dfdfdf', padx=10, pady=10)
        self.text_block3.pack()

        # thermostat
        self.text_block4 = Label(self.mainframe, text = "Living room thermostat temperature", background='#dfdfdf', padx=10, pady=5)
        self.text_block4.pack()
        self.slider2 = Scale(self.mainframe, from_=self.devices[1].get_min_temp(), to=self.devices[1].get_max_temp(), orient=HORIZONTAL, background='#dfdfdf', highlightthickness=0, command=self.change_th_temp)
        self.slider2.pack()
        thermostat_button = Button(self.mainframe, text="Toggle ON/OFF", 
                            command=self.on_off_thermostat, padx=10, pady=2)
        thermostat_button.pack()
        self.text_block5 = Label(self.mainframe, text = f"Living room thermostat - {self.devices[1].get_temperature()}C", background='#dfdfdf', padx=10, pady=10)
        self.text_block5.pack()

        # camera
        self.text_block6 = Label(self.mainframe, text = "Front door camera motion detection", background='#dfdfdf', padx=10, pady=5)
        self.text_block6.pack()
        self.motion_detect_button = Button(self.mainframe, text="Random detect motion", 
                            command=self.detect_motion, padx=10, pady=2)
        self.motion_detect_button.pack()
        self.camera_button = Button(self.mainframe, text="Toggle ON/OFF", 
                            command=self.on_off_camera, padx=10, pady=2)
        self.camera_button.pack()
        self.text_block7 = Label(self.mainframe, text = f"Front door camera motion - {'YES' if self.devices[2].getMotion() else 'NO'}", background='#dfdfdf', padx=10, pady=10)
        self.text_block7.pack()
        
        # text
        self.text_block8 = Label(self.mainframe, text = ("Automation rule: turn on lights " +
                                "when motion is detected"), background='#dfdfdf', padx=10, pady=10)
        self.text_block8.pack()

        # sensor data
        self.text_block9 = Label(self.mainframe, text = ("Sensor data box (5 sec update):"),
                                 background='#dfdfdf', padx=10, pady=10)
        self.text_block9.pack()

        self.sensor_data_box = Text(self.mainframe, height=3, width = 70, padx=10, pady=10)
        self.iter = -3
        self.loop_thread2 = threading.Thread(target = self.call_gather_sensor_data, daemon=True)
        self.loop_thread2.start()
        self.sensor_data_box.pack()

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

        self.asys.store_sensor_data()
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

    # thermostat
    def change_th_temp(self, num):
        self.devices[1].set_temperature(int(num))
        self.text_block5.config(text=f"Living room thermostat - {self.devices[1].get_temperature()}C")
        self.update_status_box()

    def on_off_thermostat(self):
        if(self.devices[1].get_status() == Status.Off):
            self.devices[1].set_status(Status.On)
        else:
            self.devices[1].set_status(Status.Off)

        self.update_status_box()

    # camera
    def detect_motion(self):
        self.asys.randomize_detect_motion()
        self.text_block7.config(text=f"Front door camera motion - {'YES' if self.devices[2].getMotion() else 'NO'}")
        self.update_status_box()

    def on_off_camera(self):
        if(self.devices[2].get_status() == Status.Off):
            self.devices[2].set_status(Status.On)
        else:
            self.devices[2].set_status(Status.Off)

        self.update_status_box()

    # sensor data
    def call_gather_sensor_data(self):
        while True:
            self.asys.gather_sensor_data()
            self.sensor_data_array = self.asys.get_sensor_data()
            self.sensor_data_lines = ""
            self.iter += 3
            for i in range(self.iter, self.iter + 3):
                self.sensor_data_lines += self.sensor_data_array[i]
            self.sensor_data_box.delete("1.0", "end")
            self.sensor_data_box.insert("1.0", self.sensor_data_lines)
            time.sleep(5)

if __name__ == '__main__':
    App()