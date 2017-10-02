#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
def isreadable(str): # check readability (allow only alphanumeric chars and some punctiation)
    return bool(re.search('^[a-zA-Z0-9\., \'\"\-_\:\(\)]+$', str))

#字符串两两分组存入list
str1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
n = 2
str = []
str = [str1[i:i + n] for i in xrange(0, len(str1), n)]
#print str
#print (type(str))

#统计词频
feq = {}
for x in str:
    if str.count(x)>1:
        feq[x] = str.count(x)
#print(feq)
s1 = max(feq, key=feq.get)
#print s1
#{'39': 2, '33': 2, '31': 2, '37': 5, '36': 3, '1b': 2, '78': 6}

#统计结果显示0x78出现次数最多，预测为空格，异或之后得到密钥
key = chr(int(s1, 16) ^ 0x20)
print("key = %s")%(key)
#key = X

#key与密文异或得到明文
text = []
for x in str:
    text.append(chr(ord(key) ^ int(x,16)))
    #text.append()
a = ""
#print text
#print ("the text is: %s")%a.join(text)

if (isreadable(a.join(text))):
    print ("the text is: %s") % a.join(text)