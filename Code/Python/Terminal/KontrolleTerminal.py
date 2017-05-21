
from Terminal.Action import ActrionC as Action
from Terminal.Manuel import ManuelC as Manuel
from Basic.LED import LED as LED


# noinspection PyCallByClass
class StartC:
    # noinspection PyCallByClass
    def Starten(self):
        Auswahlstring = "Ihnen stehen Action1 (Finger auf und zu)\n" \
                        "Action2 (Bewegt Elenbogen hoch HAndgelenk nach vorne und alle Finger auf und zu)\n" \
                        "Action3 ()\n"\
                        "Manuel  (Laesst sie die Gelenke einzeld bewegen)\n"\
                        "Die Zahl in der Eckigen Klammer ist für die Eingabe\n\n"
        while(True):
            Auswahl = input(Auswahlstring)

            if(Auswahl == 1):
                Action.Action1()
                break
            elif(Auswahl == 2):
                Action.Action2()
                break
            elif (Auswahl == 3):
                Action.Action3()
                break
            elif (Auswahl == 4):
                Manuel.Kontrolle()
            elif (Auswahl == 5):
                x=0
                while(x<=1):
                    Buchstabe = int(input("Bitte einen Buchtaben auswählen 1-26 = A-Z Ä=27 Ü=28 Ö=29"))
                    # noinspection PyCallByClass
                    LED.LED.Alphabet(Buchstabe)
                    Ende = int(input("Noch ein Buchstabe ? [Y=1/N=0]"))
                    if(Ende == 1):
                        break
                    elif(Ende == 0):
                        x = 1
                    else:
                        print("Error")
            else:
                print("Error")
