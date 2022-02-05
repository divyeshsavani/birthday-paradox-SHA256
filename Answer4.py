#Assignment 2:Public Key Cryptography and Hash Functions Cryptography and Secure Communications (MITS5500/CSCI5310)
#Answer4 :  There is less possibility you find collision in this so that I have increase round if that can help
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.backends import default_backend
import sympy
import random
import sys
import hashlib

def hashSHA(a, b, c):
    d=str(a)+str(b)+str(c)
    digest = hashlib.sha256(d.encode())
    temp = digest.hexdigest()
    temp = int(str(temp),16)
    # print(temp)
    return digest.hexdigest()

class answer4:
	def SHA_256(self):
		i=j=0
		listComposite = listPrimes = []
		setPrimes = []
		valueHash = []

		for i in range (2,256):
			listComposite.append(i)
		listPrimes = list(sympy.primerange(2,256)) #list of prime numbers less than 2^8
		
		# remove all prime numbers from the list of 2 to 256
		for element in listComposite:
			if element in listPrimes:
				listComposite.remove(element) 

		for i in range (10):
			prime1 = sympy.randprime(2,256)
			prime2 = sympy.randprime(2,256)

			if prime2 == prime1: #check weather both the eandomly selected number is not same
				prime2 = sympy.randprime(2,256)
			prime3 = sympy.randprime(2,256)

			if prime3 == prime1 or prime3 == prime2:
				prime3 = sympy.randprime(2,256)
			
			#made set of prime numbers
			primes = set((prime1,prime2,prime3))
			
			#made list of tuple primes
			setPrimes.append(primes) 
			
			hash = hashSHA(prime1,prime2,prime3) 
			valueHash.append(hash)

			print(primes," || ",hash)
			i=i+1
		#for loop ends
		
		composite1 = random.choice(listComposite)
		composite2 = random.choice(listComposite)
		
		if composite2 == composite1:
			composite2 = random.choice(listComposite)
		composite3 = random.choice(listComposite)
		
		if composite3 == composite1 or composite3 == composite2:
			composite3 = random.choice(listComposite)
		
		composites = set((composite1,composite2,composite3))
		
		hashComposite = hashSHA(composite1,composite2,composite3)
		
		print("Looking for a fraudulent message that matches a valid message's hash...")
		
		while j < 10000000:
			if hashComposite in valueHash:
				j=j+1
				print("collision found after ", j ," attempts:")
				
				#find the index of prime set
				flag = valueHash.index(hashComposite)
				
				print(setPrimes[flag]," || ",valueHash[flag])
				print(composites," || ",hashComposite)
				sys.exit()
			else:
				composite1 = random.choice(listComposite)
				composite2 = random.choice(listComposite)
				
				if composite2 == composite1:
					composite2 = random.choice(listComposite)
				composite3 = random.choice(listComposite)
				
				if composite3 == composite1 or composite3 == composite2:
					composite3 = random.choice(listComposite)
				
				composites = set((composite1,composite2,composite3))
				
				hashComposite = hashSHA(composite1,composite2,composite3)
				
				j=j+1
		#while loops end here

answer = answer4() #insatnce of class	
answer.SHA_256() #function call