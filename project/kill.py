import os
import glob
    
removingjpg= glob.glob("*.jpg")
for f in removingjpg:
    os.remove(f)
removingtxt = glob.glob("*.txt")
for f in removingtxt:
    os.remove(f)