r = input("enterv the number:")
v = list(r)
print(v)
a = [int(i) for i in v]
print(a)
k = len(a)
power = [number ** k for number in a]



print(type(sum(power)))
if int(r) == sum(power):
    print("armstrong number")
else:
    print("not armstrong number")

