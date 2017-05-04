import json
import os  
from pprint import pprint
from dicttoxml import dicttoxml
from os import listdir
from os.path import isfile, join



ufs = ["PB", "RN", "PE"]

for uf in ufs:
	i=0
	jsonMandados = []
	jsonMandadosDetalhes = []
	jsonMandadosExtra = []

	print("Convertendo - ", uf, "\n")

	while os.path.isfile("resultado/RESPONSE/"+str(uf)+"/bnmp_response_"+str(format(i+1, "05d"))+".json"):
		with open("resultado/RESPONSE/"+str(uf)+"/bnmp_response_"+str(format(i+1, "05d"))+".json", "r") as dataFile: 
			data = json.load(dataFile)

			mandados = data["mandados"]
			for mandado in mandados:
				listDetalhesElement = mandado.pop("detalhes")
				mandadoElement = mandado

				jsonMandados.append(mandadoElement)

				dictDetalhesElement = dict()
				for d in listDetalhesElement:
					detalhes 	= d.split(":")
					
					atributo 	= detalhes[0].replace(" ", "")
					value 		= detalhes[1]

					dictDetalhesElement[atributo] = value

				dictDetalhesElement["id"] = mandadoElement["id"]
				jsonMandadosDetalhes.append(dictDetalhesElement)
		i+=1

	if jsonMandados != []:
		print("Escrevendo : XML/bnmp_mandados_"+str(uf)+".xml")
		f = open("resultado/XML/bnmp_mandados_"+str(uf)+".xml", 'w', encoding='utf8')
		dataXML = dicttoxml(jsonMandados)
		print(str(dataXML, 'utf-8'), file=f)
		f.close()

	if jsonMandadosDetalhes != []:	
		print("Escrevendo : XML/bnmp_detalhes_"+str(uf)+".xml")
		f = open("resultado/XML/bnmp_detalhes_"+str(uf)+".xml", 'w', encoding='utf8')
		dataXML = dicttoxml(jsonMandadosDetalhes)
		print(str(dataXML, 'utf-8'), file=f)
		f.close()

	pwd = 'resultado/dataID/'+uf
	files = [f for f in os.listdir(pwd) if os.path.isfile(os.path.join(pwd, f))]

	for f in files:
		with open(pwd+"/"+f, "r") as dataFile: 
			data = json.load(dataFile)

		jsonMandadosExtra.append(data["mandado"])

	if jsonMandadosExtra != []:	
		print("Escrevendo : XML/bnmp_extra_"+str(uf)+".xml")
		f = open("resultado/XML/bnmp_extra_"+str(uf)+".xml", 'w', encoding='utf8')
		dataXML = dicttoxml(jsonMandadosExtra)
		print(str(dataXML, 'utf-8'), file=f)
		f.close()

	print("Finalizado\n\n")