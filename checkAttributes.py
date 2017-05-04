import json
import os  
from pprint import pprint


i = 0
atributosGeral = set([])
atributosDetalhes = set([])

ufs = ["PB"]
# ufs = ["PB", "PE", "RN"]
piorCaso = dict();

for uf in ufs:
	while os.path.isfile("resultado/"+str(uf)+"/bnmp_response"+str(i+1)+".json"):
		with open("resultado/"+str(uf)+"/bnmp_response"+str(i+1)+".json", "r") as dataFile: 
			data = json.load(dataFile)

			for j in range(len(data["mandados"])):
				atts = list(data["mandados"][j].keys())

				atributosGeral |= set(atts)

				for att in atts:
					attAtual = str(data["mandados"][j][att])

					if att in piorCaso:
						if len(attAtual) > piorCaso[att]:
							piorCaso[att] = len(attAtual)
					else:
						piorCaso[att] = len(attAtual)

					# if "numeroMandado" in piorCaso:
					# 	if piorCaso["numeroMandado"] == 30:
					# 		pprint(data["mandados"][j])
					# 		exit()

				for k in range(len(data["mandados"][j]["detalhes"])):
					detalhe = data["mandados"][j]["detalhes"][k].split(":")
					att = detalhe[0]

					atributosDetalhes |= set([att])

					if att in piorCaso:
						if len(detalhe[1]) > piorCaso[att]:
							piorCaso[att] = len(detalhe[1])
					else:
						piorCaso[att] = len(detalhe[1])
		i+=1

print("\n\n###################")
pprint(piorCaso)


print("\n\n###################")
pprint(atributosGeral)


print("\n\n###################")
pprint(atributosDetalhes)