def sumall(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

result = sumall(3,4,5,6,7)
print(result)
result = sumall(1,2,3)
print(result)

def summul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    else:
        result = 0
    return result

result = summul('sum',1,2,3,4,5,6,7)
print(result)
result = summul('sum',1,2,3)
print(result)
result = summul('mul',1,2,3)
print(result)
result = summul('mul',1,2,3,4,5)
print(result)

def sumandmul(a,b):
    return a+b,a*b

result = sumandmul(3,4) #결과를 여러개 돌려줄수도 있다. => 튜플로 값이 묶인다.
print(result) 

num1, num2 = sumandmul(5,6) #따로 따로 받고 싶으면 이렇게 받으면 된다.
print(num1, num2)

def ret2summul(a,b):
    return a+b
    return a*b

result = ret2summul(3,4)
print(result) # a+b만 리턴된다. a*b는 실행되지 않는다.

