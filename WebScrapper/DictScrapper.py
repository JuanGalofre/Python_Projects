import requests
from bs4 import BeautifulSoup
def main():
    mode= input("Do you wish to translate 1.Spanish to German or 2.German to Spanish")
    
    if mode == "1":URL = "https://es.pons.com/traducción/español-alemán/"
    else: URL="https://es.pons.com/traducción/alemán-español/"
    word=input("Word to look for")
    URL= URL+word.strip()
    
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    
    flexion = soup.find("span",class_="flexion")
    wordclass= soup.find("span", class_="wordclass")
    dd= soup.find_all("dd", class_="dd-inner")
    
    if flexion == None:
        flexion="It does not have inflection available"

    definitionsList=[]
    for i in dd:
        definition=i.text.strip()
        definitionsList.append(definition)
        
    print(URL.split("/")[-1])
    try:
        print(wordclass.text +" "+flexion.text)
    except AttributeError:
        print(wordclass.text + " " + flexion)
    print(  "Spanish definition: "+ str(definitionsList[0]))

    again=input("Again (y/n)")
    if again == "y": main()
main()
