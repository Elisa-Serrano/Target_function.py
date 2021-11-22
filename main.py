# Target function
## Given an even number of particles, find the way to group them in pairs
# so that the target function is minimized
import numpy as np


##ordenate function
# ordenate a list of number (particle's position)

def ordenate(a):
    # a
    d = len(a)
    for i in range(d - 1):
        for j in range(i + 1, 0, -1):
            if (a[j] < a[j - 1]):
                amin = a[j]
                amax = a[j - 1]
                a[j] = amax
                a[j - 1] = amin
            else:
                break
    return a


## Once the positions are ordenate, we only have to sum the distance between consecuitve particles

def target_f(a):
    # a is a list of particle's position
    n = len(a)
    s = 0
    for i in range(0, n, 2):
        s += abs(a[i] - a[i + 1])
    return int(s)
