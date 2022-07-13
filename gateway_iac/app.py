from chalice import Chalice, Response
from models import Bill

app = Chalice(app_name='gateway_iac')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/import-csv', methods=['POST'],
           content_types=['application/octet-stream'])
def bin_echo():
    raw_request_body = app.current_request.raw_body
    Bill().add(raw_request_body)
    return Response(body=raw_request_body,
                    status_code=200,
                    headers={'Content-Type': 'application/octet-stream'})