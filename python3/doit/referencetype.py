import sys
print(sys.getrefcount(3))

a = 3
print(sys.getrefcount(3))
print(type(a))

b = 3
print(sys.getrefcount(3))
print(a is b)

c=3
print(sys.getrefcount(3))

a,b = ('python','life')
print(a,b)

(a,b) = 'apple','pie'
print(a,b)

a,b = 'banana','juice'
print(a,b)

[a,b] = ['1','2']
print(a,b)

[a,b] = 'hello', 'hi'
print(a,b)

a = b = "python"
print(a,b)

a = 3
b = 5
print(a,b)
a,b = b,a
print (a,b)

del(a)
del(b)
#del은 해도 되고 안해도 되고

a = [1,2,3]
b = a
a[1]= 4
print(a)
print(b) # b리스트의 1번 위치 값도 바뀌었다. => a와 b는 이름만 다를뿐이지 같은 리스트 가리켰기 때문에
print(b is a)

#그러면 값은 같지만 다른 리스트를 가리킬려면?
a = [1,2,3]
b = a[:] #a 리스트 전체를 복사하여 b에 대입
a[1] = 4
print(a)
print(b)
print(b is a)

#다른 방법 
from copy import copy
a = [4,5,6]
b = copy(a)
print(a)
print(b)
print(b is a)