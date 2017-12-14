a = [1,2,3]
b = [4,5,6]
print(a+b)

print(a*3)

#print(a[2]+"hi") <= type error a[2]=int
print(str(a[2])+"hi")

a = [1,2,3]
print(a)
a[2]=4
print(a)

print(a[1:2])
a[1:2] = ['a','b','c']
print(a) #a[1:2]사이의 리스트를 [a,b,c]로 바꾼다.
#result [1, 'a', 'b', 'c', 4]

b = [1,2,4]
b[1] = ['a','b','c']
print(b) #위의 것과 다른 결과. b[1] 원소를 리스트로 치환한다.
#result [1, ['a', 'b', 'c'], 4]

print(a)
a[1:3] = [] #리스트 요소 삭제.
print(a)
del a[1] #함수 이용 리스트 요소 삭제
print(a)

a = [1,2,3,4,5]
del a[2:4] #del 함수로 범위 삭제도 가능.
print(a)

a = [1,2,3]
a.append(4)
a.append([5,6]) #리스트 추가
print(a)

a = [1,4,5,2,3]
a.sort()
print(a)

a = ['c','a','e','d','b']
a.sort()
print(a)

a.reverse()
print(a)

a=[1,2,3]
print(a.index(3))
print(a.index(1))
#print(a.index(0)) <= error발생, 0이 리스트에 없어서

a.insert(0,4) #0번째 위치에 4대입
print(a)

a.insert(3,5)
print(a)

a = [1,2,3,1,2,3]
a.remove(3) # 처음 나오는 3 삭제
print(a)
a.remove(3)
print(a)

a = [1,2,3]
print(a.pop()) #맨 마지막 꺼낸다.
print(a) # pop 한것은 삭제된다

a = [1,2,3]
print(a.pop(1)) #1번 위치에 있는 자료 꺼낸다
print(a)

a = [1,2,3,4,1]
print(a.count(1)) #리스트 내에 몇개 있는지 알려준다.

a = [1,2,3]
a.extend([4,5]) #리스트에 4,5 넣는다.
print(a)
b = [6,7,8]
a.extend(b)
print(a)