#Diffie-Hellman Key Exchange Simple Code Sample
# Python 3.6.7

import random, time

def genRandPrimeNumb(min, max):
    randNum = random.SystemRandom().randint(min, max)
    while(not(isPrime(randNum))):
        randNum = random.SystemRandom().randint(min, max)
    return randNum

def isCoprime(int):
    #GCD == 1
    if int is 1:
        return True
    else:
        return False

def isPrime(int):
    if int <= 1:
        return False
    for i in range(2, int):
        if(int % i is 0):
            return False
    return True

def euclideanAlgorithm(int_1, int_2):
    #GCD, Assume that int_1 > int_2
    r = int_1 % int_2
    while(r is not 0):
        int_1 = int_2
        int_2 = r
        r = int_1 % int_2
    return int_2

def getPrimitiveNumbList(primeNum): 
    # Calculate Primitive Root List
    listPrimitiveRoots = []
    listCoprime = []
    listComparativeGroup = []
    for i in range(1, primeNum):
        if (isCoprime(euclideanAlgorithm(primeNum, i))):
            listCoprime.append(i)
    for i in listCoprime:
        for j in range(1, primeNum):
            k = pow(i, j, primeNum)
            if k in listCoprime:
                listComparativeGroup.append(k)
            else:
                break
        listTemp = list(set(listCoprime) - set(listComparativeGroup))
        if not listTemp:
            listPrimitiveRoots.append(i)
        listComparativeGroup = []
    return listPrimitiveRoots

def choosePrimitiveRoot(RootsList):
    PrimitiveRoot = random.choice(RootsList)
    return PrimitiveRoot

# Below Test Code
print("======== --- ========")

minInteger = 100
maxInteger = 400

sharedPrimeNumb_q = genRandPrimeNumb(minInteger, maxInteger)
print("Shared Prime Number : ", sharedPrimeNumb_q)
sharedPrimitiveRoot_a = choosePrimitiveRoot(getPrimitiveNumbList(sharedPrimeNumb_q))
print("Shared Primitive Root : ", sharedPrimitiveRoot_a)
print("--- End of sharing ---")
print()
print("--- ALICE ---")
Alice_X = genRandPrimeNumb(minInteger, sharedPrimeNumb_q) # X < sharedPrimeNumb_q, Private_Value
print("Alice's X Value : ", Alice_X)
Alice_Y = pow(sharedPrimitiveRoot_a, Alice_X,sharedPrimeNumb_q) # Public_Value, a^X mod q
print("Alice's Y Value : ", Alice_Y)
print()
print("--- BOB ---")
Bob_X = genRandPrimeNumb(minInteger, sharedPrimeNumb_q) # X < sharedPrimeNumb_q, Private_Value
print("Bob's X Value : ", Bob_X)
Bob_Y = pow(sharedPrimitiveRoot_a, Bob_X, sharedPrimeNumb_q) # Public_Value, a^X mod q
print("Bob's Y Value : ", Bob_Y)
print()
print("--- Calculating Key Value... ---")
Alice_Key = pow(Bob_Y, Alice_X, sharedPrimeNumb_q) # The other person's Y^ Own X mod q
print("Alice Key : ", Alice_Key)
Bob_Key = pow(Alice_Y, Bob_X, sharedPrimeNumb_q) # The other person's Y^ Own X mod q 
print("Bob Key : ", Bob_Key)
print("======== --- ========")