import sqlite3
import argparse
import encryption

master_password = "master"

dbfile = 'pwmanager.db'
con = sqlite3.connect(dbfile)

# Let the user add a website, an username (generally an email) and a password

def append_new(website, username, password):
    current = con.cursor()

    encrypted_password = encryption.encrypt_password(password, master_password).encode('utf-8').hex()
    current.execute("insert into passwords(website, username, password) values (?, ?, ?) ",
                    (website, username, encrypted_password))
    con.commit()
    con.close()


# Let the user view all the accounts that he has on a specific website

def get(website):
    current = con.cursor()
    str_website = str(website)

    select_password = [a for a in current.execute("SELECT password from passwords where website = ?",
                                                  (str_website,))]

    password_for_printing = str(select_password)[3:-4]
    password_for_decrypt = bytes.fromhex(password_for_printing).decode('utf-8')

    select_username = [a for a in current.execute("SELECT username from passwords where website = ?",
                                                  (str_website,))]

    select_username_for_printing = str(select_username)[3:-4]

    print("Username: ", select_username_for_printing)
    print("Password: ", encryption.decrypt_password(password_for_decrypt, master_password))

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
    parser = argparse.ArgumentParser(description='Password manager', usage='%(prog)s <master_password> '
                                                                           '-<operation> <website> <username> '
                                                                           '<password>')
    parser.add_argument('master_password', type=str)
    parser.add_argument('-get', type=str)
    parser.add_argument('-remove', type=str)
    parser.add_argument('-list', action='store_true', help="List all the websites, username and passwords")

    parser.add_argument('-add', nargs=3, type=str, help='the operation to be done')

    args = parser.parse_args()

    if args.master_password != master_password:
        raise ValueError("The master password {} is not recognised".format(args.master_password))

    if args.add:
        arguments = args.add
        website = arguments[0]
        username = arguments[1]
        password = arguments[2]
        append_new(website, username, password)
        print(website, username, password)

    elif args.list:
        read_passwords()

    elif args.get:
        website_to_be_read = args.get
        get(website_to_be_read)

    elif args.remove:
        website_to_be_removed = args.remove
        remove_a_website(website_to_be_removed)


if __name__ == '__main__':
    main()
