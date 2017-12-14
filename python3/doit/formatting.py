print("i eat %d apples"%3)
print("i eat %s apples"%"five")
number = 3
print("i eat %d apples"%number)
number = 5
day = "ten"
print("i ate %d apples before %s days"%(number,day))

# %s : 문자열 %c : 문자1개 %d : 정수  %f : 부동소수  %o : 8진수  %x : 16진수   %% : %문자
# %s는 어떠한 값도 문자열로 바꿀수 있다.

print("i eat %s apples"%3)
print("i eat %s apples"%4.196)

print("rain is comming %d %%"%98)

print("%10s"%"hi") # 전체 길이 10개 문자열 공간에서 hi를 오른쪽으로 정렬하고 나머지는 공백
print("%-10s"%"hello") #전체 길이 10개 문자열 공간에서 hello를 왼쪽 정렬하고 나머지는 공백

print("%0.4f"%3.123456) #소수 4자리까지만
print("%10.4f"%3.42134234) #소수 4자리가지 표시하고 전체길이 10개인 문자열 공간에서 오른쪽 정렬

a = "airplane"
print(a.count('a')) #문자 개수 세기
print(a.find('p')) #문자 위치 찾기
print(a.find('k')) #문자 없으면 -1
print(a.index('n'))
#print(a.index('k')) # k없어서 오류발생 => index는 없는 문자 찾으면 오류난다.

a = ","
b = a.join('abcde') #문자 사이사이마다 , 대입
print(b)

a = "hi"
b = a.upper() 
print(b)

a = "HI"
b = a.lower()
print(b)

a = "    hi  "
b = a.lstrip()
print(b)

a = "  hi         "
b = a.rstrip()
print(b)

a = "    hi      "
b = a.strip()
print(b)

a = "banana is delicious"
print(a)
b = a.replace("banana","strawberry")
print(b)

print(a.split())
c = "a:b:c:d"
print(c.split(":"))

print("i eat {0} apples".format(3))
print("i eat {0} apples".format("five"))
number = 3
print("i eat {0} apples".format(number))
day = "ten"
print("i eat {0} apples, {1} days ago".format(number,day))

print("i eat {number} apples, {day} days ago".format(number=10,day=3))

print("i eat {0} apples, {day} days ago".format(10,day=5))

print("{0:<10}".format("hi")) # 치환되는 문자열 왼쪽 정렬, 문자열 총 크기 = 10
print("{0:>10}".format("hi")) # 치환되는 문자열 오른쪽 정렬, 문자열 총 크기 = 10
print("{0:^10}".format("hi")) # 치환되는 문자열 가운데 정렬, 문자열 총 크기 = 10

print("{0:=^10}".format("hi")) # 공백을 지정한 문자(=)로 채운다. 가운데 정렬, 총크기 = 10
print("{0:!<10}".format("hi")) # 공백을 !로 채운다.왼쪽정렬, 총크기 = 10

y = 3.41277412498721304120
print("{0:0.4f}".format(y)) # 소수 4자리까지 표현
print("{0:10.4f}".format(y)) # 소수 4자리까지 표현, 문자열공간 10개

#format 쓸때 중괄호{} 쓰려면
print("{{this is mid gwalho}}".format())




