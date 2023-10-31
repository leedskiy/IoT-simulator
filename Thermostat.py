from IoTDevice import IoTDevice
from Status import Status

class Thermostat(IoTDevice):
    def __init__(self, id, temperature, min_temp, max_temp):
        super().__init__(id)
        self.__temperature = temperature
        self.__min_temp = min_temp
        self.__max_temp = max_temp

    def get_temperature(self):
        return self.__temperature

    def get_min_temp(self):
        return self.__min_temp

    def get_max_temp(self):
        return self.__max_temp

    def set_temperature(self, temperature):
        if self._status == Status.Off:
            self._status = Status.On
        
        if(self.__min_temp <= temperature and self.__max_temp >= temperature):
            self.__temperature = temperature
        else:
            print(f"Error. Temperature must be between {__min_temp} and {__max_temp}")

    def set_min_temp(self, min_temp):
        self.__min_temp = min_temp

    def set_max_temp(self, max_temp):
        self.__max_temp = max_temp
        
    def adjust_temperature(self, temperature):
        if self._status == Status.Off:
            self._status == Status.On
        
        new_temp = temperature + self.__temperature
        
        if(self.__min_temp <= new_temp and self.__max_temp >= new_temp):
            self.__temperature = new_temp
        else:
            print(f"Error. Temperature must be between {__min_temp} and {__max_temp}")