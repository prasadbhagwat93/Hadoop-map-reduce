#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
#import numpy

#number of columns of A/rows of B
n = int(sys.argv[1]) 

#Create data structures to hold the current row/column values (if needed; your code goes here)
cRow = [0]*n
cCol = [0]*n
res = 0.0;

currentkey = None

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

	line = line.strip()

	#Get key/value 
	key, value = line.split(",",1)
	

	#Parse key/value input (your code goes here)
	result = "("

	result = result + str(currentkey) +"), "
	token = value.split(" ")
	#print(token)
	#If we are still on the same key...
	
	if key==currentkey:

		#Process key/value pair (your code goes here)
		if(token[1] == "A"):
			cRow[int(token[2])] = token[3]
		elif(token[1] == "B"):
			cCol[int(token[2])] = token[3]


	#Otherwise, if this is a new key...
	else:
		#If this is a new key and not the first key we've seen
		if currentkey:
			#compute/output result to STDOUT (your code goes here)
			for i in range(0,n):
				
				xA = []
				#xA.append(cRow[i])
				xR =float(cRow[i])
				
				#xB = xB.append(cCol[i])
				xC = float(cCol[i])
				
				res = res + (xR*xC)
				
			print(result+str(res))
			cRow = [0]*n
			cRow[int(token[2])] = token[3]
			cCol = [0]*n
			res = 0.0;
			currentkey = key
			
		else:
			#Process input for new key (your code goes here)
			#print("****")
			currentkey = key
			if(token[1] == "A"):

				cRow[int(token[2])] = token[3]
			elif(token[1] == "B"):
				cCol[int(token[2])] = token[3]
			
#Compute/output result for the last key (your code goes here)

for i in range(0,n):
	#xA = (cRow[i]).split()
	xR = float(cRow[i])
	#xB = (cCol[i]).split()
	xC = float(cCol[i])
	res = res + (xR*xC)
print(result+str(res))

