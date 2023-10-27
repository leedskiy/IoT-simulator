from IoTDevice import IoTDevice

class SmartLight(IoTDevice):
    def __init__(self, id, brightness):
        super().__init__(id)
        self.__brightness = brightness
    
    def get_brightness(self):
        return self.__brightness 

    def set_brightness(self, brightness):
        if self.__status == False and brightness > 0:
            self.__status = True
        elif self.__status == True and brightness == 0:
            self.__status == False

        self.__brightness = brightness

    def gradualDimming(self):
        pass