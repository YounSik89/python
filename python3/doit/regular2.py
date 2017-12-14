'''
[abc] -> apple/Yes, before/Yes, dude/No
[a-c] = [abc]
[0-5] = [012345]
[^] = not

\d -> number -> [0-9]
\D -> not number -> [^0-9]
\s -> white space -> [\t\n\r\f\v]
\S -> not white space -> [^\t\n\r\f\v]
\w -> alphanumeric -> [a-zA-Z0-9]
\W -> not alphanumeric -> [^a-zA-Z0-9]

.(dot) matches all characters except '\n'
ex)
a.b = a + "all characters" + b
=> aab/yes, a0b/yes, abc/no(because no (chracters between a and b))
ex2)
a[.]b = a + "." + b
=> a.b/yes, a0b/no

x* => x is more than 0 then Yes
ca*t -> ct/yes, cat/yes, caaaat/yes

x+ => x is more than 1 then yes
ca+t -> ct/no, cat/yes, caaat/yes

{x} -> iterator (absolutely x times required then Yes)
ex)
ca{2}t -> cat/no, caat/yes
ca{2,5}t -> cat/no, caat/yes, caaat/yes, caaaaat/yes, caaaaaat/no

x? => use 0 or 1 times then Yes
ab?c -> abc/yes, ac/yes
'''

#regular express need 're' module
import re
# match() -> 문자열 처음부터 끝까지 정규식과 매치되는지 조사
# search() -> 문자열 전체를 검색하여 정규식과 매치되는지 조사
# findall() -> 정규식과 매치되는 모든 문자열을 리스트로 리턴
# finditer() ->  정규식과 매치되는 모든 문자열을 반복가능한 객체로 리턴

#match
p1 = re.compile('[a-z]+')
print(p1.match("python")) #match
print(p1.match("3python")) #not match

#match example 
def getmatch(string):
    p = re.compile('[a-zA-Z]+')
    m = p.match(string)
    if m:
        print('Match found : ',m.group())
    else:
        print('No Match')
getmatch("python")
getmatch("34py")
getmatch("math123")

#search
print(p1.search('python'))
print(p1.search('4python'))

#