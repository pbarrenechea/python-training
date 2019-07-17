import sqlite3
from modules import connection

def create_todo(task):
  print("creating todo")
  db = connection.Db()
  with db as db_cursor:
    sql = 'insert into todos (todo, finished) values ("' + task + '", 0)'
    db_cursor.execute(sql)
    
def list_todos():
  print("Print todos")
  db = connection.Db()
  with db as db_cursor:
    sql = 'select * from todos'
    db_cursor.execute(sql)
    results = db_cursor.fetchall()  
    return results