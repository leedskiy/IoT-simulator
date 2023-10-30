from IoTDevice import IoTDevice
from Status import Status
import random

class SecurityCamera(IoTDevice):
    def __init__(self, id, security_status):
        super().__init__(id)
        self.__security_status = security_status

    def get_security_status(self):
        return self.__security_status

    def set_security_status(self):
        self.__security_status = security_status

    def detectMotion(self):
        if self._status == Status.Off:
            self._status == Status.On

        motion = True if random.randint(0,1) else False
        return motion