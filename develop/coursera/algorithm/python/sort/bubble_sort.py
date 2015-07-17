import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../log'))
from logger import Logger

def bubble_sort(array):
    Logger.info('bubule sort')
    Logger.info('input: %s' % array)
    length = len(array)
    for i in range(length - 1, -1, -1):
        Logger.info('i: %s' % i)
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        Logger.info('internal: %s' % array)

    Logger.info('output: %s' % array)
