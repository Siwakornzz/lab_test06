from fastapi.testclient import TestClient
from datetime import date
import sys        
sys.path.insert(0, '../lab_test06')        
from main import app

today = date.today()
client = TestClient(app)

def test_year_data_api():
    input = "2544"
    output = 21
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"age": output}

def test_year_overthanthisyear_api():
    input = "6666"
    output = "Year can't be over than " + str(today.year + 543)
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"msg": output}

def test_test_year_lowerthanzero_api():
    input = "-1"
    output = "Year can't be less than zero"
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"msg": output}