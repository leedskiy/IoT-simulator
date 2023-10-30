from IoTDevice import IoTDevice
from Status import Status

class SmartLight(IoTDevice):
    def __init__(self, id, brightness):
        super().__init__(id)
        self.__brightness = brightness
    
    def get_brightness(self):
        return self.__brightness 

    def set_brightness(self, brightness):
        if self._status == Status.Off and brightness > 0:
            self._status = Status.On
        elif self._status == Status.On and brightness == 0:
            self._status == Status.Off

        self.__brightness = brightness

    def gradualDimming(self):
        pass