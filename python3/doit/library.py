#절대값
abs(3)
abs(-3)

#power
pow(2,4) #reutrn 2^4 = 16

#반복자료 판별
all([1,2,3]) #true (because all are true)
all([1,2,3,0]) #false (because has 0)

any([1,2,3,0]) # true (because has true more than one)
any([0,""]) #false (because all has false)

#string
chr(97) # ascii -> char
ord('a') #chr -> ascii
str(3) #return string type
str('hi')
str('hi'.upper()) #retrun upper string
str('HI'.lower)


#get object method(function)
dir([1,2,3])
dir({'1':'a'})

#divmod(input intA,intB)->return tuple(div,mod)
divmod(7,3)

#enumerate -> print index and value
for i, name in enumerate(['body','foo','bar']):
    print(i,name)

#eval -> input(string) return result / usually use in dynamic func&class
eval('1+2')
eval("'hi'+'a'")
eval('divmod(4,3)')

#filter
def positive(numberList):
    result = []
    for num in numberList:
        if num > 0:
            result.append(num)
    return result

print(positive([-1,-2,3,4,0,-5,6]))

#lambda
print(list(filter(lambda x:x>0,[-1,-2,3,4,0,-5,6])))

sumfunc = lambda a,b:a+b
sumfunc(1,2)
# same as
'''
def sumfunc(a,b):
    return a+b
'''
myList = [lambda a,b:a+b, lambda a,b:a*b]
print(myList)
print(myList[0])
print(myList[0](3,4)) # get 7
print(myList[1](3,4)) # get 12

#hex - 16 (int to hex)
hex(234)
hex(3)

#oct -8 (int to oct)
oct(34)
oct(12345)


#id -> get reference addr
a = 3
id(3)
id(a)
b=a
id(b)

#int
int('3')
int(3.14)
int('11',2) #get 10jinsu -> 11(binary) = 1*2 + 1*1 = 3
int('1A',16) #get 10jinsu -> 1A(hex) = 1*16 + A(10)*1 = 26

#isinstance
class Person:pass #empty class 
saram = Person()
isinstance(saram,Person) # if saram is instance of Person then return true
number = 3
isinstance(number,Person) # number is not instance of Person then retrun false

#len
len('python') # return 6
len([1,2,3]) # return 3
len([1,'a']) # return 2

#list
#make list 
py = list("python")
print(py)
num = list((1,2,3))
print(num)
#return list
a=[1,2,3]
b=list(a)
print(b)

#make tuple
ta = tuple('abc')
print(ta)
tb = tuple([1,2,3])
print(tb)
tc = tuple((1,2,3))
print(tc)

#get type
print(type('abc'))
print(type([]))
print(type(open("test","w")))

#zip
za = list(zip([1,2,3],[4,5,6]))
print(za)
zb = list(zip([1,2,3],[4,5,6],[7,8,9]))
print(zb)
zc = list(zip('abc','def'))
print(zc)