# Created by gcristini at 19/10/2018

import serial


class CustomSerial(serial.Serial):

    def __init__(self, **kwargs):
        """ Initialize (???) """
        super(CustomSerial, self).__init__(**kwargs)
        self._dataRX = ""
        self._bytes_available_rx = 0

    def serial_init(self):
        """ Open serial port, if closed """
        if self.is_open:
            self.close()
            self.open()
        else:
            None  # do nothing

    #@staticmethod
    def serial_write(self, data):
        """ Use 'write' method of Serial class enconding data in UTF-8"""
        self.write(data.encode())
        return

    def serial_read(self):
        """ Use 'read' method of Serial class enconding data in UTF-8"""
        # TODO controllare codifica!
        self._dataRX = self.read(self._bytes_available_rx).decode('utf-8')
        return self._dataRX

    @property
    def bytes_available_rx(self):
        """ Check available bytes of data """
        self._bytes_available_rx = self.inWaiting()
        return self._bytes_available_rx
