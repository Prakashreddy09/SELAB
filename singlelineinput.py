from Tempfunction import *

with open('inputs.txt','r') as ifile:
    inputs = ifile.readline().strip()
a,b,c,t = inputs.split()
a = float(a)
b = float(b)
c = float(c)
t = float(t)

print(f"The Temperature at Time {t} is {Temperature(a,b,c,t)} C")
