#튜플은 값이 변하지 않는다.

t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a','b',('ab','cd'))

t1 = (1,2,'a','b')
#del t1[1] 튜플 값 지우려면 에러발생
#t1[1] = 'c' 튜플 값 변경하려해도 에러 발생
print(t1[0])
print(t1[3])
print(t1[1:])
t2 = (3,4)
print (t1+ t2)
print(t2*3)