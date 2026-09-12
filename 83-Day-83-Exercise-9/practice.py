

import win32com.client

speaker=win32com.client.Dispatch("SAPI.SpVoice")
speaker.Rate = 1      
speaker.Volume = 100
l=["Bob","Jake","Robin"]

for i in range(len(l)):
    m=f"Shout out to ",l[i]
    print(m)
    speaker.Speak(m)

