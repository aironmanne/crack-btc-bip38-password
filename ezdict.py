#!/usr/bin/env python3
# This program attempts all passwords in 'pw.txt' for the BIP38 key assigned to the BIP38 variable.

import sys
import pybip38 # pip install pybip38
# Note: The pybip38 is limited to Bitcoin (only) BIP38 encoded keys, NOT other alt-coins that use BIP38. Probably based on validation performed by that library.

# Example BIP38 Key. Password = test
BIP38 = '6PnTPCDoztgePLK3bqmaVwc7MvcyKchc1ksabMuRiPeUemULFpsDd9eouD'

dic = open("pw.txt", "r")

for line in dic:

	pwd = line.strip()
	print(pwd) 
	
	if pybip38.bip38decrypt(pwd, BIP38) != False:
			print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
			print("XXXXXXXXXX   KEY FOUND XXXXXXXXXXXXX")
			print(pwd)
			print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
			print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
			pwd_file = open("winner", "w")
			pwd_file.write(pwd)
			pwd_file.close()
			sys.exit(0)
		
print("Key Not Found :(")
pwd_file2 = open("loser", "w")
pwd_file2.write(":)")
pwd_file2.close()
sys.exit(0)
