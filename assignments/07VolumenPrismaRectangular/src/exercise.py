
def main():
    #escribe tu código abajo de esta línea
    
    def areaPrisma (base,altura,profundidad):
        area=base*altura*profundidad
        return area

    def main():
        b=float(input("Dame la base: "))
        a=float(input("Dame la altura: "))
        p=float(input("Dame la profundidad: "))

        x=areaPrisma(b,a,p)
        print("El volumen del prisma es:",x)
    pass

if __name__=='__main__':
    main()
