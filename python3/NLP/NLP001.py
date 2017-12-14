import unicodedata
import math

class NLP:
    def __init__(self):
        self.beforeTXT=''
        self.cntBeforeTXT=0
        self.cho = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
        self.jung = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
        self.jong = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
    
    def getLength(self):
        self.cntBeforeTXT = len(self.beforeTXT)
        return self.cntBeforeTXT
    
    def getOneWord(self,L=None):
        if L is None:
            L = []
        length = self.cntBeforeTXT
        print('***** 음절별 분석 *****')
        for i in range(0,length):
            word = self.beforeTXT[i]
            print(word+' / '\
                +unicodedata.name(word)+' / '\
                +unicodedata.category(word) + ' / '\
                +str(ord(word)) + ' / '+str(word.encode('UTF-8'))
            )
            #print(self.getParseUnicode(word))
            L.append(self.getParseUnicode(word))
        return L

    def getParseUnicode(self, char, L=None):
        if L is None:
            L=[]
        uniNum = ord(char)-44032
        ret = ""
        chosung = str(self.cho[int(math.floor(uniNum/(21*28)))])
        #Uarray.append(chosung)
        if(len(chosung)!=0):
            ret += chosung
            ret += str(ord(chosung))
            L.append(chosung)
            L.append(str(ord(chosung)))
        jungsung = str(self.jung[int(math.floor((uniNum/28)%21))])
        #Uarray.append(jungsung)
        if(len(jungsung)!=0):
            ret += jungsung
            ret += str(ord(jungsung))
            L.append(jungsung)
            L.append(str(ord(jungsung)))
        jongsung = str(self.jong[uniNum%28])
        if(len(jongsung)!=0):
            ret += jongsung
            ret += str(ord(jongsung))
            L.append(jongsung)
            L.append(str(ord(jongsung))) 
        #Uarray.append(jongsung)
        #print(ret)
        return L
        
    def makeParseTree(self):
        print('tree')
        return None

print('')
print('*'*36)
print('*'*36)
print('*'*11+'한글 문장 분석'+'*'*11)
print('*'*4+'한글 문장만 분석 가능합니다.'+'*'*4)
print('*'*36)

inputStr= input('문장을 입력하세요(한글만 가능) : ')
print('분석할 문장은 "'+inputStr+'" 입니다.')
inputL = inputStr.split(" ")
for i in inputL:
    print('')
    #print(i)
    nlp1 = NLP()   
    nlp1.beforeTXT = i
    print('분석할 어절은 '+nlp1.beforeTXT+'입니다.')
    txtLength = nlp1.getLength()
    print('문장 길이 : '+str(txtLength))
    retL = nlp1.getOneWord()
    print()
    print('***** 형태소 분석 *****')
    print('** 형태소,유니코드값 **')
    for cnt in range(0,txtLength):
        print(retL[cnt])

input('아무 키나 누르면 종료됩니다.')


'''
cntL = len(retL)
for i in range(0,cntL):
    cntU = len(retL[i])
    for j in range(1,cntU,2):
        print(retL[i][j])
'''
