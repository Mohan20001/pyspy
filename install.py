import os

try:
    os.system("pip install pyngrok")
except:
    os.system("pip3 install pyngrok")

f = open('requirments.txt', 'r')
l = f.readlines()
for item in l:
    if item != "":
        os.system("npm install " + item)