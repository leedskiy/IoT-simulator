from IoTDevice import IoTDevice
from Status import Status
import random

class SecurityCamera(IoTDevice):
    def __init__(self, id, security_status):
        super().__init__(id)
        self.__security_status = security_status
        self.__motion = False

    def get_security_status(self):
        return self.__security_status

    def set_security_status(self):
        self.__security_status = security_status

    def getMotion(self):
        return self.__motion

    def detectMotion(self, motion):
        if self._status == Status.Off:
            self._status = Status.On

        self.__motion = motion