f = open("/home/ysroot/Python/python3/doit/test.txt","r") #쓰기모드일때 파일 없으면 새로 생성함, 파일이 존재하면 내용은 모두 사라진다.
line = f.readline()
print(line)
f.close()

f = open("/home/ysroot/Python/python3/doit/test.txt","r") #쓰기모드일때 파일 없으면 새로 생성함, 파일이 존재하면 내용은 모두 사라진다.
while True:
    line = f.readline()
    if not line: break #읽을 줄 없으면 readline에서 None리턴
    print(line)
f.close()

f = open("/home/ysroot/Python/python3/doit/test.txt","r") #쓰기모드일때 파일 없으면 새로 생성함, 파일이 존재하면 내용은 모두 사라진다.
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open("/home/ysroot/Python/python3/doit/test.txt","r") #쓰기모드일때 파일 없으면 새로 생성함, 파일이 존재하면 내용은 모두 사라진다.
data = f.read()
print(data)
f.close()

with open("/home/ysroot/Python/python3/doit/test.txt","r") as f:
    data = f.read()
    print(data)