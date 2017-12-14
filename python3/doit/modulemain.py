import moduletest
from moduletest2 import safe_sum
#from moduletest2 import safe_sum, sum #import sum and safe_sum
#from moduletest2 import * #import all function
import moduletest3

#모듈을 불러올때 다른 디렉토리에 있으면
#import sys
#print(sys.path)
#dir = '' #모듈이 저장된 위치
#sys.path.append("dir")
#print(sys.path) #확인용
#
#이 방법 말고 다른 방법으로
#파이썬 콘솔에서 set PYTHONPATH=모듈이위치한주소
#도 가능하다.

print(moduletest.sum(4,5))

print(moduletest.safe_sum(1,'a'))

print(moduletest.safe_sum(1,4))

print(safe_sum(4,'b'))
print(safe_sum(1,7))

print(moduletest3.PI)