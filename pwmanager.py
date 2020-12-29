import sys
import argparse
import os.path

master_password = "master"
initialization_vector = "00112233445566778899AABBCCDDEEFF"


def xor_strings(s, t):
    return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))


# Temporary function to ``encrypt`` a password
def encrypt(p):
    encrypted_p = xor_strings(p, initialization_vector)
    print(encrypted_p)


encrypt(master_password)


def check_existence():
    if os.path.exists("info.txt"):
        pass
    else:
        file = open("info.txt", 'w')
        file.close()


def read_passwords():
    file = open('info.txt', 'r')
    content = file.read()
    file.close()
    print(content)


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

def append_new():
    file = open("info.txt", 'w')

    print()
    print()

    user_name = input("Please enter the user name: ")
    password = input("Please enter the password here: ")
    website = input("Please enter the website address here: ")

    print()
    print()

    usrnm = "UserName: " + user_name + "\n"
    pwd = "Password: " + password + "\n"
    web = "Website: " + website + "\n"

    file.write("---------------------------------\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write("---------------------------------\n")
    file.write("\n")
    file.close()


# Let the user view all the accounts that he has on a specific website

# Let the user remove a website

# Let the user list all the passwords, websites and usernames
