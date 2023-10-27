class IoTDevice:
    def __init__(self, id):
        self.__id = id
        self.__status = False
    
    def get_status(self):
        return self.__status
    
    def set_status(self, status):
        self.__status = status

    def get_id(self):
        return self.__id
