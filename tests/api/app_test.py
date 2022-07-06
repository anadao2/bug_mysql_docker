from http import HTTPStatus
from pytest_chalice.handlers import RequestHandler
import json



def test_index(client: RequestHandler) -> None:
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json == {'hello': 'world'}

def test_post_bill(client: RequestHandler) -> None:
    file_test = ("000.000.000-00, nada@nada.com, 20.00, xx-xx-xxx, 06/07/2022"
                "111.111.111-11, nada@nada2.com, 10.00, 66-66-666, 30/07/2022")
    
    response = client.post('/import-csv', body=file_test, headers={'Content-Type': 'application/json'},)
    assert response.status_code == HTTPStatus.OK
    assert response.json == {"bill": {"json": "teste"}
}