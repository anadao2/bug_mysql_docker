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
   