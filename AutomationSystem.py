from IoTDevice import IoTDevice
from SmartLight import SmartLight
from Thermostat import Thermostat
from SecurityCamera import SecurityCamera
from Status import Status
import random
from datetime import date
from datetime import datetime
from os import strerror

class AutomationSystem:
    def __init__(self):
        self.__devices = []
        self.__sensor_data = []
    
    def get_devices(self):
        return self.__devices

    def add_devices(self):
        sl = SmartLight(0, 0)
        th = Thermostat(1, 0, 0, 30)
        sc = SecurityCamera(2, "secure")

        self.__devices.append(sl)
        self.__devices.append(th)
        self.__devices.append(sc)

    def exec_automation_tasks(self):
        if self.__devices[2].get_motion():
            self.__devices[0].set_status(Status.On)
            if self.__devices[0].get_brightness() == 0:
                self.__devices[0].set_brightness(1)

    def randomize(self):        
        self.__devices[0].set_brightness(random.randint(0,100))

        min_t = random.randint(0,30)
        self.__devices[1].set_min_temp(min_t)
        self.__devices[1].set_max_temp(random.randint(min_t,30))

        self.__devices[1].set_temperature(random.randint(
                self.__devices[1].get_min_temp(), self.__devices[1].get_max_temp()))

        self.__devices[2].detect_motion(True if random.randint(0,1) else False)

    def randomize_detect_motion(self):  
        self.__devices[2].detect_motion(True if random.randint(0,1) else False)

    def get_sensor_data(self):
        return self.__sensor_data

    def gather_sensor_data(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.__sensor_data.append("[" + str(date.today()) + " " + current_time + "] " + "Living room Light brightness: " + str(self.__devices[0].get_brightness()) + "%" + "\n")
        self.__sensor_data.append("[" + str(date.today())  + " " + current_time + "] " + "Living room Thermostat temperature: " + str(self.__devices[1].get_temperature()) + "C" + "\n")
        self.__sensor_data.append("[" + str(date.today())  + " " + current_time + "] " + "Front door camera motion: " + str(self.__devices[2].get_motion()) + "\n\n")
    
    def store_sensor_data(self):
        try:
            fo = open('out.txt', "wt")
            for line in self.__sensor_data:
                fo.write(line)
            fo.close()
        except IOError as e:
            print("Error: ", strerror(e.errno))