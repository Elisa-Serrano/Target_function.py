# script for test function
import numpy as np
from main import ordenate
from main import target_f


def test():
     pass

#test to ordenate particle's positions
a = np.array([-3, 2, -1, 1])

def test_ordenate():
     #a is a lsit of particle's positions
     global a
     n = len(a)
     t = True
     b = ordenate(a)
     for i in range(n-1):
          if (b[i]>b[i+1]):
               t = False

     assert t

def test_target():
     global a
     n = len(a)
     assert target_f(a) == 3
