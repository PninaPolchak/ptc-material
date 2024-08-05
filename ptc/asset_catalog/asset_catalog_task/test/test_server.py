import pytest
import os
from src.server import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
        
def test_upload_file(client):
    try:
        files = {'file': open("try.txt", 'rb')}
        response = client.post("http://0.0.0.0:4000/upload", data=files)
        os.remove("../server/try.txt")
        os.remove("try.txt")
        assert b'File try.txt upload to server' in response.data
        assert response.status_code == 200
        
    except Exception as e:
        raise ValueError(e)
