import sqlite3
import os.path
import argparse
import os
import encryption

master_password = "master"

dbfile = 'pwmanager.db'

con = sqlite3.connect(dbfile)


# def xor_strings(s, t):
#     return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))
#
#
# # Temporary function to ``encrypt`` a password
# def encrypt(p):
#     encrypted_p = xor_strings(p, initialization_vector)
#     return encrypted_p
#
#
# def decrypt(p):
#     encrypted_p = xor_strings(p, initialization_vector)
#     return encrypted_p


def check_existence():
    if os.path.exists("info.txt"):
        pass
    else:
        file = open("info.txt", 'w')
        file.close()


# Let the user add a website, an username (generally an email) and a password


def append_new(website, username, password):
    current = con.cursor()

    print()
    print()

    # table_list = [a for a in current.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
    # print(table_list)

    encrypted_password = encryption.encrypt_password(password, master_password)
    current.execute("insert into passwords(website, username, password) values (?, ?, ?) ",
                    (website, username, encrypted_password))
    con.commit()
    con.close()


# Let the user view all the accounts that he has on a specific website
def get(website):
    current = con.cursor()
    str_website = str(website)
    #
    # select_password = [a[0] for a in current.execute("SELECT password from passwords where website = ?",
    #                                               (str_website,))]
    # print(select_password)
    # decrypted_password = decrypt(select_password, "l")

    get_website = [a for a in current.execute("SELECT website, username, password from passwords where website = ?",
                                              (str_website,))]
    print(get_website)

    con.commit()
    con.close()


# Let the user remove a website

def remove_a_website(website):
    current = con.cursor()

    current.execute("Delete from passwords where website = ?", (website,))
    con.commit()
    con.close()


# Let the user list all the passwords, websites and usernames


def read_passwords():
    current = con.cursor()

    show_usernames = [a for a in current.execute("Select username from passwords")]
    print(show_usernames)

    show_websites = [a for a in current.execute("Select website from passwords")]
    print(show_websites)

    show_passwords = [a for a in current.execute("Select password from passwords")]
    print(show_passwords)

    con.commit()
    con.close()


def main():
    password = 'parola foarte grea'
    print(encryption.encrypt_password(password, master_password))

    parser = argparse.ArgumentParser(description='Password manager', usage='%(prog)s <master_password> '
                                                                           '-<operation> <website> <username> <password>')
    parser.add_argument('master_password', type=str)
    parser.add_argument('-get', type=str)
    parser.add_argument('-remove', type=str)
    parser.add_argument('-list', action='store_true', help="List all the websites, username and passwords")

    parser.add_argument('-add', nargs=3, type=str, help='the operation to be done')

    args = parser.parse_args()

    if args.add:
        arguments = args.add
        website = arguments[0]
        username = arguments[1]
        password = arguments[2]
        enc_p = encryption.encrypt_password(password, master_password)
        append_new(website, username, password)
        print(website, username, enc_p)

    elif args.list:
        read_passwords()

    elif args.get:
        website_to_be_read = args.get
        get(website_to_be_read)

    elif args.remove:
        website_to_be_removed = args.remove
        remove_a_website(website_to_be_removed)

    # for i, argument in enumerate(args.add):
    #     append_new(argument[1], argument[2], argument[3])
    #     print(f'[ {i} ] Supplied to add: {argument}')

    if args.master_password != master_password:
        raise ValueError("The master password {} is not recognised".format(args.master_password))


if __name__ == '__main__':
    main()
