import json

def abrirJSON():
    empanadasTodas= []
    with open("data/data.json",'r') as openFile:
        empanadasTodas=json.load(openFile)
    return empanadasTodas

def guardarJSON(dic):
    with open("data/data.json",'w') as outFile:
        json.dump(dic,outFile)
