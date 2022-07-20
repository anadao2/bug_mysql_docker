import csv
import io
import codecs
from mysql.connector import connect, Error

config = {
  'user': 'root',
  'password': 'mauFJcuf5dhRMQrjj',
  'host': 'mysql',
  'database':'bill_system',
  'raise_on_warnings': True
}

class DBConn:
  cnx=None
  def __init__(self):
    self.cnx = connect(**config)
    #self.cnx.close()
   
class ModelBase(DBConn):
    def __init__(self, table, columns):
          self.table = table
          self.columns = columns
          super().__init__()
   
    def save(self, values):
        query = f"INSERT INTO {self.table} {self.columns} values ({values})"
        #print(query)

        conn=DBConn()
        with conn.cnx.cursor() as cursor:
            cursor.execute(query)
            conn.cnx.commit()
    
    def list(self):
      with self.cnx.cursor() as cursor:
        query = f"SELECT * FROM {self.table}"
        cursor.execute(query)

        myresult = cursor.fetchall()
        print (myresult)
        return myresult

    def get(self, id):
      with self.cnx.cursor() as cursor:
        query = f"SELECT * FROM {self.table} where id={id}"
        cursor.execute(query)

        myresult = cursor.fetchall()
        return myresult

class FileImport:
   def read_binary_csv(self, file):
        new_bytes_obj = io.BytesIO(file)
        csv_reader = csv.reader(codecs.iterdecode(new_bytes_obj, 'utf-8'), delimiter=',')
        return csv_reader