import sqlite3
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


# Let the user add a website, an username (generally an email) and a password


def append_new():
    dbfile = 'pwmanager.db'

    con = sqlite3.connect(dbfile)

    current = con.cursor()

    ident = 1
    website = "website.com"
    user_name = "ionut.feraru"
    password = "verystrongpassword"

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
    current.execute("insert into passwords(id, website, username, password) values (?, ?, ?, ?) ",
                    (ident, website, user_name, password))
    con.commit()
    con.close()


# Let the user view all the accounts that he has on a specific website

# Let the user remove a website

# Let the user list all the passwords, websites and usernames

def main():
    append_new()
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

    # if args.master_password != master_password:
    #     # raise ValueError("The master password {} is not recognised".format(args.master_password))
    #     print("Master password is not correct")


if __name__ == '__main__':
    main()
