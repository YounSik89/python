# false => 숫자:0, 문자열:"", 리스트:[], 튜플:(), 딕셔너리:{}

money = 2000
card = 1
if money>=3000 or card:
    print("택시를 타고가라")
else:
    print("걸어가라")

x=3
y=2
print(x>y)
print(x<=y)
print(x==y)
print(x!=y)

print(1 in [1,2,3])
print(1 not in [1,2,3])
#리스트, 튜플, 문자열에서 in / not in 가능하다

pocket = ['paper','cellphone','money']
if 'money' in pocket:
    print("택시")
else:
    print("걷기")

pocket = ['paper','cellphone','money']
if 'money' in pocket:
    pass #아무런 일도 하지 않게 pass
else:
    print("카드")

pocket = ['paper','cellphone']
card = 0

if 'money' in pocket:
    print("택시")
else:
    if card:
        print("택시")
    else:
        print("걷기")


#elif 사용

if 'money' in pocket:
    print("택시")
elif card:
    print("택시")
else:
    print("걷기")

pocket = ['paper','money','cellphone']
if 'money' in pocket: pass
else: print("카드")


treehit = 0
while treehit < 10:
    treehit += 1
    print("%d번 나무 찍었습니다."%treehit)
    if treehit == 10:
        print("나무 넘어간다")



coffee = 10
while True:
    money = int(input("돈을 넣어주세요"))
    if money == 300:
        print("커피를 뽑습니다.")
        coffee -= 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 뽑습니다."%(money-300))
        coffee -= 1
    else:
        print("돈을 반환하고 커피를 뽑지 않습니다.")
        print("남은 커피 개수는 %d개 입니다."%coffee)
    if not coffee:
        print("커피가 다 떨어졌네요 판매를 중단합니다")
        break