def es_bisiesto (year):
    if year%4==0:
        if year%100==0 and year%400==0:
            bisiesto=True
        elif year%100==0 and year%400!=0:
            bisiesto=False
        else:
            bisiesto=True
    else:
        bisiesto=False
    return bisiesto

def main():
    a=int(input())
    z=es_bisiesto(a)
    print(z)
    pass

if __name__=='__main__':
    main()
