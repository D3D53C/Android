import time
import RPi.GPIO as GPIO

class LED:


    #A-Z = 1-26
    #Ä = 27
    #Ü = 28
    #Ö = 29

    def Start(self):
        self.pin = 7

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)

    def Long(self):
        GPIO.output(self.pin, GPIO.LOW)
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(self.pin,GPIO.LOW)
        time.sleep(0.5)
    def Short(self):
        GPIO.output(self.pin, GPIO.LOW)
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(self.pin, GPIO.LOW)
        time.sleep(0.5)
    def Alphabet(self, Buchstabe):

        if(Buchstabe == 1):
            self.Short()
            self.Long()
            time.sleep(1)
        elif(Buchstabe == 2):
            self.Long()
            self.Short()
            self.Short()
            self.Short()
            time.sleep(1)
        elif(Buchstabe == 3):
            self.Long()
            self.Short()
            self.Long()
            time.sleep(1)
        elif(Buchstabe == 4):
            self. Long()
            self.Short()
            self.Short()
            time.sleep(1)
        elif(Buchstabe == 5):
            self.Short()
            time.sleep(1)
        elif(Buchstabe == 6):
            self. Short()
            self. Short()
            self. Long()
            self.self.Short()
            time.sleep(1)
        elif(Buchstabe == 7):
            self.Long()
            self.Long()
            time.sleep(1)
        elif(Buchstabe == 8):
            self. Short()
            self.Short()
            self.Short()
            self. Short()
            time.sleep(1)
        elif(Buchstabe == 9):
            self.Short()
            self. Short()
            time.sleep(1)
        elif(Buchstabe == 10):
            self. Short()
            self.Long()
            self.Long()
            self. Long()
            time.sleep(1)
        elif(Buchstabe == 11):
            self. Long()
            self.Short()
            self. Long()
            time.sleep(1)
        elif(Buchstabe == 12):
            self. Short()
            self. Long()
            self.  Short()
            self. Short()
            time.sleep(1)
        elif(Buchstabe == 13):
            self. Long()
            self. Long()
            time.sleep(1)
        elif(Buchstabe == 14):
            self. Long()
            self. Short()
            time.sleep(1)
        elif(Buchstabe == 15):
            self. Long()
            self.Long()
            self. Long()
            time.sleep(1)
        elif(Buchstabe == 16):
            self.Short()
            self.Long()
            self.  Long()
            self. Short()
            time.sleep(1)
        elif(Buchstabe == 17):
            self.Long()
            self. Long()
            self. Short()
            self.Long()
            time.sleep(1)
        elif(Buchstabe == 18):
            self.Short()
            self.Long ()
            self.Short()
            time.sleep(1)
        elif(Buchstabe == 19):
            self. Short()
            self.  Short()
            self.  Short()
            time.sleep(1)
        elif(Buchstabe == 20):
            self.   Long()
            time.sleep(1)
        elif(Buchstabe == 21):
            self.   Short()
            self.   Short()
            self.   Long()
            time.sleep(1)
        elif(Buchstabe == 22):
            self.  Short()
            self. Short()
            self.  Short()
            self. Long()
            time.sleep(1)
        elif(Buchstabe == 23):
            self. Short()
            self.   Long()
            self. Long()
            time.sleep(1)
        elif(Buchstabe == 24):
            self. Long()
            self.  Short()
            self. Short()
            self. Long()
            time.sleep(1)
        elif(Buchstabe == 25):
            self.  Long()
            self. Short()
            self.    Long()
            self.  Long()
            time.sleep(1)
        elif(Buchstabe == 26):
            self. Long()
            self. Long ()
            self. Short()
            self. Short()
            time.sleep(1)
        elif(Buchstabe == 27):
            self.  Short()
            self. Long()
            self.  Short()
            self.  Long()
            time.sleep(1)
        elif (Buchstabe == 28):
            self.   Short()
            self.   Short()
            self.    Long()
            self.   Long()
            time.sleep(1)
        elif (Buchstabe == 29):
            self.    Long()
            self.   Long()
            self.   Long()
            self.   Short()
            time.sleep(1)