a = "Younsik is a student, he is a programmer"
print(a[3]) # 앞에서 4번째 문자
print(a[0]) # 가장 첫 문자 = 앞에서 첫번째 문자.
print(a[-1]) # 가장 마지막 문자 = 뒤에서 첫번째 문자
print(a[-2]) # 뒤에서 두번째 문자

b = a[0]+a[1]+a[2]+a[3]
print(b)
c = a[0:4] #맨 마지막 4는 안들어간다.
print(c)
d = a[7:14]
print(d)
e = a[10:]
print(e)
b = a[:15]
print(b)
print(a[:])

print(a[19:-7])

#문자열 요소는 바꿀수 있는 값이 아니다. ex) 문자열, 튜플 등은 immutable한 자료형이기 때문에

a = "pithon"
b = a[:1]+'y'+a[2:]
print(b)