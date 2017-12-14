class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

#eagle은 bird 클래스를 상속받음
#eagle = Eagle()
#eagle에서 fly함수 구현 안해서 error발생
#eagle.fly()

class Hawk(Bird):
    def fly(self):
        print('very fast')

hawk = Hawk()
hawk.fly()