#-*-coding: utf8 -*-
#class 생성

class test1:
    def __init__(self):
        self.numA=1
        self.numB=2

testA = test1()

print(testA.numA)
print(testA.numB)
print(vars(testA))

class test2:
    def __init__(self,name):
        self.numA=1
        self.numB=2
        self.name=name

#test2 -> name 입력 없으면 에러
#testB = test2()
testB = test2('hello')
print(testB.numA)
print(testB.numB)
print(testB.name)
print(vars(testB))

class test3:
    def __init__(self, name='tester'):
        self.numA=1
        self.numB=2
        self.name=name

testC = test3()
print(testC.numA)
print(testC.numB)
print(testC.name)
print(vars(testC))