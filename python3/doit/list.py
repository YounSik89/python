odd = [1,3,5,7,9]
char = ['a','b','c','d']
mix = [1,2,'a','b']
indup = [1,2,['a','b']]
print(odd)
print(char)
print(mix)
print(indup)

print(odd[0]+odd[3])
print(odd[-1])

a = [1,2,3,['a','b','c']]
print(a[-1])
print(a[3])
print(a[3][0])
print(a[-1][1])

triple = [1,2,3,['a','b',['game','over']],4,5]
print(triple[3][2][1])

print(a[0:2])
print(a[:2])
print(a[2:])
print(triple[1:5])
print(triple[3][:2])