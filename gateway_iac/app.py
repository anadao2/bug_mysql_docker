from chalice import Chalice

app = Chalice(app_name='gateway_iac')


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/import-csv', methods=['POST'])
def import_csv():
    account_as_json = app.current_request.raw_body
    Bill().add(account_as_json)
    return {'account': account_as_json}
