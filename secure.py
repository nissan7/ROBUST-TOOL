import sym1 as sym 
import rsa as rsa, binascii
'''
    main encryption module
'''

def signf(file_path):
    keyf = open("PrivateKey.pem","r")
    key = keyf.read()
    key = rsa.PrivateKey.load_pkcs1(key)
    keyf.close()
    f = open(file_path, "rb")
    signature = rsa.sign(f, key, 'SHA-1')
    signature = signature.encode('hex')
    f.close()
    return signature

def verifyf(file_path, pubKey, signature):
    signature = signature.decode('hex')
    print(type(signature), signature)
    f = open(file_path, "rb")
    key = rsa.PublicKey.load_pkcs1(pubKey)
    try:
            rsa.verify(f, signature, key)
    except rsa.VerificationError:
            return False

    return True



    
       

def keygen():
    (pub, pri) = rsa.newkeys(1024)
    f = open("./PrivateKey.pem", "w+b")
    pri = pri.save_pkcs1(format='PEM')
    f.write(pri)
    f.close()
    f = open("./PublicKey.pem","w+b")
    pub = pub.save_pkcs1(format= 'PEM')
    f.write(pub)
    f.close()
    
def encryptFile(file_path, pubKey):
    key = rsa.PublicKey.load_pkcs1(pubKey)
    sym.encrypt(file_path, key)


def decryptFile(file_path):

    keyf = open("PrivateKey.pem","r")
    key = keyf.read()
    key = rsa.PrivateKey.load_pkcs1(key)
    sym.decrypt(file_path, key)
    



