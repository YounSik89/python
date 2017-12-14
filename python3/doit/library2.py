def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)

#map
def two_times_map(x):return x*2
ret = list(map(two_times_map,[1,2,3,4]))
print(ret)

#lambda
ret2 = list(map(lambda a:a*2,[1,2,3,4]))
print(ret2)

def plus_one(x):
    return x+1
print(list(map(plus_one,[1,2,3,4,5])))

#max/min
max([1,2,3]) #return 3
max('python') #return y
min([1,2,3]) # return 1
min('python') #return h


#range
print(list(range(5)))
print(list(range(5,10)))
print(list(range(1,10,2))) 

#sorted
print(sorted([3,1,2]))
print(sorted(['c','b','c']))
print(sorted('zero'))
print(sorted((3,2,1)))

#list-sort
a=[3,1,2]
result = a.sort() #list methond - sort() has no return
print(result) #return None
print(a)

#random
import random
random.random()
random.randint(1,10)