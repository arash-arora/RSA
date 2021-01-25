# RSA
RSA ALGORITHM IN CRYPTOGRAPHY

# OVERVIEW OF RSA

* Get a plain text in order to encrypt it.
* Select any 2 prime numbers of your choice, more larger the prime number, more secure your encrypted data is. In my case i stored the prime numbers in p and q.
* n in the code which stands for the modulus in the RSA is equal to the product of those two prime numbers. n = p*q.
* REMEMBER THE LENGTH OF n SHOULD ALWAYS BE LARGER THAN THE LENGTH OF THE MESSAGE AS SUPPOSE n = 33 -> it can encrypt the message of maximum length 32.
* e which stands for public exponent. 
* φ(n) = (p − 1) × (q − 1) 
  φ(n) is an EULER's function of n to calculate the secret key. It's important to note that φ(n) and e should be co-prime (largest common factor = 1).
* d is the private exponent 
  (e*d)%phi == 1 -> the value of d is selected as per the equation stated.
  
  
> PUBLIC KEY = (e,n) <br />

> PRIVATE KEY = (d,n)

# Conversion of PLAIN TEXT to CIPHER TEXT
> cipher = (length**e) % n


# Conversion of CIPHER TEXT to PLAIN TEXT
> plain = (cipher**d) % n <br />

# TRY RUNNING YOURSELF
https://repl.it/@arasharora/RSA#main.py


# OUTPUT:
<hr>

![rsa](https://user-images.githubusercontent.com/52750629/105712557-f69d1480-5f3f-11eb-9357-61431515a5b9.PNG)

