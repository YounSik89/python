#-*-coding: utf8 -*-
#py2 ver
x = "세상에는 %d 종류의 사람이 있어요" %10
binary = "'이진수'"
do_not = "모르는"
y = "%s를 아는 사람과 %s 사람." %(binary, do_not)
z = 'how fun is it!!!'
print x
print y
print z

print "'%s'라고 했어요" %x
print "'%s'이라고도 했죠" %y
print "So, %r" %z
# %r은 raw data(debug에 좋음), 보통 사용자에게는 %s 등 사용

h = False
j = "웃기는 농담 아니에요?! %r"
print j % h

w = "이 문자열의 왼쪽 ->"
e = "이 문자열의 오른쪽"
print w+e

print "." * 10

end1 = "a"
end2 = "b"
end3 = "c"
end4 = "d"
end5 = "e"
print end1 + end2,
print end3 + end4 + end5

