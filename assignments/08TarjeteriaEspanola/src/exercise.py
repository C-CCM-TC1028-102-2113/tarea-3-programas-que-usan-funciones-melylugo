def tarjeteria(albanene,plumones):
    Tpliegos=albanene*12
    Tplumones=plumones*35
    if Tpliegos<=Tplumones:
        return Tpliegos
    elif Tplumones<=Tpliegos:
        return Tplumones
    
def main():
    a=int(input("Dame la cantidad de pliegos de papel albanene: "))
    p=int(input("Dame la cantidad de plumones: "))

    x=tarjeteria(a,p)
    print ("El número máximo de tarjetas que se pueden hacer es:",x)
    pass

if __name__=='__main__':
    main()
