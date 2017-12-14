def sum(a,b):
    return a+b

def safe_sum(a,b):
    if type(a) != type(b):
        print("타입이 서로 다릅니다")
        return
    else:
        result = sum(a,b)
        return result