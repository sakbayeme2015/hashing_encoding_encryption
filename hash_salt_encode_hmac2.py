#!/usr/bin/env python2

import os
import hashlib
import sys
import hmac
import base64
from random import SystemRandom

if len(sys.argv) <=1:
 print "Usage python hash_salt_encode_hmac.py <username> <password>"
 exit()

def hashfunct_384():
 cryptogen = SystemRandom()
 sequence = [cryptogen.randrange(4096) for i in range(24)]
 hexsequence = list(map(hex, sequence))
 salt = "".join([x[2:] for x in hexsequence])
 username_object = sys.argv[1]
 hash_object = hashlib.sha384(username_object.encode('utf-8') + salt.encode('utf-8')).hexdigest()
 for z in username_object:
  return hash_object
print "The username is : " , hashfunct_384()

def base64encode_funct():
 cryptogen = SystemRandom()
 sequence = [cryptogen.randrange(4096) for m in range(24)]
 hexsequence = list(map(hex, sequence))
 salt = "".join([x[2:] for x in hexsequence])
 password_object = sys.argv[1]
 encode_object = base64.urlsafe_b64encode(hmac.new(bytearray(salt, 'utf-8'), bytearray(password_object, 'utf-8'),digestmod=hashlib.sha384).digest())
 for t in password_object:
  return encode_object
print "The password is : " , base64encode_funct()
