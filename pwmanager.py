
import sys
import argparse

master_password = "master"
initialization_vector = "00112233445566778899AABBCCDDEEFF"

def xor_strings(s,t):
    return "".join(chr(ord(a)^ord(b)) for a,b in zip(s,t))

# Temporary function to ``encrypt`` a password
def encrypt(p):
	encrypted_p = xor_strings(p, initialization_vector)
	print(encrypted_p)

encrypt(master_password)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('master_password', type=str)
	
	parser.add_argument('-add', '--insertion', type=str)
	args = parser.parse_args()

	if args.master_password != master_password:
		# raise ValueError("The master password {} is not recognised".format(args.master_password))
		print("Master password is not correct")


if __name__ == '__main__':
	main()

# Let the user add a website, an username (generally an email) and a password

# Let the user view all the accounts that he has on a specific website

# Let the user remove a website

# Let the user list all the passwords, websites and usernames