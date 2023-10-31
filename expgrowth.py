import math
P=float(input("Enter P: "))
r=float(input("Enter r: "))
t=float(input("Enter t: "))


result_c=P*math.e**r*t
print(result_c)

n=int(input("Enter n: "))
result_d=P*(1+(r/n))**n*t
print(result_d)

#the higher n is, the closer it gets to the result_d
#gets to result_c. In other words, result_d approaches
#result_c asymptotically as n approaches infinity.