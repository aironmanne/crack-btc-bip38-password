#!/usr/bin/env python3
# This program attempts all passwords in 'pw.txt' in combination with a user enterred password (manpw) and all passwords in pw2.txt for the BIP38 key assigned to the BIP38 variable.
# Passwords from the list and manually enterred are combined in both possible orders.

import sys
import pybip38 # pip install pybip38
# Note: The pybip38 is limited to Bitcoin (only) BIP38 encoded keys, NOT other alt-coins that use BIP38. Probably based on validation performed by that library.

# Example BIP38 Key. Password = test
BIP38 = '6PnTPCDoztgePLK3bqmaVwc7MvcyKchc1ksabMuRiPeUemULFpsDd9eouD'

dicp1 = open("pw.txt", "r")
global passwords
passwords = []

manpw = raw_input("Enter password segment: ")

def inner(pw1):
	dicp2 = open("pw2.txt", "r")
	for line in dicp2:
		pw2 = line.strip()
		pw1c = pw1
		passwords.append(str(pw1c) + str(pw2))
		passwords.append(str(pw1c) + str(manpw) + str(pw2))
		passwords.append(str(pw2) + str(pw1c))
		passwords.append(str(pw2) + str(manpw) + str(pw1c))
		
	dicp2.close()

for line in dicp1:
	password1 = line.strip()
	inner(password1)
	

    
for item in passwords:
	print(item)
	if pybip38.bip38decrypt(item, BIP38) != False:
		print("XXXXXXXXXXXXXXXXXXXX")
		print("KEY FOUND: ")
		print(item)
		print("XXXXXXXXXXXXXXXXXXXX")
		sys.exit(0)

print("\n## Password NOT found :-(\n")
