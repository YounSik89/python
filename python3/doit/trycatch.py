#zero division
try:
    a = 4/0
    print(a)
except ZeroDivisionError as e:
    #e = exeption type -> need str() to convert
    print('error : '+str(e))


#other exam

f = open('./python3/doit/trytest.txt','w')
try:
    #do something
    f.write('startpoint\n')
finally:
    print('finally')
    f.write('endpoint')
    f.close()


try:
    f = open('foo.txt','r')
except FileNotFoundError as e:
    print('error : '+str(e))
else:
    data = f.read()
    f.close()

try:
    f = open("notfile",'r')
except FileNotFoundError:
    pass
