import csv
import io
from utils import DBConn


class Bill:
#   `document` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
#   `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
#   `amount` DECIMAL(6,2) NOT NULL DEFAULT '0.00',
#   `date` DATE NOT NULL,
#   `reference` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
#   `status` TINYINT(1) NOT NULL DEFAULT '0',
    
    def add(self, file):
        table="bills"
        columns="(document, email, amount, date, reference)"

        #print(file)
        #print(file.decode())
        
        new_bytes_obj = io.BytesIO(file)
        next(new_bytes_obj)
        for line in new_bytes_obj:
            print (line.decode())
                    
            #query+="("+bill["cpf"], bill["email"], bill["amount"], bill["date"], bill["codigo"]+")"
            query = f"INSERT INTO {table} {columns} values ({str(line[0])})"
            print(query)

            #with DBConn().cnx.cursor() as cursor:
            #    cursor.execute(query)
            #    DBConn().cnx.commit()