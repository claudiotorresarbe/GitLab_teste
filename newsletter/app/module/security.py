import random
from hashlib import sha256

def encript(decripted):
    return sha256(decripted.encode()).hexdigest()

def compare(encripted,decripted):
    if encripted == encript(decripted):
        return True
    else:
        return False

def generate(length):
    number = [str(x) for x in range(0,10)]
    alphalower = [chr(i) for i in range(ord('a'),ord('z')+1)]
    alphaupper = [x.upper() for x in alphalower]
    especial = list("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""")
    return ''.join(random.choice(alphalower+alphaupper+especial+number) for x in range(length))
    