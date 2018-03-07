#!/usr/bin/env python3
# This program attempts all passwords in 'pw.txt' in combination with a user enterred password (pwd1) for the BIP38 key assigned to the BIP38 variable.
# Passwords from the list and manually enterred are combined in both possible orders.

import sys
import pybip38 # pip install pybip38
# Note: The pybip38 is limited to Bitcoin (only) BIP38 encoded keys, NOT other alt-coins that use BIP38. Probably based on validation performed by that library.

# Example BIP38 Key. Password = test
BIP38 = '6PnTPCDoztgePLK3bqmaVwc7MvcyKchc1ksabMuRiPeUemULFpsDd9eouD'

pwdf = "123"
dic = open("pw.txt", "r")

while pybip38.bip38decrypt(pwdf, BIP38) == False:

	pwd1 = raw_input("Enter password: ")
	dic.seek(0)
	for line in dic:
		pwd2 = line.strip()
		pwdf = str(pwd1) + str(pwd2)
		pwdf2 = str(pwd2) + str(pwd1)		
		print(pwdf) 
		print(pwdf2)
		if pybip38.bip38decrypt(pwdf, BIP38) != False or pybip38.bip38decrypt(pwdf2, BIP38) != False:
			print("\n## KEY FOUND: %s\n" % pwdf, 'or', pwdf2)
			pwd_file = open("winner", "w")
			pwd_file.write(pwdf)
			pwd_file.write(pwdf2)
			pwd_file.close()
			sys.exit(0)
			
	print("Key Not Found :(")
	pwd_file2 = open("loser", "w")
	pwd_file2.write(":)")
	pwd_file2.close()
	sys.exit(0)
		

		

