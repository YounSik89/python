a = 123
b = -178
c = 0
print(a,b,c)

a = 1.2
b = -3.45
c = 4.24e10
d = 4.24e-10 #4.24*10^-10
print(a,b,c,d)

a = 0o177
b = 0x8ff
print(a,b)

a = 1+2j
b = 3-4j
print(a,b)
print(a.real)
print(a.imag)
print(a.conjugate())
print(abs(a)) #1+2j의 절대값 : 루트5

#python2에서는 3/4 할 경우 값이 0이 리턴됨. 정수로만 결과가 리턴되기 때문
# 3/4 = 0.75 얻고 싶으면 3/(4*1.0) 처럼 분모를 강제로 실수형 변환해야함.

a=3
b=4
c = a**b #제곱계산
print(c)

d = a%b
print(d) 

a = 7
b = 4
c = a/b
d = a//b
print(c,d)