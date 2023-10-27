from IoTDevice import IoTDevice

class SecurityCamera(IoTDevice):
    def __init__(self, id, security_status):
        super().__init__(id)
        self.__security_status = security_status
    
    