# r : read only , w : write, a : append (추가)

f = open("/home/ysroot/Python/python3/doit/test.txt","w") #쓰기모드일때 파일 없으면 새로 생성함, 파일이 존재하면 내용은 모두 사라진다.
for i in range(1,11):
    data = "%d 번째 줄입니다.\n"%i
    f.write(data)
f.close()
