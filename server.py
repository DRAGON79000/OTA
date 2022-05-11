from glob import glob
from turtle import st
from methods import getRecord,getFiles
from fastapi import FastAPI
from github import Github
import uvicorn
import dotenv
import socket

config = dotenv.dotenv_values(".env")
g = Github(config["TOKEN"])
startRecord = getRecord(getFiles(config["REPO"],g,names=False))
count = 0
app = FastAPI()

@app.get("/check-update")
def check_update():
    global startRecord
    global count
    record = getRecord(getFiles(config["REPO"],g,names=False))
    if record == startRecord and count == 1:
        return {"update":False}
    startRecord = record
    if count == 0:
        count += 1
    return {"update":True}

@app.get("/get_update")
def get_update():
    files = getFiles(config["REPO"],g,names=True)
    return {"files":files}

uvicorn.run(app,host='ip_address',port='port_number')