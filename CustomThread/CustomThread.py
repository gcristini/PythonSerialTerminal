from threading import Thread
import time
from CustomThread.ThreadClassEnums import *


def dummy_runnable():
    print("No runnable element passed as argument")
    return


class CustomThread(Thread):
    """ Extend class Thread """

    def __init__(self, thread_name="", runnable=dummy_runnable, num_of_iter=1, start_delay_ms=0, timing_ms=0,
                 print_current_iter=False):
        super().__init__()
        self._name = thread_name
        self._runnable = runnable
        if (type(num_of_iter) == int) or (num_of_iter == "Inf"):
            self._num_of_iter = num_of_iter
        else:
            raise ValueError("num_of_iter must be integer or 'Inf' value only")

        self._start_delay = start_delay_ms / 1000
        self._timing = timing_ms / 1000
        self._print_current_iter = print_current_iter

        self._exit_condition = False  # While loop exit condition
        self._current_iter = 1
        self._thread_status = ThreadStatesEnum.TS_INIT
        self._thread_command = ThreadCommandEnum.TC_INIT
        self._last_thread_command = self._thread_command
        return

    def run(self):
        """ Overriding run method of class Thread """
        # Run the looping state machine
        while not self._exit_condition:
            # Execute the state function depending by thread status
            self._state_machine_manager(self.thread_status)
            # Store last thread command
            self._last_thread_command = self._thread_command
        return

    def pause(self):
        """ Pause thread from running status """
        # Pause is allowed only if thread is running or initialing
        if ((self._thread_status == ThreadStatesEnum.TS_RUNNING) or
                (self._thread_status == ThreadStatesEnum.TS_INIT)):
            self._thread_command = ThreadCommandEnum.TC_PAUSE
        return

    def resume(self):
        """ Resume thread from paused status """
        # Resume is allowed only if thread is paused
        if self._thread_status == ThreadStatesEnum.TS_PAUSED:
            self._thread_command = ThreadCommandEnum.TC_RESUME
        return

    def stop(self):
        """ Stop thread """
        self._thread_command = ThreadCommandEnum.TC_STOP
        return

    @property
    def thread_status(self):
        return self._thread_status

    """ State Machine to manage thread """
    def _init_state_manager(self):
        # Pause for start_delay time
        time.sleep(self._start_delay)
        # Go to running state
        self._thread_status = ThreadStatesEnum.TS_RUNNING
        # Thread start
        print(self._name + ": start")
        return

    def _running_state_manager(self):
        if self._print_current_iter:
            print(self._name + ": iteration n. " + str(self._current_iter))
        # Increment counter
        self._current_iter += 1

        # Execute Runnable element
        self._runnable()

        if self._thread_command == ThreadCommandEnum.TC_PAUSE:
            # Go to paused state
            print(self._name + ": paused")
            self._thread_status = ThreadStatesEnum.TS_PAUSED
        elif ((self._thread_command == ThreadCommandEnum.TC_STOP) or
              (self._current_iter-1 == self._num_of_iter)):
            # Go to stopped state
            print(self._name + ": stopped")
            self._thread_status = ThreadStatesEnum.TS_STOPPED
        # Wait
        time.sleep(self._timing)
        return

    def _stopped_state_manager(self):
        self._exit_condition = True
        return

    def _paused_state_manager(self):
        while 1:
            if self._thread_command == ThreadCommandEnum.TC_RESUME:
                # Go to running state
                print(self._name + ": resume")
                self._thread_status = ThreadStatesEnum.TS_RUNNING
                break
            elif self._thread_command == ThreadCommandEnum.TC_STOP:
                # Go to running state
                print(self._name + ": stop")
                self._thread_status = ThreadStatesEnum.TS_STOPPED
                break
        return

    def _state_machine_manager(self, thread_state):
        thread_fun_dict = {
            ThreadStatesEnum.TS_INIT: self._init_state_manager,
            ThreadStatesEnum.TS_RUNNING: self._running_state_manager,
            ThreadStatesEnum.TS_STOPPED: self._stopped_state_manager,
            ThreadStatesEnum.TS_PAUSED: self._paused_state_manager
        }
        # Get function from dictionary
        fun = thread_fun_dict.get(thread_state)
        # Execute function
        fun()
        return

