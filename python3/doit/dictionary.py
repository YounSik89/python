dic = {'name':'pey','phone':'01012341234','birth':'1108'}
a = {1:'hi'}
b = {'a':[1,2,3]}
print(dic)
print(a)
print(b)
print(dic['name'])
print(a[1])
print(b['a'])

a[2] = 'b' #a 딕셔너리에 2:'b'추가
print(a)
a['name'] = 'pey'
a[3] = [1,2,3]
print(a)
del a[1]
print(a)

grade = {'pey':10,'july':99}
print(grade['pey'])
print(grade['july'])

a = {1:'a',2:'b'}
print(a[1])
print(a[2])

#키는 고유값, 중복되면 나머지 무시됨. 어떤 것이 무시될지는 알수없다.
a = {1:'a',1:'b'}
print(a)

#튜플은 키로 쓸수 있다.하지만 리스트는 안된다. => 키는 변할수 없어야하기때문에, value는 상관 없다.
#a = {[1,2]:'a'} <= 에러발생
a = {(1,2):'a'}

a = {'name':'pey','phone':'01012341234','birth':'1108'}
print(a.keys()) #키만 보여주기
# 2버전에서는 keys()의 리턴값이 리스트 였지만 메모리낭비 줄이기 위해 3버전에서는 dict_keys라는 객체 리턴함.
# dict_values, dict_items 역시 3에서 추가된 부분
# 리턴값으로 리스트 필요하면 list(a.keys())를 활용하여 쓴다.
# dict_keys, dict_values, dict_items는 리스트로 변환안해도 iterator(ex:for문)사용가능하다.

for i in a.keys():
    print(i)

print(list(a.keys()))

print(a.values())
print(a.items())
a.clear()
print(a) #빈 딕셔너리 {}로 표시됨.

a = {'name':'pey','phone':'01012341234','birth':'1108'}
print(a.get('name'))
print(a.get('nokey')) #해당 키 없으면 None
# print(a['nokey']) <= error발생

print(a.get('foo','bar')) #foo라는 키 값이 없어서 기본값인 'bar'리턴함.

print('name' in a) #키값 존재 확인
print('email' in a)