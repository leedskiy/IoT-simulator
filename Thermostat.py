from IoTDevice import IoTDevice

class Thermostat(IoTDevice):
    def __init__(self, id, temperature):
        super().__init__(id)
        self.__temperature = temperature
    
    