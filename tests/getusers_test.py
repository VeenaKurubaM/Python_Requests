from utils.apis import APIS
import pytest


@pytest.fixture(scope='module')
def apis():
    return APIS()

def test_get_user_validation(apis):
    response=apis.get("users")
    print(response.json())
    assert response.status_code==200