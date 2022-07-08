import os
def filtrar():
    letra= input("Digite la letra por la que empiezan los beneficiarios:").strip()
    print("Listado filtrado de beneficiarios:")
    with open("agenda.txt","r") as archivo:
        for linea in archivo:
            if linea[0].lower()== letra.lower():
                print(linea.strip())
                print(archivo.readline().strip())
                print(archivo.readline().strip())

    main()
def ver():
    print("Listado de beneficiarios:")
    with open("agenda.txt","r") as archivo:
        for linea in archivo:
            print(linea.strip())
    main()
def borrar():
    tupac=()
    cuaderno = "agenda.txt" + ".bak"
    cedula=input("Digite la cedula del beneficiario a borrar:")
    with open("agenda.txt","r+") as archivo,open(cuaderno,"w") as narchivo:
        for contador,linea in enumerate(archivo):
            if linea.strip() == cedula:
                tupac=((contador-1),contador,(contador+1))
        archivo.seek(0)
        for contador,linea in enumerate(archivo):
            if contador not in tupac:
                narchivo.write(linea)
    os.remove("agenda.txt")
    os.replace("agenda.txt.bak","agenda.txt")
    print("El usuario ha sido eliminado del listado.")
    main()
def añadir():
    centinela = "off"
    print("Digite la información del beneficiario a agregar:")
    nombre= input()+"\n"
    cedula= input()+"\n"
    celular= input()+"\n"
    with open("agenda.txt","a") as archivo:
            archivo.write(nombre)
            archivo.write(cedula)
            archivo.write(celular)
    print("El beneficiario ha sido agregado")

    main()
def buscartelefono():
    centinela = "off"
    nombre=input("Digite el nombre y apellido del beneficiario a buscar:")
    with open("agenda.txt","r") as archivo:
        for linea in archivo:
            if nombre in linea:
                centinela = "On"
                print(nombre)
                print(archivo.readline().strip())
                print(archivo.readline().strip())
    if centinela == "off":
        print("No se encuentra el beneficiario en la agenda.")
    main()
def crearagenda():
    with open("agenda.txt","w") as archivo:
        pass
def salir():
    print("Hasta pronto")
def main():
    funciones = [(6,salir),(4,buscartelefono),(3,añadir),(5,borrar),(1,ver),(2,filtrar)]
    print("Menu Principal" + "\n" + "1.Ver listado" + "\n" + "2.Ver listado filtrado" + "\n" +"3.Agregar beneficiario" + "\n" + "4.Buscar beneficiario"+"\n" + "5.Borrar beneficiario" + "\n"+ "6.Salir")
    eleccion = int(input())
    for i in funciones:
        if eleccion == i[0]:
            i[1]()
main()
