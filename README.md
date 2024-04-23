Simple MD5 Hash Cracker in python using the hash library.

How to use:
1. Make sure both the "Hash_Cracker.py" and "Rockyou.txt" files are in the same directory or change the path to wherever your wordlist is stored.
2. Open a Terminal in the directory where your Hash Cracker script is located and run the following command: "py Hash_Cracker.py"
3. Once prompted for an input, put in your Unsalted MD5 hash in and press enter.



*USEFUL INFORMATION*

1. You must have the rockyou.txt wordlist for this script to work and connected either by having it in the same directory as the Hash Cracker or by updating the `wordlist = "rockyou.txt"` portion to have the full path to where your wordlist is stored.
2. This script is only able to crack the hash of any password in the rockyou.txt file. If the password that is hashed is NOT in that wordlist, the program will be unable to crack it and fail.
3. This program is unable to crack salted hashes.
