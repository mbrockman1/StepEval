'''
iOS pedometer
-----------------

Taken from: http://pyobjus.readthedocs.org/en/latest/pyobjus_ios.html \

'''

from plyer.facades import Pedometer
from pyobjus import autoclass
from pyobjus.dylib_manager import *

load_dylib('./UniBlocks.dylib')



class IosPedometer(Pedometer):

    def __init__(self):
        super().__init__()
        self._pedometer = autoclass('StepWorker').alloc().init()

    def _enable(self):
        '''Enable Step Counter sensor.'''
        self._pedometer.startPedometer()


    def _disable(self):
        '''Disable Step Counter sensor.'''
        self._pedometer.stopPedometer()

    def _get_count(self):
        return (
            self._pedometer.stepNumber,
            self._pedometer.distance)


def instance():
    return IosPedometer()
