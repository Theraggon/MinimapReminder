from playsound import playsound
import os
import random
import time
import argparse

path = '..\Sound'
interval = 5

parser = argparse.ArgumentParser()
parser.add_argument("-i","--interval", help="Set interval between sounds. Default=5",
                    type=int)
parser.add_argument("-d","--directory", help="Set path to directory with sounds")
args = parser.parse_args()
if args.interval:
    interval = args.interval
if args.directory:
    if os.path.isdir(args.directory):
        path = args.directory
    else:
        print("{0} is not a directory. Using default './Sound'".format(args.directory))

files = []

for r, d, f in os.walk(path):
    for file in f:
        if '.mp3' in file or '.wav' in file or '.aiff' in file:
            files.append(os.path.join(r, file))

while True:
    randomPath = files[random.randint(0,len(files)-1)]
    playsound(randomPath, False)
    time.sleep(interval)
