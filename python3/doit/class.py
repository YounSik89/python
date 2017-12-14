class Calc:
    def __init__(self):
        self.result = 0
    #생성자, 인스턴스 만들 때 항상 실행 된다.
    def adder(self,num):
        self.result += num
        return self.result
    #self는 생성된 인스턴스를 가리킨다.

cal1 = Calc()
cal2 = Calc()
#cal1, cal2는 객체
#cal1, cal2는 Calc의 인스턴스
#객체와 인스턴스는 같은 표현이지만 위의 표현대로 쓰는 것이 잘 어울린다.

print(cal1.adder(3))
print(cal1.adder(4))

class Simple:
    pass
# Simple클래스는 아무런 기능도 갖고있지 않은 껍질뿐인 클래스, 하지만 인스턴스 생성은 가능하다.
