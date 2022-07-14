import csv
import io
import codecs
from utils import DBConn


class Bill:
    def add(self, file):
        table="bills"
        columns="(document, email, amount, date, reference)"

        #print(file)
        #print(file.decode())
        
        new_bytes_obj = io.BytesIO(file)
        csv_reader = csv.reader(codecs.iterdecode(new_bytes_obj, 'utf-8'), delimiter=',')
        for row in list(csv_reader)[5:]:
            #print(row)
                                       
            values=str(row).replace(" ", "").replace("[", "").replace("]", "")            
            query = f"INSERT INTO {table} {columns} values ({values})"
            #print(query)

            conn=DBConn()
            with conn.cnx.cursor() as cursor:
                cursor.execute(query)
                conn.cnx.commit()
       
            # with conn.cnx.cursor() as cursor:   
            #     cursor.execute("SELECT * FROM bills")

            #     myresult = cursor.fetchall()

            #     for x in myresult:
            #         print(x)
