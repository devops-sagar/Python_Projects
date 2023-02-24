import win32com.client
l = ['Raam', 'Krishna', 'Hanuman']
speaker = win32com.client.Dispatch("SAPI.SpVoice")
i = 0
while (i < 1):
    speaker.Speak(f"Jai Shree {l[0]}")
    speaker.Speak(f"Jai Shree {l[1]}")
    speaker.Speak(f"Jai Shree {l[2]}")
    i += 1