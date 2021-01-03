import sqlite3
import os.path
import argparse

master_password = "master"
initialization_vector = "00112233445566778899AABBCCDDEEFF"


def xor_strings(s, t):
    return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))


# Temporary function to ``encrypt`` a password
def encrypt(p):
    encrypted_p = xor_strings(p, initialization_vector)
    return encrypted_p


encrypt(master_password)


def check_existence():
    if os.path.exists("info.txt"):
        pass
    else:
        file = open("info.txt", 'w')
        file.close()


# Let the user add a website, an username (generally an email) and a password


def append_new(website, username, password):
    dbfile = 'pwmanager.db'

    con = sqlite3.connect(dbfile)

    current = con.cursor()

    print()
    print()

    table_list = [a for a in current.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
    print(table_list)

    # add_website_stmt = "insert into passwords(website) values ? "
    # current.execute("insert into passwords(website) values (?) ", (website,))
    #
    # # add_username_stmt = "insert into passwords(username) values ? "
    # current.execute("insert into passwords(username) values (?) ", (user_name,))

    # add_password_stmt = "insert into passwords(password) values ? "
    current.execute("insert into passwords(website, username, password) values (?, ?, ?) ",
                    (website, username, password))
    con.commit()
    con.close()


# Let the user view all the accounts that he has on a specific website

# Let the user remove a website
def remove_a_website(website):
    dbfile = 'pwmanager.db'

    con = sqlite3.connect(dbfile)

    current = con.cursor()

    current.execute("Delete from passwords where website = ?", (website,))
    con.commit()
    con.close()

# Let the user list all the passwords, websites and usernames


def read_passwords():
    dbfile = 'pwmanager.db'

    con = sqlite3.connect(dbfile)

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
    # encrypted_password = encrypt("password")
    # append_new("gmail.com", "ionuuut.fer", encrypted_password)
    read_passwords()
    remove_a_website("gmail.com")
    read_passwords()
    # parser = argparse.ArgumentParser(description='Password manager', usage='%(prog)s <master_password> '
    #                                                                        '-<operation> <website> <username> <password>')
    # parser.add_argument('master_password', type=str)
    #
    # parser.add_argument('-add', type=str)
    #
    # subparsers = parser.add_subparsers(title='add commands')
    # subparsers.add_parser('website')
    # subparsers.add_parser('username')
    # subparsers.add_parser('password')
    #
    # parser.add_argument('-get', type=str)
    # parser.add_argument('-remove', type=str)
    # parser.add_argument('-list', type=str)
    # args = parser.parse_args()
    # print(args)
    #
    # if args.master_password != master_password:
    #     # raise ValueError("The master password {} is not recognised".format(args.master_password))
    #     print("Master password is not correct")


if __name__ == '__main__':
    main()
