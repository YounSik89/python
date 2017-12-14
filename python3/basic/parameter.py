def add(a=0, b=0, c=0):
    return a+b+c

print(add())
print(add(11))
print(add(11,22))
print(add(11,22,33))

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
	    print("-- This parrot wouldn't", action)
	    print("if you put", voltage, "volts through it.")
	    print("-- Lovely plumage, the", type)
	    print("-- It's", state, "!")

print(parrot(1000))
print(parrot(voltage=1000))
print(parrot(voltage=1000000, action='VOOOOOM'))
print(parrot(action='VOOOOOM', voltage=1000000))
print(parrot('a million', 'bereft of life', 'jump'))
print(parrot('a thousand', state='pushing up the daisies'))

#parrot()                     # 일반 인자값 없음
#parrot(voltage=5.0, 'dead')  #키워드 인자 뒤에 일반 인자값을 주지 못함
#parrot(110, voltage=220)     # 한 인자에 두 값을 주지 못함
#parrot(actor='John Cleese')  # actor라는 키워드가 없음

#만약 함수 정의부에 **kwargs 와 같은 형태의 인자가 있다면 
# kwargs는 딕셔너리 형태로 키워드 인자들 중에서 일반 인자가 아닌 것들을 넘겨 받는다. 
# 만약 가변 개수 인자 *args 와 혼용하는 경우에는 반드시 이것 뒤에 와야 한다.
def f(a, *args, **kwargs):
    print('a=',a)
    print('args=',args)
    print('kwargs=',kwargs)

print(f(11))
print(f(11,22,33))
print(f(11,22,33,b=44,c=55))

def printName(firstName, secondName='Choi'):
    print('My name is '+ firstName +' ' + secondName +'.')

print(printName('Youn-sik'))
print(printName('Youn-Sik','Park'))

#기본값 인자는 값을 생략해서 호출할 수 있지만 일반 인자는 반드시 값을 지정해 주어야 한다. 
# 따라서 printName()함수를 호출할 때 첫 문자열은 반드시 정해서 넘겨주어야 한다. 
# 여기에서 printName()함수의 두 번째 인자를 입력하지 않으면 기본적으로 ‘Kim’으로 지정된다. 
# 두 번째 인자를 명시적으로 지정하면 그것이 secondName 으로 지정된다.
#한 가지 주의할 점은 일반 인자와 기본값 인자가 같이 올 때에는 반드시 기본값 인자는 뒤에 와야 한다는 점이다. 즉, 아래와 같이 정의하면 오류가 발생한다.
#def printName(firstName='Kim', secondName):

def add(a, b=0, c=0):
    return a+b+c
print(add(1))
print(add(1,2)) #b=2
print(add(1,2,3)) #b=2, c=3
#기본값 인자가 두 개 이상일 때에도 일반인자 뒤로 온다.
#또한 호출할때 입력 순서대로 기본값인자에 값이 할당된다.

def func(a, L=[]):
    L.append(a)
    return L
print(func(1))
print(func(2))
print(func(3))
#주의할 점은 기본 인자는 최초의 호출 시에만 지정된 값으로 초기화 되고 
# 이후의 호출에서는 그렇지 않다는 점이다. 
# 따라서 리스트나 딕셔너리와 같은 가변(muatble) 객체를 기본 인자로 사용할 때 문제가 된다.
# 기본 인자 L은 최초의 호출에서만 빈 리스트로 초기화 되고 그 이후의 호출에서는 그 내용물은 유지된다. 
# 따라서 리스트의 요소가 축적되는 것이다. (마치 C/C++에서의 static 변수와 비슷한 동작을 수행한다.)

def func1(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(func1(1))
print(func1(2))
print(func1(3))
# 이러면 후속호출이 매번 초기화 된다.
