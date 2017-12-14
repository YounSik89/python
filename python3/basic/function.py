
#함수

def nop(): pass # 함수 본체 작성 안하고 껍데기만 작성 / 호출은 할 수 있으나 아무것도 수행 X

def sayHI():
    print('hi')

def sayHello():
    print('hello')

def gugudan(n):
    for x in range(1,10):
        print('%d x %d = %d'%(n,x,n*x))

gugudan(3)

funclist = [sayHI, sayHello,gugudan]
funclist[0]()
funclist[1]()
funclist[2](5)

copygugu = gugudan
copygugu(9)