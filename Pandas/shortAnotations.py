import pandas as pd

df=pd.read_csv("LocatDB.csv")

"""

df.head()-> Para mirar las primeras 5 filas
df.tail() -> Para mirar las ultimas 5 filas


for c in df.columns():
    print(c)
-> Va a imprimir todos los nombres de las columnas. Al recorrerse con un ciclo se deduce que puede ser una, lista, pero para recorrerla como tal se utiliza
c=list(df.columns)

-> Para cambiar el orden del dataframe, lo que se puede hacer es cambiar el orden de esa lista. 
   En este caso la columnas son c, pero simplemente es la lista donde se tiene los nombres de las columnas
df=df.reindex(columns=c) 

-> Para eliminar algunas columnas del dataframe, se crea un nuevo , o la lista donde se tiene la lista de nombres de las columnas
df=df[c]

-> Para modificar el valor de una columna, en este caso un string.astype castea
df["nombreColumna"]=df["nombreColumna"].str.replace(r"loQueQueremosReemplazar","LoQueVaASerReemplazado").astype(float)

-> Concatenar DF,se concatenan con concat. Para mirar la longitud y comprobar que se concatenaron, se puede usar len(df.index), porque el index siempre va a tener algo. Aunque eso tambien 
   contaria lineas vacias en el caso de un excel. Yo me imagino que para poder concatenar, deberian tener las mismas columnas con los mismos nombres. Pero para eso se pueden editar ya sean 
   los nombres o el orden.
df2 = pd.read_csv("LocatDB2.csv") 
con_df=pd.concat([df1,df2]) 
len(df1.index)

-> Para hacer un dataframe mas pequeño, se puede hacer | para acceder a un dataframe solo con la dos columnas.
df[[columna1,,columna2]]

->Para acceder a un row, se utiliza df.iloc[numero del row]. Cuando solo se devuelve una columna o una fila, se devuelve series.

-> Cuando se accede a una columna df["column"], el indice va a ser el indice generico,vease 0,1,2,3,etc. Mientras que cuando se accede a la fila, el indice va a ser el nombre de la columna. Interesante
   para acceder a lo que se necesite.

-> Para acceder a multiple rows, se puede hacer df.iloc[[0,1]]. Donde se va a obtener un data frame, con el indice normal y las columnas. Ahora, unua implementación de df.iloc, es restringir
   las columnas que queremos. Se refieren las columnas con df.iloc[[0,1],2]. En ese caso, se van a sacar las rows 1 y 2 con la columna 2. Tambien se podria poner con df.loc[[0,1],"email"] 

-> Una vez recorrido una columna, para obtener el index de la columna se hace df[df["NombreColumna"]=="Lo que queremos buscar"].index.values. Este obtiene todas las coincidencias. Mientras que 
    df[df['Columna'] == dato].index[0] obtiene la primera coincidencia

-> Una vez recorrida una fila, para obtener la columna se hace df.iloc[2].index[df.iloc[2] == i][0]

-> at e iat son metodos de acceso para modificar valores de los dataframes. at utiliza fila como index y columna como string. iat utiliza las dos como index. Pero asi se puede modificar.
"""
