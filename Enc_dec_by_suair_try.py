#Coding By Sudair 
#Encryption 
# decode
import random as gf
import os as qb
import base64 as tan

def tb(sz):
    return qb.urandom(sz)

def tx(te, sh):
    return ''.join(chr((ord(ch) + sh) % 256) for ch in te)

def rq(te, ky):
    gf.seed(ky)
    pr = list(range(len(te)))
    gf.shuffle(pr)
    return ''.join(te[i] for i in pr), pr

def je(dt, ky):
    return bytes(a ^ b for a, b in zip(dt, ky * (len(dt) // len(ky) + 1)))

fn = input("your file • : ")

with open(fn, 'r') as fl:
    oc = fl.read()

ky = tb(32)

cd = tan.b64encode(oc.encode())
cd = cd.decode('latin1')

cd = tx(cd, 15)

pc, pk = rq(cd, ky)

cd = ''.join(format(ord(ch), '08b') for ch in pc)

cd = je(cd.encode(), ky)
fe = tan.b64encode(cd).decode('latin1')

dc = f"""
import base64 as tan
import random as gf
import os as qb
def jd(dt, ky):
    return bytes(a ^ b for a, b in zip(dt, ky * (len(dt) // len(ky) + 1)))
def rq(te, pr):
    up = [''] * len(te)
    for i, ch in enumerate(te):
        up[pr[i]] = ch
    return ''.join(up)
ky = {ky}
pk = {pk}
ec = {repr(fe)}
def de(ec, ky, pk):
    cd = tan.b64decode(ec.encode('latin1'))
    cd = jd(cd, ky).decode()
    cd = ''.join(chr(int(cd[i:i+8], 2)) for i in range(0, len(cd), 8))
    cd = rq(cd, pk)
    cd = ''.join(chr((ord(ch) - 15) % 256) for ch in cd)
    cd = tan.b64decode(cd.encode('latin1')).decode()
    exec(cd)
de(ec, ky, pk)
"""

od = tan.b85encode(dc.encode()).decode()

fc = f"""
import base64 as tan
import os as qb
def T():
    C = '{od}'
    O = tan.b85decode(C).decode()

    A = '.ninjapy'
    with open(A, 'w') as temp_file:
        temp_file.write(O)
    
    qb.system(f'python {{A}}')
    qb.remove(A)

T()
"""
with open(f"ENC_{fn}", 'w') as fl:
    fl.write(fc)
print("done enc")