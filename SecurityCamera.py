from IoTDevice import IoTDevice

class SecurityCamera(IoTDevice):
    def __init__(self, id, securityStatus):
        super().__init__(id)
        self.__securityStatus = securityStatus
    
    