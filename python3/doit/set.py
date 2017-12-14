s1 = set([1,2,3])
print(s1)

s2 = set("hello")
print(s2) #집합은 중복허용X, 순서X(dictionary와 마찬가지 indexing불가)

s3 = set([1,2,3,4,5])
print(s3)

l3 = list(s3) #리스트로 변환
print(l3)
print(l3[1])

t3 = tuple(s3)
print(t3)
print(t3[1])

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1&s2) # 교집합
print(s1.intersection(s2))

print(s1|s2) #합집합
print(s1.union(s2))

print(s1-s2) #차집합
print(s1.difference(s2))
print(s2-s1)
print(s2.difference(s1))

s1 = set([1,2,3])
s1.add(4) #1개만 추가
print(s1)

s1 = set([1,2,3])
s1.update([4,5,6]) #여러개 추가
print(s1)

s1 = set([1,2,3])
s1.remove(2) #값 제거
print(s1)