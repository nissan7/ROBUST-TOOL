import sys
import os
import rsa as rsa
import binascii
import std
block = std.block
'''
  symmetric encryption module
  must include std.py
  requirement: python 3.2 or above
  not compatible with python 2.x
'''
def SymKey(size):
    hash = os.urandom(size//8)
    return hash
def to_bytes(n, length, endianess):
    h = '%x' % n
    s = ('0'*(len(h) % 2) + h).zfill(length*2).decode('hex')
    if endianess == 'big':
        s = s[:: -1]
    return s
def encrypt(fileName, encKey):
    key = SymKey(std.key_size)
    enc = rsa.encrypt(key, encKey)
    rf = open(fileName+".enc", "w+b")
    rf.write(enc)
    df = open(fileName,"rb")
    df.seek(0, os.SEEK_END)
    dsize = df.tell()
    print(dsize)
    df.seek(0,0)
    fbsize = dsize//block
    #print(fbsize)
    rfbsize = dsize%block
    l = block//len(key)
    r = block%len(key)
    key = l*key + key[:r]
    kr = key[:rfbsize]
    #k = int.from_bytes(key, sys.byteorder, signed = False)
    k = int(key.encode('hex'), 16)
    #kr = int.from_bytes(kr, sys.byteorder, signed = False)
    kr = int(kr.encode('hex'), 16)
    result = bytearray()
    for i in range(fbsize):
        data = df.read(block)
        #db = int.from_bytes(data, sys.byteorder, signed = False)
        db = int(data.encode('hex'), 16)
        db = db^(k)
        db = to_bytes(db, block, sys.byteorder)
        result+=db
        if(len(result)>104857):
            rf.write(result)
            result = bytearray()
    data = df.read(rfbsize)
    #db = int.from_bytes(data, sys.byteorder, signed = False)
    db = int(data.encode('hex'), 16)
    db = db^(kr)
    db = to_bytes(db, rfbsize, sys.byteorder)
    rf.write(db)
    rf.close()
    df.close()

def decrypt(fileName, rsakey):
     
    df = open(fileName,"rb")
    df.seek(0,os.SEEK_END)
    size  = df.tell()
    df.seek(0,0)
    key = df.read(std.rsa//8)
    key = rsa.decrypt(key, rsakey)
    dsize = size - std.rsa//8
    fbsize = dsize//block
    #print(fbsize)
    rfbsize = dsize%block
    l = block//len(key)
    r = block%len(key)
    key = l*key + key[:r]
    kr = key[:rfbsize]
    #k = int.from_bytes(key, sys.byteorder, signed = False)
    k = int(key.encode('hex'), 16)
    #kr = int.from_bytes(kr, sys.byteorder, signed = False)
    kr = int(kr.encode('hex'), 16)
    result = bytearray()
    rf = open(fileName[:-4], "w+b")
    for i in range(fbsize):
        data = df.read(block)
        #db = int.from_bytes(data, sys.byteorder, signed = False)
        db = int(data.encode('hex'), 16)
        db = db^(k)
        db = to_bytes(db, block, sys.byteorder)
        result+=db
        if(len(result)>104857):
            rf.write(result)
            result = bytearray()
    data = df.read(rfbsize)
    #db = int.from_bytes(data, sys.byteorder, signed = False)
    db = int(data.encode('hex'), 16)
    db = db^(kr)
    db = to_bytes(db, rfbsize, sys.byteorder)
    rf.write(db)
    rf.close()
    df.close()
   
