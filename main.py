import requests
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello_world():
    r = requests.get("https://zheng-chuang.synology.me")
    return r.text

