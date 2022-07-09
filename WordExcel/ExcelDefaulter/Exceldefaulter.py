import pandas as pd
import random
import names as nm
from bs4 import BeautifulSoup
import requests
def randomDate():
    anio = 2012#random.randint(2001,2020)
    mes= 2#random.randint(1,12)
    if mes ==2:
        if anio%4 ==0 :
            if anio%100 !=0:
                dia = random.randint(1,29)
            elif anio%400 ==0:
                dia = random.randint(1,29)
        else:
            dia=random.randint(1,28)
    elif mes%2 == 0 and mes<8 :
        dia = random.randint(1,30)
    elif mes%2 != 0 and mes>7:
        dia = random.randint(1,30)
    else:
        dia= random.randint(1,31)
    hora= random.randint(0,24)
    minuto= random.randint(0,60)
    segundo = random.randint(0,60)
    return str(anio)+"/"+str(mes)+"/"+str(dia)+"  "+str(hora)+":"+str(minuto)+":"+str(segundo)
def extractCityNames():
    URL="https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Colombia"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find("table")
    filas=[]
    for fila in table.find_all("tr"):
        columna = fila.find_all("td")
        columnaTratada=[]
        for i in columna:
            columnaTratada.append(i.text.strip())
        if not columnaTratada:
            pass
        else:
            filas.append(columnaTratada)
    cities=[]
    for i in filas:
        cities.append(i[1])
    return cities
cities=extractCityNames()
dates=[]
values=[]
names=[]
document=[]
docnumber=[]
ref=[]
city=[]
contador=0
while contador<100:
    dates.append(randomDate())
    values.append(random.randint(0,10000000))
    names.append(nm.get_full_name())
    document.append("C.C")
    docnumber.append(random.randint(0,1000000000))
    ref.append(random.randint(100000,200000))
    city.append(random.choice(cities))
    contador +=1

dataFrame = pd.DataFrame({'Fecha': dates,
                          'Valor': values,
                          "Nombre" : names,
                          "Tipo de documento":document,
                          "Numero de documento": docnumber,
                          "Referencia" : ref,
                          "Ciudad" : city})
writer = pd.ExcelWriter('defaultexcel.xlsx', engine='xlsxwriter')
dataFrame.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()
