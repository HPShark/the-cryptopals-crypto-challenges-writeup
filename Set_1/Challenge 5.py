#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

strA = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
key = "ICE"

str1 = strA
#print strA

#先把数据按key长度分开，比如key='ICE'则把数据三个三个一组分开存入列
text = []
n = len(key)
str2 = []
str2 = [str1[i:i + n] for i in xrange(0, len(str1), n)]
#print str2
# print (type(str2))

#把分好组的数据和key一个一个拆开，一一对应
#ex:    str2[0] = ['B', 'u', 'r']
#       key[0]  = ['I', 'C', 'E']
for str3 in str2:
    n = 1
    str = []
    str = [str3[i:i + n] for i in xrange(0, len(str3), n)]
    k = [key[i:i + n] for i in xrange(0, len(key), n)]
    #print str
    #print k
    #对应元素一一异或，并存入text中
    for x,y in zip(str,k):
        #去0x补零
        text.append(((hex(ord(x) ^ ord(y))).replace("0x","")).zfill(2))
        #print ((hex(ord(x) ^ ord(y))).replace("0x","")).zfill(2)
        #print ord(y)
        #print(ord(x) ^ ord(y))

#连接text
a=""
print  ("%s") % (a.join(text))



