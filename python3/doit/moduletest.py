def sum(a,b):
    return a+b

def safe_sum(a,b):
    if type(a) != type(b):
        print("타입이 서로 다릅니다")
        return
    else:
        result = sum(a,b)
        return result

    #그냥 이런식으로 실행하면 import하는 곳에서 바로 실행된다.
    #따라서 main일 경우에만 실행하게 하는 방법을 사용해서
    #모듈을 다른곳에서 사용할 때에는 print문이 실행 안되게 한다.
if __name__ == "__main__":
    print(safe_sum(1,4))
    print(safe_sum(5,'c'))
    print(sum(1,5))
