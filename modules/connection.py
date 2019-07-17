import sqlite3

class Db:
  
  def __init__(self):
    print('New database connection')
  
  def __enter__(self):
    self.db = sqlite3.connect('data/mydb')
    return self.db.cursor()
  
  def __exit__(self, type, value, traceback):
    self.db.commit()
    self.db.close()
  