import math
v0=float(input("Enter v0: "))
h=float(input("Enter h: "))
a=float(input("Enter alpha: "))
g=9.81
a=math.radians(a)
t=(v0*math.sin(a)+math.sqrt((v0*math.sin(a)*2)+2*g*h))
d=(v0*math.cos(a)*t)
print(t,d)