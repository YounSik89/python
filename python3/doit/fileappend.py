f = open("/home/ysroot/Python/python3/doit/test.txt","a") #쓰기모드일때 파일 없으면 새로 생성함, 파일이 존재하면 내용은 모두 사라진다.
for i in range(11,20):
    data = "%d 번째 줄입니다.\n"%i
    f.write(data)
f.close()

f = open("/home/ysroot/Python/python3/doit/test.txt","r") #쓰기모드일때 파일 없으면 새로 생성함, 파일이 존재하면 내용은 모두 사라진다.
data = f.read()
print(data)
f.close()