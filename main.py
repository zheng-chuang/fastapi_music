import requests
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello_world():
    text = requests.get("https://zheng-chuang.synology.me").text
    return text

