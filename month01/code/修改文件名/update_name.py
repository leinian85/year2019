import os
import re

names = ("update_name.py",)

def UpdateFileName(file,prefix):
    # regex = re.compile(prefix)
    for sigin_file in os.listdir(file):
        print(sigin_file)
        if os.path.isfile(file+"/"+sigin_file) and sigin_file not in names:
            # print(regex.findall(sigin_file))
            name = prefix+sigin_file
            # print(file+"/"+sigin_file)
            # print(file+"/"+name)
            os.rename(file+"/"+sigin_file,file+"/"+name)

for i in range(1,15):
    flg = "0"+str(i) if i < 10 else str(i)
    UpdateFileName("day"+flg,"d"+flg+"_")