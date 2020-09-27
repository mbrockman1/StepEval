'''
macOS pedometer
-----------------

Taken from: http://pyobjus.readthedocs.org/en/latest/pyobjus_ios.html \

'''

from plyer.facades import Pedometer



class macOSPedometer(Pedometer):

    def __init__(self):
        super().__init__()
        pass

    def _enable(self):
        '''Enable Step Counter sensor.'''
        pass


    def _disable(self):
        '''Disable Step Counter sensor.'''
        pass


def instance():
    return macOSPedometer()
