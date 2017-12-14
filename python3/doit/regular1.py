data = '''
park 789456-1231456
choi 451312-1231213
'''

result = []
for line in data.split('\n'):
    wresult = []
    for word in line.split(" "):
        if len(word)==14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        wresult.append(word)
    result.append(" ".join(wresult))
print("\n".join(result))

import re
pat = re.compile('(\d{6})[-]\d{7}')
print(pat.sub('\g<1>-*******',data))