import requests
from requests import Request
import json
from pprint import pprint
from time import sleep
import os  
import random

urlDetalhar = "http://www.cnj.jus.br/bnmp/rest/detalhar"
ufs = ["PB", "PE", "RN"]
# ufs = ["PB"]

def getData(data):
	response = requests.post(urlDetalhar, json=data);	

	if response.status_code == 200:
		dataResponse = response.json()

		with open("resultado/dataID/"+str(uf)+"/data_"+str(data["id"])+".json", "w") as out:
		    json.dump(dataResponse, out)

		return dataResponse
	else:
		return None

def request(uf, id):
	if not os.path.isfile("resultado/dataID/"+str(uf)+"/data_"+str(id)+".json"):
		sleep(0.5 + (random.random()/10))
		data = {"id": id}
		res = getData(data)

		if res is not None:
			print("Download "+uf+" - "+str(id)+" concluído.")
		else:
			print("Erro: Download "+uf+" - "+str(id)+".")
	
## SCRIPT

with open('requestDetalheCompletoTemplate.json') as requestFile:    
    requestTemplate = json.load(requestFile)

for uf in ufs:
	with open("resultado/JSON/bnmp_mandados_"+uf+".json") as dataFile:    
	    jsonMandados = json.load(dataFile)

	for m in jsonMandados["mandados"]:
		request(uf, m["id"])