# ezpwatck
Dictionary attacks combined with manual input or a second dictionary file to crack BIP38 encrypted btc private keys.

ezdict:
Standard dictionary attack.
1. Save password file pw.txt in the program folder.
2. Edit the BIP38 variable to the BIP38 encrypted wallet key.
3. Compile and run.

ezdictcombo:
Combines dictionary attack with manually entered input, attempting the combination in both orders.
1. Save password file pw.txt in the program folder.
2. Edit the BIP38 variable to the BIP38 encrypted wallet key.
3. Compile and run.

ezdictcombo2:
Attempts same combinations as ezdictcombo, plus another as it prompts user for string to sandwich between dictionary combinations.
1. Save password files pw.txt and pw2.txt in the program folder.
2. Edit the BIP38 variable to the BIP38 encrypted wallet key.
3. Compile and run.

With inspiration from https://github.com/camAtGitHub/crack-btc-bip38-password
