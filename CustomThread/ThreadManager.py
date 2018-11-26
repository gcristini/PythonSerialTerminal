from CustomThread.CustomThread import CustomThread
from CustomThread.ThreadClassEnums import ThreadStatesEnum


class ThreadManager:

    def __init__(self, thread_name="", runnable=(), num_of_iter=1, start_delay_ms=0, timing_ms=0,
                 print_current_iter=False):

        self._name = thread_name
        self._runnable = runnable

        if (type(num_of_iter) == int) or (num_of_iter == "Inf"):
            self._num_of_iter = num_of_iter
        else:
            raise ValueError("num_of_iter must be integer or 'Inf' value only")

        self._start_delay_ms = start_delay_ms
        self._timing_ms = timing_ms
        self._print_current_iter = print_current_iter

        # Create ad initialize thread object
        self.thread = self.init()
        return

    def init(self):
        thread = CustomThread(thread_name=self._name,
                              runnable=self._runnable,
                              num_of_iter=self._num_of_iter,
                              start_delay_ms=self._start_delay_ms,
                              timing_ms=self._timing_ms,
                              print_current_iter=self._print_current_iter)
        return thread

    def start(self):
        if ((self.thread.thread_status == ThreadStatesEnum.TS_INIT) or
                (self.thread.thread_status == ThreadStatesEnum.TS_STOPPED)):
            self.thread = self.init()
            self.thread.start()
        else:
            #TODO run exception?
            print("Stop thread to start it a new time")
        return

    def stop(self):
        self.thread.stop()
        self.join()
        return

    def pause(self):
        self.thread.pause()
        return

    def resume(self):
        self.thread.resume()
        return

    def join(self, timeout=None):
        self.thread.join(timeout)

    def thread_status(self):
        return self.thread.thread_status

    @property
    def thread_name(self):
        """ """
        return self._name

    @thread_name.setter
    def thread_name(self, name):
        """ """
        self._name = name
        return

    @property
    def runnable(self):
        """ """
        return self._runnable

    @runnable.setter
    def runnable(self, runnable):
        """ """
        self._runnable = runnable
        pass

    @property
    def num_of_iter(self):
        """ """
        return self._num_of_iter

    @num_of_iter.setter
    def num_of_iter(self, num_of_iter):
        """ """
        if (type(num_of_iter) == int) or (num_of_iter == "Inf"):
            self._num_of_iter = num_of_iter
        else:
            raise ValueError("num_of_iter must be integer or 'Inf' value only")
        pass

    @property
    def start_delay_ms(self):
        """ """
        return self._start_delay_ms

    @start_delay_ms.setter
    def start_delay_ms(self, start_delay_ms):
        """ """
        self._start_delay_ms = start_delay_ms
        pass

    @property
    def timing_ms(self):
        """ """
        return self._timing_ms

    @timing_ms.setter
    def timing_ms(self, timing_ms):
        """"""
        self._timing_ms = timing_ms
        pass

    @property
    def print_current_iter(self):
        """ """
        return self._print_current_iter

    @print_current_iter.setter
    def print_current_iter(self, print_current_iter):
        """ """
        if type (print_current_iter) != bool:
            raise ValueError("Value must be bool only")
        else:
            self._print_current_iter = print_current_iter
        pass
