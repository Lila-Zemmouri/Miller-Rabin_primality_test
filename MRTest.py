def userInputValue():

	while True:

		try:
			user_input=input("Enter an odd integer >=3 :\n")
			n=int(user_input)
			if(n%2!=0):
				if (n>=3):
					break
		except ValueError:
			print("That's not an integer!")
			
	print("Input number value is: {}".format(n))
	return n

def FACT(m):
	liste1=[]
	#write n − 1 as 2s·t with t odd by factoring powers of 2 from n − 1
	s = 0
	t = m-1
    #As long as t is even, it is divided by 2 and s is incremented. After the loop t must be odd and s holds the number of factors 2 in n-1.
	while (t%2==0):
		s=s+1
		t = t/2
	liste1.append(s)
	liste1.append(int(t)) 
	return  liste1    

def RAB(a,n3):
	#RAB will test if an integer a between 1 and n is a Miller witness
	#for n. (return a if a is a witness and 0 otherwise).
	liste=FACT(n3)
	x=pow(a,liste[1])#x = a^t 
	i=1
	if(x%n3!=1) and (x%n3!=n3-1):
		while i<liste[0]:#for i = 1..s-1
			
			x = pow(a,pow(2,i)*liste[1]) #x = a ^ (2^i)
			if x%n3==n3-1:#x mod n=n-1
			 	break
			else:
				i=i+1	

			
		if(i==liste[0]):
			return a #a is a witness 
		else:
			return 0#a is not a witness
	else:
		return 0

def Alea(nn):
	global rand1
	rand1=random.randint(2, nn-1)
	return rand1

def Miller_Rabin(n2):
	#randomly drawing k numbers (20,30,40 etc.) displaying "compound" if one of 
	#the integers drawn is a Miller witness and "prime" if none is a miller witness. 
	val=random.randint(20,100)
	i=1
	while i<=val:
		a=Alea(n2)
		
		if(RAB(a,n2)==a):
			#print("composite")#we only need to find one miller witness to say that n is composite
			return False
		else:
			i=i+1

	return True

  


def nbTem(n1):
	nbT=0
	i=2
	while i<n1:
		if(RAB(i,n1)==i):
			nbT=nbT+1
		i=i+1
	return nbT
def intFermat(k):
	return pow(2,pow(2,k))+1

def intMersenne(k):
	return pow(2,k)-1

import random
from pandas import DataFrame
import matplotlib.pyplot as plt


if __name__=="__main__":
	
	liste=[]
	x=[]
	y=[]
	print("/***********************/ Témoins de Miller-Rabin /****************************/\n")
	n=userInputValue()
	
	
	#1 this funcion FACT will display the list [s, t] where s and t are the intervening integers
  	#in the decomposition of n - 1.
	liste=FACT(n)
	print("[s,t]: ")
	print(liste)

	premier=Miller_Rabin(n)
	print(premier)
	if(premier==True):
		print("{} is a prime number".format(n))
	else:
		print("{} is a composite number".format(n))


	#Test whether the Fermat and Mersenne integers are prime numbers for small values of k.
	fermat=[]
	mersenne=[]
	k=2
	for k in range(2,5):
		
		fermat.append(intFermat(k))
		mersenne.append(intMersenne(k))

	q=0
	pr=" "
	for q in range(3):
		val=random.randint(20,100)
		i=1
		#print(k)
		t=Miller_Rabin(fermat[q])
		if(t==True):
			pr="prime"
		else:
			pr="composite "
		print("The Fermat integer {} is ".format(fermat[q])+" "+pr)

	q=0
	for q in range(3):
		print(mersenne[q])
		t=Miller_Rabin(mersenne[q])
		if(t==True):
			pr="prime"
		else:
			pr="composite "
		print("The Mersenne integer {} is ".format(mersenne[q])+" "+pr)



	










