from IoTDevice import IoTDevice

class SmartLight(IoTDevice):
    def __init__(self, id, brightness):
        super().__init__(id)
        self.__brightness = brightness
    
    