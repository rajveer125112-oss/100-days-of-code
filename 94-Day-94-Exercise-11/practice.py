import time
import win32com.client
decision=input("Enter the water reminder interval (hour/minutes) =")
class Hour:
   
    def __init__(self):
        self.n=float(input("Enter the water reminder interval in hours = "))
    def Reminder(self,speaker=win32com.client.Dispatch("SAPI.SpVoice")):
        
        speaker.Rate=1
        speaker.Volume=100
        while True:
            time.sleep(3600*self.n)
            speaker.Speak("Drink Water")

class Minutes:
   
    def __init__(self):
        self.n=float(input("Enter the water reminder interval in Minutes = "))
    def Reminder(self,speaker=win32com.client.Dispatch("SAPI.SpVoice")):
        
        speaker.Rate=1
        speaker.Volume=100
        while True:
            time.sleep(60*self.n)
            speaker.Speak("Drink Water")

if decision=="hour":
    h=Hour()
    h.Reminder()
elif decision=="minutes":
    m=Minutes()
    m.Reminder()

#Exe file in dist folder if you will run it reminder will turn on from the time you turned on the exe file and will close when you will close.

    
