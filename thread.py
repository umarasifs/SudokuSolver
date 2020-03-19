import threading
import main
import sudoku
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

    def run(self):
        if self.name == 1:
            main.update()
        if self.name == 2:
            sudoku.solve()