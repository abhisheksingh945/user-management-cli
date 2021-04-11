import fire
import psycopg2
 
class MyDatabase():
  def __init__(self):
    self.conn = psycopg2.connect(user="abhishek945@practicetask", password="taskmonk@100", host="practicetask.postgres.database.azure.com", port="5432", database="postgres")
    self.cur = self.conn.cursor()

  def close(self):
    self.cur.close()
    self.conn.close()

def add():
   
  try :
    db = MyDatabase()  
    firstName = input ("First Name :")
    lastName = input ("Last Name :")
    phoneNumber = input("Phone Number :")
    email = input("Email :")
    db.cur.execute("INSERT INTO users VALUES (DEFAULT, %s,%s, %s, %s)", (   firstName, lastName, phoneNumber, email))
    db.conn.commit()
    print("User has been added")
  except Exception as e:
    print(e)
  finally:
    try:  
      db.close()
    except Exception as e:
      print(e)   


def show():  
  try:
    db = MyDatabase()
    db.cur.execute("SELECT * FROM users;")  
    rows = db.cur.fetchall()
    for row in rows :
      print(row[0], row[1], row[2], row[3], row[4])
  except Exception as e:
    print(e)
  finally:
    try:  
      db.close()
    except Exception as e:
      print(e)  

 
def remove (id): 
  try:
    db = MyDatabase()
    db.cur.execute("DELETE from users where id = %s;", [id])  
    row_count = db.cur.rowcount
    db.conn.commit()
    
    if row_count == 0 :
      print("Enter valid id")
    else:
      print("Record deleted succesfully")

  except Exception as e:
    print(e)
  finally:
    try:  
      db.close()
    except Exception as e:
      print(e)  

   
def update(id):
  try:
    firstName = input ("First Name :")
    lastName = input ("Last Name :")
    phoneNumber = input("Phone Number :")
    email = input("Email :")    
    db = MyDatabase()
    db.cur.execute("UPDATE users SET (firstname, lastname, phonenumber, email) = (%s, %s, %s, %s) WHERE id = %s", (firstName, lastName, phoneNumber, email, id))
    
    row_count = db.cur.rowcount
    db.conn.commit()
    
    if row_count == 0 :
      print("Enter valid id")
    else:
      print("Record updated succesfully")

    
  except Exception as e:
    print(e)
  finally:
    try:  
      db.close()
    except Exception as e:
      print(e)  


if __name__ == '__main__':
  fire.Fire({
    'add': add,
    'show': show,
    'remove' : remove,
    'update' : update,
  })

 