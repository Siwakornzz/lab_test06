from fastapi.testclient import TestClient
import sys
sys.path.insert(0, "../lab_test06")
from main import app

client = TestClient(app)

def test_post_todo_insert(db):
    response = client.post("/",
        json={
            "name": "depressionboy",
            "description": "slept",
            "completed": "true",
            "date": "15-3-2565"
        }
    )
    assert response.status_code == 200
    assert response.json()[0]["name"] == "depressionboy"
    assert response.json()[0]["description"] == "slept"
    assert response.json()[0]["completed"] == True
    assert response.json()[0]["date"] == "15-3-2565"