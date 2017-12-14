#-*-coding: utf8 -*-
#람다함수

getSum = lambda a, b : a+b
result = getSum(1,2)
print(result)

def getAdd(a,b):
    return a+b
result2 = getAdd(1,2)
print(result2)

def getPos(x):
    return x>0
result3 = list(filter(getPos,range(-5,6)))
print(result3)

result4 = list(filter(lambda x: x>0, range(-5,6)))
print(result4)