#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import hashlib
from itertools import permutations

LinesOfEachDsaMesssage = 4


def e_gcd(a, b):
    if b == 0:
        return 1, 0, a
    (x, y, r) = e_gcd(b, a % b)
    return y, x - a // b * y, r


def ReadDsaMessages(DsaMessages):
    msg = []
    s = []
    r = []
    m = []
    temp = re.split('\n', DsaMessages)
    #print temp
    i = 0
    for x in temp:
        if (i % LinesOfEachDsaMesssage == 0):
            msg.append(x.replace("msg: ", ""))
        if (i % LinesOfEachDsaMesssage == 1):
            s.append(x.replace("s: ", ""))
        if (i % LinesOfEachDsaMesssage == 2):
            r.append(x.replace("r: ", ""))
        if (i % LinesOfEachDsaMesssage == 3):
            m.append(x.replace("m: ", ""))
        i += 1
    #print s
    return msg, s, r, m


def ReadFile(path):
    file_object = open(path, 'rU')
    file_context = ""
    try:
        for line in file_object:
            file_context = file_context + line
    finally:
        file_object.close()
    return file_context


def get_k(m1, m2, q, s1, s2):
    (ss, qq, rr) = e_gcd(abs(s1-s2), q)
    return (abs(m1 - m2) * ss) % q


def private_key_x(s, k, H, r, q):
    (rr, q1, temp) = e_gcd(r, q)
    return (((s * k) - H) * rr) % q


def guess_x():
    for aaa in range(0, len(msg)):
        for bbb in range(0, len(msg)):
           m1 = int(m[aaa], 16)
           m2 = int(m[bbb], 16)
           s1 = int(s[aaa])
           s2 = int(s[bbb])
           k = get_k(m1, m2, q, s1, s2)
           r1 = int(r[aaa])
           H_msg = int(m[aaa], 16)
           x1 = private_key_x(s1, k, H_msg, r1, q)
           y1 = pow(g, x1, p)
           if (y == y1):
               print "the private key is:" + str(hex(x1))
               return 1
    return -1
if __name__ == '__main__':
    p = 0x800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb1
    q = 0xf4f47f05794b256174bba6e9b396a7707e563c5b
    g = 0x5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119458fef538b8fa4046c8db53039db620c094c9fa077ef389b5322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a0470f5b64c36b625a097f1651fe775323556fe00b3608c887892878480e99041be601a62166ca6894bdd41a7054ec89f756ba9fc95302291
    y = 0x2d026f4bf30195ede3a088da85e398ef869611d0f68f0713d51c9c1a3a26c95105d915e2d8cdf26d056b86b8a7b85519b1c23cc3ecdc6062650462e3063bd179c2a6581519f674a61f1d89a1fff27171ebc1b93d4dc57bceb7ae2430f98a6a4d83d8279ee65d71c1203d2c96d65ebbf7cce9d32971c3de5084cce04a2e147821

    DsaMessages = ReadFile("44.txt")
    (msg, s, r, m) = ReadDsaMessages(DsaMessages)
    guess_x()







