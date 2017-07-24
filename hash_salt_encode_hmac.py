#!/usr/bin/env python2

import os
import hashlib
import hmac
import uuid
import base64
import sys


if len(sys.argv) <= 1:
 print "Usage python hash_salt_encode_hmac.py <username> <password>"
 exit()

def hash384_funct():
 salt = uuid.uuid4().hex
 username_object = sys.argv[1]
 hash_object = hashlib.sha384(username_object.encode('utf-8') + salt.encode('utf-8')).hexdigest()
 for m in username_object:
  return hash_object
print "the username is : " , hash384_funct()

def base64encode():
 salt = uuid.uuid4().hex
 password_object = sys.argv[1]
 signature_object = base64.urlsafe_b64encode(hmac.new(bytearray(salt, 'utf-8'), bytearray(password_object, 'utf-8'), digestmod=hashlib.sha384).digest())
 for z in password_object:
  return signature_object
print "the password is : " , base64encode()
