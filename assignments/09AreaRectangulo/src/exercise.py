def areaRect(base,altura):
    totArea=base*altura
    return totArea

def main():
    b=float(input("Dame la base: "))
    a=float(input("Dame la altura: "))

    x=areaRect(b,a)
    print ("El área del rectángulo es:",x)
    pass

if __name__=='__main__':
    main()
