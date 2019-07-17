	
import sqlite3
db = sqlite3.connect('data/mydb')
cursor = db.cursor()
sql = 'create table if not exists todos (id  integer primary key, todo text, finished integer)'
cursor.execute(sql)
sql = 'insert into todos (todo, finished) values ("Task 1", 1)'
cursor.execute(sql)
cursor.execute('SELECT * FROM todos')
print(cursor.fetchone())
db.close()