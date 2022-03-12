import sqlite3 as sql

Db = sql.connect(database="bbdd.dat")
cursor = Db.cursor()

cursor.execute("""create table empleados (dni text, name text, department text)""")
cursor.execute("""insert into empleados values ('15456112', 'Manuel Tebeo', 'Contabilidad')""")

Db.commit()

cursor.execute("""insert into empleados values ('15456112', 'Pedro Picapiedra', 'Contabilidad')""")

Db.commit()

cursor.execute("""select * from empleados where department='Contabilidad'""")

for tupla in cursor.fetchall():
    print(tupla)

