from utils.apis import APIS
import pytest

@pytest.fixture(scope='module')
def post_api():
    return APIS()

def test_post_user_validation(post_api):
    data={
        
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoes@example.com"
    }
    response=post_api.post("users",data)
    print(response.json())
    assert response.status_code==201
    responsemessage=post_api.get("users/1")
    print(responsemessage.json())
    assert responsemessage.status_code==200

    assert len(responsemessage.json())>0
    assert responsemessage.json()['name']=="Leanne Graham"