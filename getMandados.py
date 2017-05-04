import requests
from requests import Request
import json
from pprint import pprint
from time import sleep
import os  
import random

urlMandados = "http://www.cnj.jus.br/bnmp/rest/pesquisar"
ufs = ["PB", "PE", "RN"]

def firstRequest(data):
	firstResponse = requestData(data)
	numPaginas = firstResponse["paginador"]["totalPaginas"]
	return numPaginas

def requestData(data):
	response = requests.post(urlMandados, json=data);	

	if response.status_code == 200:
		dataResponse = response.json()
		pg = dataResponse["paginador"]["paginaAtual"]

		with open("resultado/RESPONSE/"+str(uf)+"/bnmp_response_"+str(format(pg, "05d"))+".json", "w") as out:
		    json.dump(dataResponse, out)

		return dataResponse
	else:
		return None

def requestUF(uf, dataTemplate, offset=0):

	dataTemplate["criterio"]["orgaoJulgador"]["uf"] = uf

	numPaginas = firstRequest(dataTemplate)
	for r in range(1+offset, numPaginas+1):
		sleep(0.5 + (random.random()/10))
		
		data = dataTemplate
		data["paginador"]["paginaAtual"] = r
		requestData(data)

		print("Download ("+str(r)+"/"+ str(numPaginas)+"): ", format(100 * (r)/numPaginas, ".4f"), "% concluído.")

def checkOffset(uf):
	i = 0;
	while os.path.isfile("resultado/RESPONSE/"+str(uf)+"/bnmp_response_"+str(format(i+1, "05d"))+".json"):
		i+=1
		print(i)

	return i


## SCRIPT

with open('requestTemplate.json') as dataFile:    
    dataTemplate = json.load(dataFile)

for uf in ufs:
	offset = checkOffset(uf)
	print("Iniciando captura de ", uf, "\n")
	print("Iniciando em : ", offset)
	requestUF(uf, dataTemplate, offset)
	print("Finalizado\n\n")