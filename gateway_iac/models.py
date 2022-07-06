class Bill:
#   `document` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
#   `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
#   `amount` DECIMAL(6,2) NOT NULL DEFAULT '0.00',
#   `date` DATE NOT NULL,
#   `reference` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
#   `status` TINYINT(1) NOT NULL DEFAULT '0',
    
    def add(self, file):
        query=[]
        query+="INSERT INTO bills (document, email, amount, date, reference) VALUES "
        for bill in file:
            print(file)
            query+="("+bill["cpf"], bill["email"], bill["amount"], bill["date"], bill["codigo"]+")"
            with DBConn().cnx.cursor() as cursor:
                cursor.execute(query)
                DBConn().cnx.commit()