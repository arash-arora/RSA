import random

message = input("Your message is: ").lower()
length = len(message)
# print(f"Length of message is {length}")

alpha=[]

for i in message:
  alpha.append(str(ord(i) - 96))

# print(alpha)
str_alpha = "".join(alpha)
int_alpha = int(str_alpha)
length = int_alpha
print(f"Length of message is {length}")

#KEY GENERATION

#Selecting 2 prime numbers 

primes = []

for i in range(2,20):
  flag = 0
  for j in range(1,i+1):
    if i%j == 0:
      flag += 1
  if flag == 2:
    primes.append(i)


print(primes)
p = random.choice(primes)
q = random.choice(primes)
while(p>=q):
  q = random.choice(primes)

print(p,q)
# p = 13
# q = 19

n = p*q
print(n)
phi = (p-1)*(q-1)
e = 2
print(f"phi : {phi}")

while(e < phi):
  for i in range(1, e+1):
    if e%i==0 and phi%i==0:
      hcf=i
  if hcf==1:
    break
  else:
    e+=1

print(f"e = {e}")

d = 2
while(1):
  if (e*d)%phi == 1 :
    break
  else:
    d+=1
print(f"d = {d}")

print(f"Public key : {(e,n)}")   
print(f"Private key : {(d,n)}")


# ENCRYPTION
cipher = (int_alpha**e) % n
print(f"Encrypted : {cipher}")


# DECRYPTION
plain = (cipher**d) % n
print(f"Decryped : {plain}")