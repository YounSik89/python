class CoupleNam:
    lastname = "김"
    def __init__(self,name):
        self.fullName = self.lastname + name
    
    def travel(self, where):
        print("%s, %s 여행을 가다"%(self.fullName, where))
    
    def love(self, who):
        print("%s, %s와 사랑에 빠지다."%(self.fullName, who.fullName))

    def fight(self, who):
        print("%s, %s와 사랑 싸움을 했다."%(self.fullName, who.fullName))

    def __add__(self, who):
        #연산자 오버로딩
        print("%s, %s와 결혼을 하다."%(self.fullName, who.fullName))

    def __sub__(self, who):
        print("%s, %s와 이혼을 하다."%(self.fullName, who.fullName))

class CoupleNyeo(CoupleNam):
    #클래스 상속
    lastname = "이"
    def travel(self, where, when):
        #메소드 오버라이딩
        print("%s, %s 여행을 %d일 동안 가다."%(self.fullName, where, when))

nam = CoupleNam("철수")
nyeo = CoupleNyeo("영희")
nam.travel("도쿄")
nyeo.travel("도쿄",4)
nam.love(nyeo)
nyeo.love(nam)
nam+nyeo
nam.fight(nyeo)
nam - nyeo