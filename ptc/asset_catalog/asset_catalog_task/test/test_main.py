import json
import os
import pytest
from typer.testing import CliRunner
from src.main import app,is_exist_file, send_to_server, update_cache


runner = CliRunner()

def test_app():
    result = runner.invoke(app, [""])
    with open("try.txt", 'w') as f:
        f.write("testing")
    assert result.exit_code == 0


def test_is_exist_file(): 
    with open("cache/cache.json", 'w')as f:
        f.write('{"try.txt": "try.txt"}')
    result = is_exist_file("try.txt")
    assert result == True
    
    
def test_update_cache():
    update_cache("try.txt")
    with open("cache/cache.json", 'r') as f:
        cache = json.load(f)
        if "try.txt" in cache:
            result=True
            cache.pop("try.txt")
        with open("cache/cache.json", "w") as f:
            json.dump(cache, f, indent=2)
    assert result==True 
        