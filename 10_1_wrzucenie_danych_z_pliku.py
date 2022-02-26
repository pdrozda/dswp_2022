import MySQLdb
import os
import numpy as np

host = 'localhost'
user = 'root'
passwd = ''
db = 'polaczeniePython'
folder = 'pliki_wzrost'
folder_inserted = 'wzrost_przetworzony'

db_connection = MySQLdb.connect(host=host, user=user,passwd=passwd, db=db)
cur = db_connection.cursor()

lista_plikow = os.listdir(folder)
print(lista_plikow)

for plik in lista_plikow:
    sciezka = folder+'/'+plik
    dane_wzrost = np.loadtxt(sciezka, delimiter=',')
    print('plik:', sciezka)
    print(dane_wzrost)
    for wiersz in dane_wzrost:
        print(wiersz)
        SQL_wstawianie = "INSERT INTO osoba(wzrost) VALUES("+str(wiersz)+")"
        cur.execute(SQL_wstawianie)
        db_connection.commit()
    os.rename(sciezka, folder_inserted+'/'+plik)




db_connection.close()