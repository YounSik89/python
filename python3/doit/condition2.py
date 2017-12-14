a = 0
while a < 10:
    a = a+1
    if a%2 ==0: continue #조건 만족하면 밑에것 실행안하고 다시 맨처음으로 돌아감.
    print(a)

tlist = ['one','two','three']
for i in tlist:
    print(i)

a = [(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first + last)

sum = 0
for i in range(10):
    sum += i
print(sum)

sum = 0
for i in range(1,11):
    sum += i
print(sum)

marks = [10, 8, 7, 3, 4, 5, 1, 9, 6]
for num in range(len(marks)):
    if marks[num] < 7:
        continue
    print("%d번 학생 합격입니다."%num)

for i in range(2,10):
    for j in range(1,10):
        print(i*j,end =" ")
        #end=" " 하면 다음줄 안 넘어가고 " "를 붙인다. 2버전에서는 print i*j, 뒤에 콤마해줘야 이어서 출력한다.
    print('')


a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)

a = [1,2,3,4]
result = [num*3 for num in a]
print(result)

result2 = [num*3 for num in a if num%2 ==0]
print(result2)

gugu = [x*y for x in range(2,10) for y in range(1,10)]
print(gugu)