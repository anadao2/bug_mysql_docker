from chalice import Chalice, Response
from models import Bill
from utils import FileImport
import mysql.connector

app = Chalice(app_name='gateway_iac')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/import-csv', methods=['POST'],
           content_types=['application/octet-stream'])
def bin_csv():
    bill = Bill()
    try:
        raw_request_body = app.current_request.raw_body
        
        csv_reader = FileImport().read_binary_csv(raw_request_body)

        for row in list(csv_reader)[5:]:                                
            values=str(row).replace(" ", "").replace("[", "").replace("]", "")
            bill.save(values)
    
    except mysql.connector.DataError as err:
          print("Something went wrong: {}".format(err))

        
    
    return Response(body=bill.list(),
                    status_code=200,
                    headers={'Content-Type': 'application/octet-stream'})