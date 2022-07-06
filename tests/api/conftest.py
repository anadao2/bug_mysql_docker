import pytest

from chalice import Chalice

from gateway_iac.app import app as chalice_app


@pytest.fixture
def app() -> Chalice:
    return chalice_app