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
    
    
def test_post_user_validation(api_get):
    data={
        
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoes@example.com"
    }
    response=api_get.post("users",data)
    print(response.json())
    assert response.status_code==201
    print(response.json()['name'])
    assert(response.json()['username']=="johndoe")
    assert response.json()['name']=="John Doe"
   # id=response.json()['id']
    responsegetmessage=api_get.get("users/1")
    assert responsegetmessage.status_code==200
    assert responsegetmessage.json()['name']=="Leanne Graham"