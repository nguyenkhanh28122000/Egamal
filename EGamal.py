#thuật toán egamal
from math import sqrt
import random

def randomNum(a,b):
    ran = random.randint(a,b)
    return ran
	
def isPrime( n):
 
    if (n <= 1):
        return False
    if (n <= 3):
        return True
 
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
 
    return True

def power( x, y, p):
 
    res = 1
    x = x % p

    while (y > 0):
 
        if (y & 1):
            res = (res * x) % p
 
        y = y >> 1 # y = y/2
        x = (x * x) % p
 
    return res
 
def findPrimefactors(s, n) :
 
    while (n % 2 == 0) :
        s.add(2)
        n = n // 2

    for i in range(3, int(sqrt(n)), 2):
        while (n % i == 0) :
 
            s.add(i)
            n = n // i
    if (n > 2) :
        s.add(n)

def findPrimitive( n) :
    s = set()
 
    # Check if n is prime or not
    if (isPrime(n) == False):
        return -1

    phi = n - 1

    findPrimefactors(s, phi)

    for r in range(2, phi + 1):

        flag = False
        for it in s:

            if (power(r, phi // it, n) == 1):
 
                flag = True
                break

        if (flag == False):
            return r

    return -1
# Driver Code
    
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,

                     31, 37, 41, 43, 47, 53, 59, 61, 67, 

                     71, 73, 79, 83, 89, 97, 101, 103, 

                     107, 109, 113, 127, 131, 137, 139, 

                     149, 151, 157, 163, 167, 173, 179, 

                     181, 191, 193, 197, 199, 211, 223,

                     227, 229, 233, 239, 241, 251, 257,

                     263, 269, 271, 277, 281, 283, 293,

                     307, 311, 313, 317, 331, 337, 347, 349]
 

def nBitRandom(n):

    return random.randrange(2**(n-1)+1, 2**n - 1)
 

def getLowLevelPrime(n):

    '''Generate a prime candidate divisible 

    by first primes'''

    while True:

        pc = nBitRandom(n) 

        for divisor in first_primes_list:

            if pc % divisor == 0 and divisor**2 <= pc:

                break

        else: return pc
 

def isMillerRabinPassed(mrc):

    '''Run 20 iterations of Rabin Miller Primality test'''

    maxDivisionsByTwo = 0

    ec = mrc-1

    while ec % 2 == 0:

        ec >>= 1

        maxDivisionsByTwo += 1

    assert(2**maxDivisionsByTwo * ec == mrc-1)
 

    def trialComposite(round_tester):

        if pow(round_tester, ec, mrc) == 1:

            return False

        for i in range(maxDivisionsByTwo):

            if pow(round_tester, 2**i * ec, mrc) == mrc-1:

                return False

        return True

    numberOfRabinTrials = 20

    for i in range(numberOfRabinTrials):

        round_tester = random.randrange(2, mrc)

        if trialComposite(round_tester):

            return False

    return True
 

def result(n):

    while True:

        

        prime_candidate = getLowLevelPrime(n)

        if not isMillerRabinPassed(prime_candidate):

            continue

        else:

            return prime_candidate

            break


def convert_name_to_number(name):
    m = 0
    for i in range(0, len(name)):
        m += (ord(name[i]) - ord('a')) * pow(26, len(name)-i-1)

    return m

def convert_number_to_name(m):
    name = ""
    while m > 0:
        q = m // 26
        r = m % 26
        name += chr(r+ord('a'))
        m = q
    return name[::-1]

if __name__ == '__main__':
    x="khanhhhh"
    p = result(48)
    a=randomNum(100000,999999)
    b = pow(findPrimitive(p), a, p)
    alpha=findPrimitive(p)
    cnametnum = convert_name_to_number(x);
    k=113
    xo=pow(alpha,k,p)
    kx=pow(b,k,p)
    ko=pow(cnametnum*kx,1,p)
    print('p =',p)
    print(alpha)
    
    print('a =',a)
    
    print ('b =' ,b)
    print ('Nametonumber:', cnametnum)
    print ('ek =(',xo, ',',ko,")")
    m=p-a-1
    do=pow(xo,m,p)
    dk=pow(ko*do,1,p)
    print('dk =',dk)
    print(convert_number_to_name(dk))