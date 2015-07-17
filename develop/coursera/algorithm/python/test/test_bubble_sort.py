import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../sort'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../log'))
from bubble_sort import bubble_sort


def test():
    aa = [45, 67, 656, 232, 100, 10, 3, 1]
    bubble_sort(aa)
