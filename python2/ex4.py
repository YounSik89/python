#-*-coding: utf8 -*-
#py2 ver
formatter = "%s %s %s %s"

print formatter %(1,2,3,4)
print formatter %("a","b","c","d")
print formatter %(True, False, False, True)
print formatter %(formatter, formatter, formatter, formatter)
print formatter %(
    "abcde",
    "fghij",
    "klmno",
    "pqrst"
    )

formatter2 = "%r %r %r %r"
# %r은 표현형 - 디버그 정보를 얻기 위해서만 쓴다. 한글은 간혹 인식 불가능 %s로 확인한다.
print formatter2 %(
    "abcde",
    "fghij",
    "klmno",
    "pqrst"
    )

days = "월 화 수 목 금 토 일"
months = "1월\n2월\n3월\n4월\n5월\n6월\n7월\n8월\n9월\n10월\n11월\n12월"
print "요일 목록: ", days
print "월 목록: \n", months

print """
여기 세개의 따옴표
원하는것 아무렇게나
몇줄이던 상관없이
마음대로 쓸수있다
"""

print "%r" %months
# %r에서는 줄이 바뀌지 않는다. 한글은 깨진다.
