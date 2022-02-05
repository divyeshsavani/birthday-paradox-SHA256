#Assignment 2:Public Key Cryptography and Hash Functions Cryptography and Secure Communications (MITS5500/CSCI5310)
#Answer3
import sympy
import random
import sys

class answer3:
	def birthday_paradox_attack(self):
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

		print("16 valid messages:")

		for i in range (16):
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
			
			#find hash value by XORing three prime number
			hash = prime1^prime2^prime3 
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
		
		hashComposite = composite1^composite2^composite3
		
		print("Looking for a fraudulent message that matches a valid message's hash...")
		
		while j < 1000:
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
				
				hashComposite = composite1^composite2^composite3
				
				j=j+1
		#while loops end here

answer = answer3() #insatnce of class	
answer.birthday_paradox_attack() #function call