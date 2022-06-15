import pytest
from allocation.app import app


@pytest.fixture()
def client():
    return app.test_client()