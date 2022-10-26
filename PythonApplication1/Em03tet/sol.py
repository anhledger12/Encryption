import random
f = open('flag','r')
u = f.read()
k = random.randint(57, 75)
out = ""
for uu in u:
    out = out + str(ord(uu)^k)+" "
g = open("output","a")
g.write(out)