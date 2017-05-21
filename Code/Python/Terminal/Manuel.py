import Basic.servo as Servo


# noinspection PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass
class ManuelC:
    def Kontrolle(self):
        x = 0
        Auswahlstring = "Manuele Kontrollle \n" \
                        "Daumen 1,Zeigefinger 2,Mittelfinger 3, Ringfinger 4, KFinger 5 \n" \
                        "Handgelenk 6, EllenbogenH 7, EllenbogenV 8"
        while (x <= 1):
            Auswahl = int(input(Auswahlstring))
            if Auswahl == 1:
                Degree = int(input("Degree ?\n"))
                self.Daumen(Degree)
            elif Auswahl == 2:
                Degree = int(input("Degree ?\n"))
                self.Zeigefinger(Degree)
            elif Auswahl == 3:
                Degree = int(input("Degree ?\n"))
                self.Mittelfinger(Degree)
            elif Auswahl == 4:
                Degree = int(input("Degree ?\n"))
                self.Ringfinger(Degree)
            elif Auswahl == 5:
                Degree = int(input("Degree ?\n"))
                self.KleinerFinger(Degree)
            elif Auswahl == 6:
                Degree = int(input("Degree ?\n"))
                self.Handgelenk(Degree)
            elif Auswahl == 7:
                Degree = int(input("Degree ?\n"))
                self.EllenbogenH(Degree)
            elif Auswahl == 8:
                Degree = int(input("Degree ?\n"))
                self.EllenbogenV(Degree)

    # noinspection PyCallByClass
    def KleinerFinger(self, Degree):
        # noinspection PyCallByClass
        Finger = Servo.Servo.__init__(self, 37, 50)
        Finger.change_position(Degree)

    # noinspection PyCallByClass
    def Ringfinger(self, Degree):
        # noinspection PyCallByClass
        Finger = Servo.Servo.__init__(self, 35, 50)
        Finger.change_position(Degree)

    # noinspection PyCallByClass
    def Mittelfinger(self, Degree):
        # noinspection PyCallByClass
        Finger = Servo.Servo.__init__(self, 33, 50)
        Finger.change_position(Degree)

    # noinspection PyCallByClass
    def Zeigefinger(self, Degree):
        # noinspection PyCallByClass
        Finger = Servo.Servo.__init__(self, 31, 50)
        Finger.change_position(Degree)

    # noinspection PyCallByClass
    def Daumen(self, Degree):
        # noinspection PyCallByClass
        Finger = Servo.Servo.__init__(self, 29, 50)
        Finger.change_position(Degree)

    # noinspection PyCallByClass
    def EllenbogenH(self, Degree):
        # noinspection PyCallByClass
        Finger = Servo.Servo.__init__(self, 36, 50)
        Finger.change_position(Degree)

    # noinspection PyCallByClass
    def EllenbogenV(self, Degree):
        # noinspection PyCallByClass
        Finger = Servo.Servo.__init__(self, 38, 50)
        Finger.change_position(Degree)

    # noinspection PyCallByClass
    def Handgelenk(self, Degree):
        # noinspection PyCallByClass
        Finger = Servo.Servo.__init__(self, 40, 50)
        Finger.change_position(Degree)
