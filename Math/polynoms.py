import math
import random
import time
def index_first_letter(chain):
    rta=None
    exceptions=[".","e","-"]
    for i in range(len(chain)):
        if chain[i] not in exceptions:
            try:
                int(chain[i])
            except ValueError:
                rta=i
                break
    return rta


def polynom_generator(grade) -> list:
    poly=[]
    number_list=range(100)

    for i in range(grade+1):
        if i==0:
            ran_number=random.choice(number_list)
            poly.append(ran_number)
        else:
            letter=i*"x"
            ran_number=str(random.choice(number_list))
            poly.append((ran_number+letter))
    return poly


def list_handler(nested) -> list:
    rta_list=[]
    for i in nested:
        for j in i:
            rta_list.append(j)
    return rta_list


def polynom_sizer(sequence) -> int:
    recorder=[]
    size=0
    whitelist= set("x")
    for contador, i in enumerate(sequence):
        if isinstance(i,str):
            if "x" in i:
                value=''.join([c for c in i if c in whitelist])
                if value not in recorder:
                    recorder.append(value)
                else:
                    size=contador
                    break
        else:
            recorder.append("c")
    return size-1


def polynom_mod(polynom_list)-> list:
    for value_1,i in enumerate(polynom_list):
        for value_2,j in enumerate(i):
            if isinstance(j,str):
                if any(k.isdigit() for k in j) == False:#alternative option isalpha()
                    polynom_list[value_1][value_2]="1"+j
    return polynom_list

def depolyfier(polyfied_polynom):
    polynom=[]
    for i in polyfied_polynom:
        num=i[0]
        if i[1]:
            num=str(num)
            letter=i[1]
            polynom.append((num+letter))
        else:
            polynom.append(num)
    return polynom


def polynomial_multiplication(polynom_list) -> list:#args version, Only multiplies two polynoms
    if isinstance(polynom_list[0],list):
        polynom1_size=len(polynom_list[0])
        polynom2_size=len(polynom_list[1])
        args=list_handler(polynom_list)
    modified_args=[]
    for i in args:
        if not isinstance(i,str):
            modified_args.append((i,""))
        else:
            index=index_first_letter(i)
            modified_args.append((float(i[0:index]),i[index:len(i)]))
    print(modified_args)
    raw_multiplications=[]
    for i in range(polynom1_size):
        for j in range(polynom2_size):
            numeric=modified_args[i][0]*modified_args[((polynom1_size+j))][0]
            letters=modified_args[i][1]+modified_args[((polynom1_size+j))][1]
            raw_multiplications.append((numeric,letters))
    degrees=[]
    for i in raw_multiplications:
        if i[1] not in degrees:
            degrees.append(i[1])
    result=[]
    for i in degrees:
        tracker=0
        for j in raw_multiplications:
            if j[1]==i:
                tracker+=j[0]
        if tracker != 0:
            result.append((tracker,i))

    return result

def main_polynom(mode=0):
    if mode==0:
        polynom_list=[]
        senna=True
        while senna == True:
            polynom= input("Please insert the polynom separated by , .To finish, use 0")
            if "," in polynom:
                result=polynom.split(",")
                for i in range(len(result)):
                    if not result[i]:
                        result.pop(i)
                    elif "x" not in result[i]:

                        result[i]=float(result[i])
                    elif "^" in result[i]:
                        index=result[i].index("^")
                        try:
                            new_x=result[i][index-1]*int(result[i][index+1])
                        except ValueError:
                            print("No fractional values are accpeted")
                            main_polynom()
                        result[i]=new_x
                polynom_list.append(result)
            else:
                senna=False
    else:
        pass
    polynom_list=polynom_mod(polynom_list)
    short_list=[polynom_list[0],polynom_list[1]]
    result_poly=depolyfier(polynomial_multiplication(short_list))
    polynom_list.pop(0)
    polynom_list.pop(0)
    if polynom_list:
        for i in polynom_list:
            short_list=[result_poly,i]
            result_poly=depolyfier(polynomial_multiplication(short_list))

    print(result_poly)
main_polynom()
#Generate random Polynoms: polynom_generator()
