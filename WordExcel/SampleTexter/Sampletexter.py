from docx import Document
document= Document("Someword.docx")

for p in document.paragraphs:
    lista= p.text.split(" ")
    contador=0
    for i in lista:
        if i != "":
            lista[contador]="sampletext"
        contador+=1
    p.text=" ".join(lista)

document.save("Sampletext.docx")
