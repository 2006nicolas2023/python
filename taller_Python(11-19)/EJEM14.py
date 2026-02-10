a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
e = float(input("e: "))
f = float(input("f: "))

den = a*e - b*d
x = (c*e - b*f) / den
y = (a*f - c*d) / den

print("X =", x)
print("Y =", y)

#a: 2
#b: 1
#c: 5
#d: 1
#e: 3
#f: 6
#X = 1.8
#Y = 1.4
