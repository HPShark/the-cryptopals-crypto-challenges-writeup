#!/usr/bin/python
# -*- coding: UTF-8 -*-

hex1 = 0x1c0111001f010100061a024b53535009181c
hex2 = 0x686974207468652062756c6c277320657965
hex = hex1 ^ hex2
print("hex1 ^ hex2 = %x")%(hex)
#hex1 ^ hex2 = 746865206b696420646f6e277420706c6179
