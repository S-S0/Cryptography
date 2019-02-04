# Public-Key Cryptography Simple Code Sample
# Python 3.6.7
# https://github.com/S-S0

import random, time

def isPrime(int):
    if int <= 1:
        return False
    for i in range(2, int):
        if(int % i is 0):
            return False
    return True

def genRandPrimeNumb(min, max):
    randNum = random.SystemRandom().randint(minInteger, maxInteger)
    while(not(isPrime(randNum))):
        randNum = random.SystemRandom().randint(minInteger, maxInteger)
    return randNum

def eulersTheorem(int_1, int_2):
    return (int_1 - 1) * (int_2 - 1)

def euclideanAlgorithm(int_1, int_2):
    #GCD, int_1(Eulers_Theorem Value) > int_2
    r = int_1 % int_2
    while(r is not 0):
        int_1 = int_2
        int_2 = r
        r = int_1 % int_2
    return int_2

def isCoprime(int):
    #GCD == 1
    if int is 1:
        return True
    else:
        return False

def getValue_e(Eulers_Theorem):
    #e < 160(Eulers_Theorem Value) And Coprime With 160(Eulers_Theorem Value)
    randNum = random.randint(2, Eulers_Theorem - 1)
    while(not(isCoprime(euclideanAlgorithm(Eulers_Theorem, randNum)))):
        randNum = random.randint(2, Eulers_Theorem - 1)
    return randNum

def getValue_d(Eulers_Theorem, int_e):
    # d < 160 And (de % 160) = 1
    randNum = random.randint(2, Eulers_Theorem - 1)
    while((randNum * int_e % Eulers_Theorem) is not 1):
        randNum = random.randint(2, Eulers_Theorem - 1)
    return randNum

# Below Test Code
print("======== --- ========")
plainMsg = 73 # Must plainMsg < n Value

minInteger = 100
maxInteger = 500

print("Plain Message : ", plainMsg)
print()
startTime = time.time() # 시간 측정

p = genRandPrimeNumb(minInteger, maxInteger)
q = genRandPrimeNumb(minInteger, maxInteger)
n = p * q
Eulers_Theorem = eulersTheorem(p, q)

e = getValue_e(Eulers_Theorem) # Pub_Key = {e, n}
print('<-- Encrypting Start -->')
cryptMsg = pow(plainMsg, e, n) # Msg^e Modular n (Msg**e % n)
print("EncryptMsg : %s" % cryptMsg)
print(" --- Encrypted ---")

print()
d = getValue_d(Eulers_Theorem, e) # Pri_Key = {d, n}
print("Bruteforce or Generate Private Key --- %0.2f Seconds ---" % (time.time() - startTime))
print()

print('<-- Decrypting Start -->')
decryptMsg = pow(cryptMsg, d, n) # Msg^d Modular n (Msg**d % n)
print("decryptMsg : %s" % decryptMsg)
print(" --- Decrypted ---")
print("======== --- ========")