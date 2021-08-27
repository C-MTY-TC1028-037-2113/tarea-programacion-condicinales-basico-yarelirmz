
def main():
    edad = int(input("Ingresa tu edad: "))
    if edad>0:
        if edad>=18:
            idoficial=str(input("¿Tienes identificación oficial? (s/n): "))
            if (idoficial=="s") or (idoficial=="S"):
                print("Trámite de licencia concedido")
            elif (idoficial=="n" or idoficial=="N"):
                print("No cumples requisitos")
            else:
                print("Respuesta incorrecta")
        else:
            print("No cumples requisitos")
    else:
        print("Respuesta incorrecta")





if __name__ == '__main__':
    main()
