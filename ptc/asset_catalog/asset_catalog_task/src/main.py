import typer 
import os
import json
import logging
import requests
from threading import RLock
from dotenv import load_dotenv

load_dotenv()

global lock
lock=RLock()

app = typer.Typer()

@app.command()
def main(file_path:str)-> None:
    try:
        with lock:
            if os.path.exists(file_path):
                if not is_exist_file(file_path):
                    if send_to_server(file_path) == 200:
                        update_cache(file_path)
            else:
                print(f"File '{file_path}' not exists")
    except Exception as e:
        raise ValueError(f"Failed upload file: {file_path} {e}")
    
    
def is_exist_file(file_path:str)->bool:
    try:
        f=open("cache/cache.json", 'r')
        cache = json.load(f)
        file_name = os.path.basename(file_path)
        if file_name in cache:
            print(f"File '{file_name}' already exists")
            return True
        
    except Exception as e:
        raise ValueError(e)

       
def send_to_server(file_path:str)->int:
    try:
        if os.path.exists(file_path):
            files = {'file': open(file_path, 'rb')}
            res = requests.post(os.getenv("SERVER_URL"), files=files)
            print(res.text)
            print(res.status_code)
            return res.status_code
        
    except Exception as e:
        raise ValueError(e)
    

def update_cache(file_path:str)-> None:
    try:
        f=open("cache/cache.json", 'r')
        cache = json.load(f)
        file_name = os.path.basename(file_path)
        cache[file_name] = file_path
        f=open("cache/cache.json", 'w')
        json.dump(cache, f, indent=2)
        print(f"File '{file_name}' uploaded to cache")
                
    except Exception as e:
        raise ValueError(e)
    
    
if __name__ == "__main__":
    app()
