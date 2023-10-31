from IoTDevice import IoTDevice
from Status import Status
import time

class SmartLight(IoTDevice):
    def __init__(self, id, brightness):
        super().__init__(id)
        self.__brightness = brightness
    
    def set_status(self, status):
        if status == Status.On and self.__brightness == 0:
            self.__brightness = 1
        elif status == Status.Off and self.__brightness > 0:
            self.__brightness = 0
        
        self._status = status

    def get_brightness(self):
        return self.__brightness 

    def set_brightness(self, brightness):
        if self._status == Status.Off and brightness > 0:
            self._status = Status.On
        elif self._status == Status.On and brightness == 0:
            self._status = Status.Off

        self.__brightness = brightness

    def gradual_dimming(self, steps, duration, delay, step_size):
        for _ in range(steps):
            new_brightness = self.__brightness - step_size
            if(new_brightness >= 0):
                self.__brightness = new_brightness
            time.sleep(delay)

        self.__brightness = 0
        self._status = Status.Off