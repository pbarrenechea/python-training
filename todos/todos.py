import sqlite3

def create_todo(task):
  print("creating todo")
  db = sqlite3.connect('data/mydb')
  cursor = db.cursor()
  sql = 'insert into todos (todo, finished) values ("' + task + '", 0)'
  cursor.execute(sql)
  db.commit()
  db.close()
  
def list_todos():
  print("Print todos")
  db = sqlite3.connect('data/mydb')
  cursor = db.cursor()
  sql = 'select * from todos'
  cursor.execute(sql)
  db.commit()
  results = cursor.fetchall()  
  db.close()
  return results