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

    def set_security_status(self, security_status):
        self.__security_status = security_status

    def get_motion(self):
        if self._status == Status.Off:
            return False

        return self.__motion

    def detect_motion(self, motion):
        if self._status == Status.Off:
            self._status = Status.On

        self.__motion = motion