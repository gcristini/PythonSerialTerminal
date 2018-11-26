# Created by gcristini at 24/10/2018

from CustomSerial.CustomSerial import CustomSerial
from CustomThread.ThreadManager import ThreadManager
from serial.serialutil import *
import serial

class SerialDataType(object):
    def __init__(self, port=None, baudrate=None, bytesize=None, parity=None, stopbits=None,
                 timeout=None, rx_bytes_available=None, rx_data=None, tx_data=None):
        self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits
        self.timeout = timeout
        self.rx_bytes_available = rx_bytes_available
        self.rx_data = rx_data
        self.tx_data = tx_data


class ThreadDataType(object):
    def __init__(self, thread_name=None, runnable=None, num_of_iter=None, start_delay_ms=None,
                 timing_ms=None, print_current_iter=None):
        self.thread_name = thread_name
        self.runnable = runnable
        self.num_of_iter = num_of_iter
        self.start_delay_ms = start_delay_ms
        self.timing_ms = timing_ms
        self.print_current_iter = print_current_iter


class SerialManager:
    """ """
    def __init__(self, port="", baudrate=115200, bytesize=EIGHTBITS, parity=PARITY_NONE,
                 stopbits=STOPBITS_ONE, timeout=None):

        self._serial_data = SerialDataType(port=port,
                                           baudrate=baudrate,
                                           bytesize=bytesize,
                                           parity=parity,
                                           stopbits=stopbits,
                                           timeout=timeout,
                                           rx_bytes_available=0,
                                           rx_data="",
                                           tx_data="")

        self._rx_thread_data = ThreadDataType(thread_name=self._serial_data.port + " RX Thread",
                                              runnable=self._rx_runnable,
                                              num_of_iter="Inf",
                                              start_delay_ms=0,
                                              timing_ms=0,
                                              print_current_iter=False)

        self._tx_thread_data = ThreadDataType(thread_name=self._serial_data.port + " TX Thread",
                                              runnable=self._tx_runnable,
                                              num_of_iter=1,
                                              start_delay_ms=0,
                                              timing_ms=0,
                                              print_current_iter=False)

        # Create serial object
        self._serialPort = CustomSerial(port=self._serial_data.port,
                                        baudrate=self._serial_data.baudrate,
                                        bytesize=self._serial_data.bytesize,
                                        parity=self._serial_data.parity,
                                        timeout=self._serial_data.timeout)

        # Create RX and TX thread objects
        self._rx_thread = ThreadManager(thread_name=self._rx_thread_data.thread_name,
                                        runnable=self._rx_thread_data.runnable,
                                        num_of_iter=self._rx_thread_data.num_of_iter,
                                        start_delay_ms=self._rx_thread_data.start_delay_ms,
                                        timing_ms=self._rx_thread_data.timing_ms,
                                        print_current_iter=self._rx_thread_data.print_current_iter)

        self._tx_thread = ThreadManager(thread_name=self._tx_thread_data.thread_name,
                                        runnable=self._tx_thread_data.runnable,
                                        num_of_iter=self._tx_thread_data.num_of_iter,
                                        start_delay_ms=self._tx_thread_data.start_delay_ms,
                                        timing_ms=self._tx_thread_data.timing_ms,
                                        print_current_iter=self._tx_thread_data.print_current_iter)

        # Init serial port
        self._serialPort.serial_init()

    def _rx_runnable(self):
        """ """
        # If there are bytes available on port, read!
        if self.rx_bytes_available > 0:  # if self._serialPort.byteAvailableRX > 0:
            self._serial_data.rx_data = self._serialPort.serial_read()
            # debug
            print(self._serial_data.rx_data)
        return self._serial_data.rx_data

    def start_rx_thread(self):
        """ """
        self._rx_thread.start()
        return

    def stop_rx_thread(self):
        """ """
        self._rx_thread.stop()
        return

    def pause_rx_thread(self):
        """ """
        self._rx_thread.pause()
        return

    def resume_rx_thread(self):
        """ """
        self._rx_thread.resume()
        return

    def _tx_runnable(self):
        """ """
        self._serialPort.serial_write(self._serial_data.tx_data)
        return

    def start_tx_thread(self):
        """ """
        self._tx_thread.start()
        return

    def stop_tx_thread(self):
        """ """
        self._rx_thread.stop()
        return

    def pause_tx_thread(self):
        """ """
        self._tx_thread.pause()
        return

    def resume_tx_thread(self):
        """ """
        self._tx_thread.resume()
        return

    # **** Getter/setter ***
    # Serial
    @property
    def rx_bytes_available(self):
        """ Return the number of available bytes on rx """
        # Search for number of available bytes on rx
        self._serial_data.rx_bytes_available = self._serialPort.bytes_available_rx

        return self._serial_data.rx_bytes_available

    @property
    def rx_serial_data(self):
        """ """
        return self._serial_data.rx_data

    @property
    def tx_serial_data(self):
        """ get tx_data string """
        return self._serial_data.tx_data

    @tx_serial_data.setter
    def tx_serial_data(self, tx_data):
        """ set tx_data string to passed value """
        self._serial_data.tx_data = tx_data
        return

    # RX Thread
    # @property
    # def rx_runnable(self):
    #     """ """
    #     return self._rx_thread.runnable
    #
    # @rx_runnable.setter
    # def rx_runnable(self, rx_runnable):
    #     """"""
    #     # Store runnable in local struct rx_thread_data
    #     self._rx_thread_data.runnable = rx_runnable
    #     # Set runnable
    #     self._rx_thread.runnable = rx_runnable
    #     return
    #s
    @property
    def rx_num_of_iter(self):
        """ """
        return self._rx_thread_data.num_of_iter

    @rx_num_of_iter.setter
    def rx_num_of_iter(self, rx_num_of_iter):
        """ """
        # Store num_of_iter in local data struct rx_thrad_data
        self._rx_thread_data.num_of_iter = rx_num_of_iter
        # Set num of iter
        self._rx_thread.num_of_iter = rx_num_of_iter
        return

    @property
    def rx_start_delay_ms(self):
        """ """
        return self._rx_thread_data.start_delay_ms

    @rx_start_delay_ms.setter
    def rx_start_delay_ms(self, rx_start_delay_ms):
        """"""
        # Store start_delay_ms in local data struct rx_thread_data
        self._rx_thread_data.start_delay_ms = rx_start_delay_ms
        # Set start_delay_ms
        self._rx_thread.start_delay_ms = rx_start_delay_ms
        return

    @property
    def rx_timing_ms(self):
        """ """
        return self._rx_thread_data.timing_ms

    @rx_timing_ms.setter
    def rx_timing_ms(self, rx_timing_ms):
        """ """
        # Store timing_ms in local data struct rx_thread_data
        self._rx_thread_data.timing_ms = rx_timing_ms
        # Set timing_ms
        self._rx_thread.timing_ms = rx_timing_ms
        return

    @property
    def rx_print_current_iter(self):
        """ """
        return self._rx_thread_data.print_current_iter

    @rx_print_current_iter.setter
    def rx_print_current_iter(self, rx_print_current_iter):
        """ """
        # Store timing_ms in local data struct rx_thread_data
        self._rx_thread_data.print_current_iter = rx_print_current_iter
        # Set timing_ms
        self._rx_thread.print_current_iter = rx_print_current_iter
        return

    # TX Thread
    # @property
    # def tx_runnable(self):
    #     """ """
    #     return self._tx_thread.runnable
    #
    # @tx_runnable.setter
    # def tx_runnable(self, tx_runnable):
    #     """"""
    #     # Store runnable in local struct tx_thread_data
    #     self._tx_thread_data.runnable = tx_runnable
    #     # Set runnable
    #     self._tx_thread.runnable = tx_runnable
    #     return

    @property
    def tx_num_of_iter(self):
        """ """
        return self._tx_thread_data.num_of_iter

    @tx_num_of_iter.setter
    def tx_num_of_iter(self, tx_num_of_iter):
        """ """
        # Store num_of_iter in local data struct tx_thrad_data
        self._tx_thread_data.num_of_iter = tx_num_of_iter
        # Set num of iter
        self._tx_thread.num_of_iter = tx_num_of_iter
        return

    @property
    def tx_start_delay_ms(self):
        """ """
        return self._tx_thread_data.start_delay_ms

    @tx_start_delay_ms.setter
    def tx_start_delay_ms(self, tx_start_delay_ms):
        """"""
        # Store start_delay_ms in local data struct tx_thread_data
        self._tx_thread_data.start_delay_ms = tx_start_delay_ms
        # Set start_delay_ms
        self._tx_thread.start_delay_ms = tx_start_delay_ms
        return

    @property
    def tx_timing_ms(self):
        """ """
        return self._tx_thread_data.timing_ms

    @tx_timing_ms.setter
    def tx_timing_ms(self, tx_timing_ms):
        """ """
        # Store timing_ms in local data struct tx_thread_data
        self._tx_thread_data.timing_ms = tx_timing_ms
        # Set timing_ms
        self._tx_thread.timing_ms = tx_timing_ms
        return

    @property
    def tx_print_current_iter(self):
        """ """
        return self._tx_thread_data.print_current_iter

    @tx_print_current_iter.setter
    def tx_print_current_iter(self, tx_print_current_iter):
        """ """
        # Store timing_ms in local data struct tx_thread_data
        self._tx_thread_data.print_current_iter = tx_print_current_iter
        # Set timing_ms
        self._tx_thread.print_current_iter = tx_print_current_iter
        return


class SerialScan:

    @staticmethod
    def scan(numOfPort):
        """ Scanning available serial ports up to "NumOfPort"
        Return a list of string with free serial ports
        """
        available_port_list = []  # List of available ports
        port = ""

        # Try to connect to a port: if successful save it in "availabilePortList"
        for i in range(numOfPort):
            try:
                port = "COM" + str(i + 1)
                CustomSerial(port=port)

                available_port_list.append(port)

                # if CustomSerial(port=port).is_open:
                #     CustomSerial(port=port).close()

            except serial.SerialException:
                # print("exception on COM" + str(i + 1))
                pass

        if len(available_port_list) == 0:
            available_port_list = "No COMs available"
        return available_port_list
