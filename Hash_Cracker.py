import hashlib

#intro
print("         -Python MD5 Hash Cracker-")
print("         Script by, Luke Allred.")
print("         Version: 1.0.0.")


#Wordlist
wordlist = "rockyou.txt"

#hash input
md5input = input("To begin, please input your MD5 Hash here: ")

print("The Hash: " + "'" + md5input + "' " + " is being cracked, please wait one moment as it could take some time...")

#Comparing hashes from the rockyou.txt wordlist
def file_open(wordlist):
    global password_file
    try:
        with open(wordlist, "r", encoding='latin-1') as password_file:
            for hashed in password_file:
                encoded = hashed.strip().encode('utf-8')
                md5hash = hashlib.md5(encoded).hexdigest()
                if md5hash == md5input:
                    print("The cracked Hash is: " + hashed)
                    break
    except FileNotFoundError:
        print("An Error has Occurred. Unable to read/locate wordlist")

file_open(wordlist)
