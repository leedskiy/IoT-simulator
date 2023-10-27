from IoTDevice import IoTDevice

class SecurityCamera(IoTDevice):
    def __init__(self, id, security_status):
        super().__init__(id)
        self.__security_status = security_status

    def get_security_status(self):
        return self.__security_status

    def set_security_status(self):
        self.__security_status = security_status