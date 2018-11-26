#!/usr/bin/env python
import serial
from SerialManager.SerialManager import SerialManager
from SerialManager.SerialManager import SerialScan
from CustomThread.ThreadManager import ThreadManager
from tkinter import *


class Main:

    def __init__(self, master=None):

        self.mainWindow = Tk()
        self.mainFrame = Frame(self.mainWindow, bg='black')
        self.mainFrame.place(relwidth=0.5, relheight=0.5)

        self.mainWindow.title("Serial Term")
        self.mainWindow.geometry('1960x1280')

        self._createWidgets()

        # # GUI
        # self._app = App("Serial Scanner", layout="grid", width=1280, height=960)
        # #self._app.
        # self._app_comListTitle = Text(self._app, text="Available COMs", grid=[0, 0])
        # self._app_comListBox = ListBox(self._app, items="", scrollbar=True, grid=[0, 1, 1, 10])
        # self._app_numOfComTextBox = TextBox(self._app, grid=[1, 1])
        # self._app_comListScanButton = PushButton(self._app, text="Scan", grid=[2, 1], command=self._com_scan)
        #
        # self._app.display()
        #

    def _com_list_label(self):
        self.comLabel = Label(master=self.mainFrame, text="COM list", textvariable=True, bg='green')
        self.comLabel.place(relwidth=0.2, relheight=0.06, relx=0.12, rely=0.1, anchor=CENTER)
        return

    def _com_list_listbox(self):
        self.comList = Listbox(master=self.mainFrame)
        self.comList.place(relwidth=0.2, relheight=0.3, relx=0.12, rely=0.3, anchor=CENTER)
        # add scrollbar
        return

    def _num_of_com_to_scan_entry(self):
        self.numOfComsToScan = Entry(self)
        self.numOfComsToScan.place(relwidth=0)

    def _scan_button(self):
        self.scanButton = Button(self, text="Scan", padx=10, pady=5)
        self.scanButton.place()
        return

    def _createWidgets(self):
        self._com_list_label()
        self._com_list_listbox()
        #self._num_of_com_to_scan_entry()
        #self._scan_button()
        return









        #self.comList.grid.place()
        #self.numOfComsToScan.place()





    def _com_scan(self):
        # # Get number of COMs to scanning for
        # self._numOfComs = self._app_numOfComTextBox.get()
        # # Scan
        # self._availableComs = SerialScan.scan(numOfPort=int(self._numOfComs))
        # # Clear list box and update
        # self._app_comListBox.clear()
        #
        # for i in range(len(self._availableComs)):
        #     self._app_comListBox.append(self._availableComs[i])

        return

    def _com_connect(self):

        return


main = Main()
main.mainWindow.mainloop()
#main.mainLoop()





# availableComs=[]
# numOfComs=0
#
#
#
#
# print(availableComs)
#
#
# comDevice1 = SerialManager(port="COM4",
#                            baudrate=115200,
#                            bytesize=serial.EIGHTBITS,
#                            timeout=None)
#
# # com4 = SerialManager(port="COM5",
# #                      baudrate=115200,
# #                      bytesize=serial.EIGHTBITS,
# #                      timeout=None)
#
# text = None
# def inputRunnable():
#     text = input()
#
#     if text is not None:
#         # com4.tx_serial_data = text
#         # com4.start_tx_thread()
#         comDevice1.tx_serial_data = text + "\n"
#         comDevice1.start_tx_thread()
#         text = None
#
#     return
#
#
# inputThread = ThreadManager(num_of_iter="Inf",
#                             timing_ms=0,
#                             runnable=inputRunnable
#                             )
#
# comDevice1.start_rx_thread()
# inputThread.start()
#
# inputThread.join()
#
