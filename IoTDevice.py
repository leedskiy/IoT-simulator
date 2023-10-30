from Status import Status

class IoTDevice:
    def __init__(self, id):
        self._id = id
        self._status = Status.Off
    
    def get_status(self):
        return self._status
    
    def set_status(self, status):
        self._status = status

    def get_id(self):
        return self._id
