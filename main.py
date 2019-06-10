from playsound import playsound
import os
import random
import time

path = '.\Sound'
interval = 5

files = []

for r, d, f in os.walk(path):
    for file in f:
        if '.mp3' or '.wav' or '.aiff' in file:
            files.append(os.path.join(r, file))

while True:
    randomPath = files[random.randint(0,len(files)-1)]
    playsound(randomPath, False)
    time.sleep(interval)
