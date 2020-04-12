'''
RSA implements the RSA public-key cryptosystem
   @author: Shelby Neal
   Emplid: 6030859
   Email: ssn287@email.vccs.edu
   Purpose: Programming Assignment #4
'''

import random

'''
gcd method computes the greatest common denominator of two integers iteratively (since we are dealing with large numbers)
'''
def gcd(m, n):
    while n:
        m, n = n, m % n
    return abs(m)

'''
gcdExtended method uses the extended Euclidean algorithm to find integer coefficients x and y such that
   mx + ny = gcd(m, n)
'''
def gcdExtended(m, n):
    r1, r = abs(m), abs(n) #init remainders
    x, x1, y, y1 = 0, 1, 1, 0 #init x and y values
    while r: #while a remainder exists
        r1, (q, r) = r, divmod(r1, r) #swap remainders, use divmod function to set q = r1 // r and r = r1 % r
        #multiply x and y values by the quotient q and swap
        x, x1 = x1 - q * x, x
        y, y1 = y1 - q * y, y
    return r1, x1 * (-1 if m < 0 else 1), y1 * (-1 if n < 0 else 1) #return g, x, and y (g == 1 if parameters are coprime)

'''
isPrime method returns whether or not the given parameter n is prime
   this method has been optimized for large values of n
'''
def isPrime(n):
  if n == 2 or n == 3: return True #if n is 2 or 3 then true
  if n < 2 or n%2 == 0: return False #if n is 1 or even then false
  if n < 9: return True #if n is less than 10 and the previous conditions are not met then n is prime
  if n % 3 == 0: return False #if n is divisible by 3 then false
  r = (n ** 0.5) % 1 #take the square root of n
  f = 5
  while f <= r: #while f is less than the square root of n
    if n % f == 0: return False #if n is divisible by f then false
    if n % (f+2) == 0: return False #if n is divisble by f + 2 then false
    f += 6 #increment f by 6 and repeat
  return True

'''
multInverse method returns the modular inverse of two numbers that are coprime such that
   mx = 1 % m
'''
def multInverse(e, phi):
    g, x, y = gcdExtended(e, phi) #calls gcdExtended function and splits into x and y- components
    if g != 1: #if g is not one the numbers are not coprime
        raise ValueError
    return x % phi #returns the modular inverse of the prime number

'''
genKeyPair generates a public key with components (e, n) and a private key with components (d, n)
'''
def genKeyPair(p, q):
    if not (isPrime(p) and isPrime(q)): #if p and q are not coprime the keypair cannot be generated
        raise ValueError
    elif p == q: #if p and q are the same the keypair cannot be generated
        raise ValueError
    n = p * q
    phi =  (p - 1) * (q - 1) #phi is the totient of n
    e = random.randrange(1, phi) #selects a random integer between 1 and phi
    g = gcd(e, phi) #determines if the random integer is coprime with phi
    while g != 1: #if the numbers are not coprime, a new random integer is created until e and phi are both coprime
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = multInverse(e, phi) #generates component for private key using multInverse function
    return ((e, n), (d, n)) #returns public key and private key

'''
encrypt method encrypts a message using a public key
'''
def encrypt(pk, msg):
    key, n = pk #splits the public key into its components (e, n) where e is the key
    cipher = [pow(ord(char), key, n) for char in msg] #each char in the message is converted to unicode, raised the the power of e and modded by n
    return cipher #encrypted message is returned as an array

'''
decrypt method decrypts a cipher using a private key
'''
def decrypt(pk, cipher):
    key, n = pk #splits the private key into its components (d, n) where d is the key
    plain = [chr(pow(char, key, n)) for char in cipher] #each unicode point is raised to the power of d and modded by n, then converted into String format and stored in an array
    return ''.join(plain) #the String characters in the array are joined and the original decrypted message is returned

'''
main driver
'''
print("RSA Implementation")
p = int(input("Enter a prime number (e.g. 13): ")) #user inputs first prime number
q = int(input("Enter a different prime number (e.g. 17): ")) #user inputs second prime number
publ, priv = genKeyPair(p, q) #keypair is generated
print("Your public key is ", publ, ". Your private key is ", priv) #keypair is printed for user
msg = input("Enter a message to encrypt with your public key: ") #user inputs message to be encrypted
emsg = encrypt(publ, msg) #encrypted message is generated
print("Your encrypted message is: ")
print(''.join(map(lambda x: str(x), emsg))) #encrypted message is printed for user
print("Your message decrypted is: ")
print(decrypt(priv, emsg)) #message is decrypted for user