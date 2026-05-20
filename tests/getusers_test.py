from utils.apis import APIS
import pytest


@pytest.fixture(scope='module')
def api_get():
    return APIS()

def test_get_user_validation(api_get):
    response=api_get.get("users")
    print(response.json())
    assert response.status_code==200
    print(response.json())
    assert len(response.json())>0