from bs4 import BeautifulSoup
import requests
import pandas as pd
import xlsxwriter
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
    return filas
lista=extractCityNames()
namesList=[]
numbersList=[]
departmentsList=[]
for i in lista:
    numbersList.append(i[0])
    namesList.append(i[1])
    departmentsList.append(i[2])
df = pd.DataFrame({'Numero': numbersList,
                   'Ciudad': namesList,
                   "Departamento" : departmentsList ,
                    })
writer = pd.ExcelWriter('ciudades.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()
