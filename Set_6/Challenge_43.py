#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time


# 扩展欧几里德算法
def e_gcd(a, b):
    if b == 0:
        return 1, 0, a
    (x, y, r) = e_gcd(b, a % b)
    return y, x - a // b * y, r


def private_key_x(s, k, H, r, q):
    (r1, q1, temp) = e_gcd(r, q)
    return (((s * k) - H) * r1) % q


def get_r_s(x, g, p, q, H, k):
    r = (pow(g, k, p)) % q
    (k1, q1, r1) = e_gcd(k, q)
    s = (k1 * (H + x * r)) % q
    if(r != 0):
        return r, s
    else:
        return -1, -1

if __name__ == '__main__':
    p = 0x800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb1
    q = 0xf4f47f05794b256174bba6e9b396a7707e563c5b
    g = 0x5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119458fef538b8fa4046c8db53039db620c094c9fa077ef389b5322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a0470f5b64c36b625a097f1651fe775323556fe00b3608c887892878480e99041be601a62166ca6894bdd41a7054ec89f756ba9fc95302291
    H_msg = 0xd2d0714f014a9784047eaeccf956520045c45265
    r = 548099063082341131477253921760299949438196259240
    s = 857042759984254168557880549501802188789837994940
    y = 0x84ad4719d044495496a3201c8ff484feb45b962e7302e56a392aee4abab3e4bdebf2955b4736012f21a08084056b19bcd7fee56048e004e44984e2f411788efdc837a0d2e5abb7b555039fd243ac01f0fb2ed1dec568280ce678e931868d23eb095fde9d3779191b8c0299d6e07bbb283e6633451e535c45513b2d33c99ea17

    print "------------------guess by s&r-------------------"
    start = time.clock()
    for k in range(0,pow(2,16)+1):
        x = private_key_x(s, k, H_msg, r, q)
        (r1, s1) = get_r_s(x, g, p, q, H_msg, k)
        if(r!=-1 and s!=-1):
            #print r, s
            #print hex(x)
            if(r1 == r and s1 == s):
                print "the private key is:" + str(hex(x))
                #print r,r1,s,s1
                break
    elapsed = (time.clock() - start)
    print("Time used:", elapsed)
    print "-----------------guess by pubkey-----------------"
    start = time.clock()
    for k in range(0, pow(2, 16) + 1):
        x = private_key_x(s, k, H_msg, r, q)
        y1= pow(g,x,p)
        if(y == y1):
            print "the private key is:" + str(hex(x))
            break
    elapsed = (time.clock() - start)
    print("Time used:", elapsed)






