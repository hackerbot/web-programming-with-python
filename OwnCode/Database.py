import sqlite3 as db

conn = db.connect('database.db')
cursor = conn.cursor()
cursor.execute('drop table if exists table1')
cursor.execute('create table table1 (field1 text, field2 int)')
cursor.execute('insert into table1 values ("text1", 35)')
cursor.execute('insert into table1 values ("text2", 42)')
cursor.execute('insert into table1 values ("text3", 38)')
cursor.execute('insert into table1 values ("text4", 41)')
cursor.execute('insert into table1 values ("text5", 40)')
cursor.execute('insert into table1 values ("text6", 28)')
cursor.execute('insert into table1 values ("text7", 45)')
conn.row_factory = db.Row
cursor.execute('select * from table1')
rows = cursor.fetchall()
for row in rows:
    print('%s %s' % (row[0], row[1]))
cursor.execute('select avg(field2) from table1')
row = cursor.fetchone()
print('The average field2 for field1 is: %s' % row[0])