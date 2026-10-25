import ctypes
class dynamicarray:

  def __init__(self,n):
    self.n=0
    self.capacity=1
    self.arr=self._makearray(self.capacity)
