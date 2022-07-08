import requests as req
from bs4 import BeautifulSoup

lista_de_peticiones=[]
lista_de_urls=[]
lista_de_traducciones=[]
senna="off"

while senna=="off":
    peticion=input("Ingrese las palabras")
    if peticion == "0":
        senna="on"
    else:
        lista_de_peticiones.append(peticion)

for i in lista_de_peticiones:
    url="https://es.pons.com/traducción/alemán-español/" + i
    lista_de_urls.append(url)

for i in lista_de_urls:
    print(i)
    r= req.get(i)
    contenido_web = BeautifulSoup(r.text, 'lxml')
    Palabra =contenido_web.find("div", attrs={'class':'rom first'})
    Palabra2=Palabra.find("h2")
    traduccion=[]
    for i in Palabra2:
        a=i.string
        if isinstance(a,str) == False or bool(a)== False or a== ' ' or "\n" in a.strip():
            pass
        else:
            traduccion.append((a.strip()))


    f=Palabra.find("dd")
    g=f.find("a")
    traduccion.append(g.string)

    lista_de_traducciones.append(",".join(traduccion))
for i in lista_de_traducciones:
    print(i)
