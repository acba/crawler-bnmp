import sys
import json
import os  
from pprint import pprint
from dicttoxml import dicttoxml

dataFile = """{
  "sucesso": true,
  "mensagem": null,
  "mandado": {
    "id": 632242,
    "situacao": "Aguardando Cumprimento",
    "numero": "5884-32.2013.8.15.0011.0003",
    "data": "29/04/2013",
    "validade": "27/10/2032",
    "processo": "5884-32.2013.8.15.0011",
    "classe": "Pedido de Prisão Temporária",
    "assuntos": [
      "Homicídio Simples"
    ],
    "procedimentos": [
      "Outro N°00058843220138150011"
    ],
    "magistrado": "ALBERTO QUARESMA",
    "orgao": "Tribunal de Justiça do Estado da Paraíba, 2° TRIBUNAL DO JURI",
    "municipio": "CAMPINA GRANDE",
    "nomes": [
      "FRANCISCO HENRIQUE DA SILVA"
    ],
    "alcunhas": null,
    "sexos": [
      "MASCULINO"
    ],
    "documentos": null,
    "genitores": null,
    "genitoras": null,
    "nacionalidades": null,
    "naturalidades": null,
    "datasNascimentos": null,
    "aspectosFisicos": null,
    "profissoes": null,
    "enderecos": [
      "Rua Maestro Vila Lobos  N°: 43  Cidade: Campina Grande/PB "
    ],
    "dataDelito": "28/10/2012",
    "assuntoDelito": "",
    "motivo": "Preventiva",
    "prazo": "",
    "recaptura": "Não",
    "sintese": "DIANTE DO EXPOSTO, com base nos arts. 311 e 312 do CPP, e em hamonia com o parecer ministerial de fls. 49/51, por conveniencia da instrução criminal e para resguardar a aplicação da lei penal, DECRETO A PRISÃO PREVENTIVA de  Leandro Santos da Silva, Francisco Henrique da Silva e Tiago Bezerra da Silva, qualificaddos nos autos, os quais deverão ser recolhidos ao Predsidio Regional do Serrtão, ficando a disposição deste Juízo.  C. Grande, 18 de abril de 2013. Alberto Quaresma - Juiz de Direito.",
    "pena": null,
    "regime": null,
    "codigoCertidao": null
  }
}"""
# fileName = sys.argv[1]

# with open(fileName+".json", "r") as dataFile: 
data = json.loads(dataFile)


f = open("data02_1.xml", 'w', encoding='utf8')
dataXML = dicttoxml(data)
print(str(dataXML, 'utf-8'), file=f)
f.close()