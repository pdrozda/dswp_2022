import MySQLdb

host = 'localhost'
user = 'root'
passwd = ''
db = 'polaczeniePython'


db_connection = MySQLdb.connect(host=host, user=user,passwd=passwd, db=db)
cur = db_connection.cursor()
SQL_wstawianie = "INSERT INTO osoba(wzrost) VALUES(199)"
cur.execute(SQL_wstawianie)
db_connection.commit()
SQL_select = "SELECT * FROM osoba"
cur.execute(SQL_select)
rows = cur.fetchall()
for row in rows:
    print("id=", row[0])
    print("wzrost=", row[1])
db_connection.close()