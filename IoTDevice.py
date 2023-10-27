class IoTDevice:
    def __init__(self, id):
        self.__id = id
        self.__status = False
    
    def getStatus(self):
        return self.__status
    
    def setStatus(self, status):
        self.__status = status

    def getId(self):
        return self.__id
