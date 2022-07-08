import math as mt
import os.path as pt

def laburoconproteina(atomodeseado):

    file=open(r"C:\Users\Juan Galofre\Desktop\Computacional\Archivos Comp\Proteina_sin_ligandos.pdbqt","r")
    listacercanos=[]
    for i in file:
        a=i.split()
        if "ATOM" in a:
            operacion = mt.sqrt(((float(a[6])-float(atomodeseado[0]))**2)+((float(a[7])-float(atomodeseado[1]))**2)+((float(a[8])-float(atomodeseado[2]))**2))
            if operacion<= 5:
                listacercanos.append(a)
    file.close()
    if pt.exists("cercanos.txt") == True:
        file=open("cercanos.txt","a")
        for i in listacercanos:
            a = " ".join(i)
            file.write(a+"\n")
        file.close
    else:
        file=open("cercanos.txt","x")
        file.close
        file=open("cercanos.txt","a")
        for i in listacercanos:
            a=" ".join(i)
            file.write(a+"\n")
        file.close()

#Se abre el archivo que contiene el ligando
def analisis_de_ligando(path):
    file=open("r"+path,"r")
    lista=[]
    senna=False
    while senna==False:
        a=file.readline()
        if "MODEL" in a:
            lista.append(a)
        elif( "ENDMDL" in a):
            senna=True
        elif "REMARK" in a:
            pass
        else:
            list.append(a)
    file.close()
    listaarreglada=[]
    for i in lista:
        listaarreglada.append(i.split())
    atomodeseado=None
    partedelaproteina=None
    promediogen=False
    residuo="N49"
    x=0
    y=0
    z=0
    c=0
    if promediogen ==True:
        for i in listaarreglada:
            if "HETATM" in i:
                x+=float(i[6])
                y+=float(i[7])
                z+=float(i[8])
                c+=1
        xprom = x / c
        yprom = y / c
        zprom = z / c
        atomodeseado = (xprom, yprom, zprom)
    else:

        for i in listaarreglada:
            if "HETATM" in i:
                atomodeseado=(i[6],i[7],i[8])
                laburoconproteina(atomodeseado)
    file=open("cercanos.txt","r")
    listaorganizada=[]
    strsalida=""
    for i in file:
        a= i.split()
        if {a[3]:a[5]} not in listaorganizada:
            listaorganizada.append({a[3]:a[5]})
            strsalida+=a[3]+a[5]+","
    print(strsalida)
    print(listaorganizada)
