import json
import os  
from pprint import pprint
from dicttoxml import dicttoxml

ufs = ["PB", "RN", "PE"]

for uf in ufs:
	i=0
	jsonMandados         = {"mandados": []}
	jsonMandadosDetalhes = {"detalhes": []}

	print("Convertendo - ", uf, "\n")

	while os.path.isfile("resultado/RESPONSE/"+str(uf)+"/bnmp_response_"+str(format(i+1, "05d"))+".json"):
		with open("resultado/RESPONSE/"+str(uf)+"/bnmp_response_"+str(format(i+1, "05d"))+".json", "r") as dataFile: 
			data = json.load(dataFile)

			mandados = data["mandados"]
			for mandado in mandados:
				listDetalhesElement = mandado.pop("detalhes")
				mandadoElement = mandado

				jsonMandados["mandados"].append(mandadoElement)

				dictDetalhesElement = dict()
				for d in listDetalhesElement:
					detalhes 	= d.split(":")
					atributo 	= detalhes[0].replace(" ", "")
					value 		= detalhes[1]

					dictDetalhesElement[atributo] = value

				dictDetalhesElement["id"] = mandadoElement["id"]
				jsonMandadosDetalhes["detalhes"].append(dictDetalhesElement)
		i+=1

	if jsonMandados != []:
		f = open("resultado/JSON/bnmp_mandados_"+str(uf)+".json", 'w', encoding='utf8')
		print(json.dumps(jsonMandados), file=f)
		f.close()

	if jsonMandadosDetalhes != []:	
		f = open("resultado/JSON/bnmp_detalhes_"+str(uf)+".json", 'w', encoding='utf8')
		print(json.dumps(jsonMandadosDetalhes), file=f)
		f.close()

	print("Finalizado\n\n")