import os

path = '.\Sound'
interval = 5

files = []

for r, d, f in os.walk(path):
    for file in f:
        if '.mp3' or '.wav' or '.aiff' in file:
            files.append(os.path.join(r, file))
