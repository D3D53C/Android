from Basic.servo import Servo as Servo
import time
import sys


# noinspection PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass
class ActrionC:
    # noinspection PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass
    def Action1(self):  # Finger einzelnd ein und Ausklappen
        # noinspection PyCallByClass
        F2S = Servo.__init__(self,29,50)
        # noinspection PyCallByClass
        F3S = Servo.__init__(self,31,50)
        # noinspection PyCallByClass
        F4S = Servo.__init__(self,33,50)
        # noinspection PyCallByClass
        F5S = Servo.__init__(self,35,50)

        F2S.change_position(0)
        time.sleep(2)
        F2S.change_position(180)
        time.sleep(0.5)
        F3S.change_position(0)
        time.sleep(2)
        F3S.change_position(180)
        time.sleep(0.5)
        F4S.change_position(0)
        time.sleep(2)
        F4S.change_position(180)
        time.sleep(0.5)
        F5S.change_position(0)
        time.sleep(0.5)
        F5S.change_position(180)

    # noinspection PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass
    def Action2(self): #Bewegt Ellenbogen hoch, dreht Handgelenk, Schlißt und öffnet alle Finger


        F2S = Servo.__init__(self, 29, 50)
        # noinspection PyCallByClass
        F3S = Servo.__init__(self, 31, 50)
        # noinspection PyCallByClass
        F4S = Servo.__init__(self, 33, 50)
        # noinspection PyCallByClass
        F5S = Servo.__init__(self, 35, 50)

    # noinspection PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass
    def Action3(self): #


        F2S = Servo.__init__(self, 29, 50)
        # noinspection PyCallByClass
        F3S = Servo.__init__(self, 31, 50)
        # noinspection PyCallByClass
        F4S = Servo.__init__(self, 33, 50)
        # noinspection PyCallByClass
        F5S = Servo.__init__(self, 35, 50)