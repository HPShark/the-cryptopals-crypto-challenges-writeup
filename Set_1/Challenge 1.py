#!/usr/bin/python
# -*- coding: UTF-8 -*-

hexstr = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
print "hex to character:" + hexstr.decode('hex')
#hex to character:I'm killing your brain like a poisonous mushroom

characterstr = hexstr.decode('hex')
print "character to base64:" + characterstr.encode('base64')
#character to base64:SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t