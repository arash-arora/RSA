import random

message = input("Your message is: ").lower()
length = len(message)
# print(f"Length of message is {length}")

alpha=[]

for i in message:
  alpha.append(str(ord(i) - 96))

# print(alpha)
str_alpha = "".join(alpha)
length = int(str_alpha)

if len(str_alpha) > 2 : 
  print("Try again! The message is larger for the key to encrypt.")
print(f"Message is {length}")

#KEY GENERATION

#Selecting 2 prime numbers 

primes = []

for i in range(2,25):
  flag = 0
  for j in range(1,i+1):
    if i%j == 0:
      flag += 1
  if flag == 2:
    primes.append(i)


# print(primes)
while(1):
  p = random.choice(primes)
  q = random.choice(primes)
  while(p>=q):
    q = random.choice(primes)
  if(p*q > length):
    break

# print(p*q)

#RSA's MODULO
n = p*q
if n < length:
  print("Try Again! The Key was small to encrypt such plain text.")
  exit()

#EULER's CONSTANT
phi = (p-1)*(q-1)
e = 2

#e - public exponent
while(e < phi):
  for i in range(1, e+1):
    if e%i==0 and phi%i==0:
      hcf=i
  if hcf==1:
    break
  else:
    e+=1

#d - private exponent
d = 2
while(1):
  if (e*d)%phi == 1 :
    break
  else:
    d+=1


print(f"Public key : {(e,n)}")   
print(f"Private key : {(d,n)}")


# ENCRYPTION
cipher = (length**e) % n
print(f"Encrypted Message : {cipher}")


# DECRYPTION
plain = (cipher**d) % n
print(f"Decryped Message : {plain}")