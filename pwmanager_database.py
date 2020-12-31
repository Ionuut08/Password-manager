import sqlite3

dbfile = 'pwmanager.db'

con = sqlite3.connect(dbfile)

current = con.cursor()


# current.execute("CREATE TABLE passwords ("
#                 "id integer PRIMARY KEY, "
#                 "website text not null, "
#                 "username text not null, "
#                 "password text not null);")

# table_list = [a for a in current.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
# # # here is you table list
# print(table_list)

show = [a for a in current.execute("select * from passwords;")]
print(show)

con.close()