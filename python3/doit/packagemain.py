#방법1
#import testpackage.exam1.exam1 as echo
#echo.echo_test()

#방법2
#from testpackage.exam1 import exam1 as echo1
#echo1.echo_test()

#방법3
#from testpackage.exam1.exam1 import echo_test
#echo_test()

#패키지 임포트는 __init__.py에 정의된 것만 참조가능 
#__init__.py 없으면 오류 발생한다.   
#python 3.3 이후로는 없어도 괜찮으나 하위버전 호환위해 생성하는게 좋다
#하위버전은 오류발생
import testpackage.exam3.exam3 as show
show.show_test()
#이것도 하위버전은 오류발생
from testpackage.exam1 import *

#exam2a에서 exam1의 echo_test()를 relative 한다.
from testpackage.exam2.exam2a import shape_test
shape_test()

#상대경로 이용한 relative 패키지
from testpackage.exam1.exam1a import listen_test
listen_test()