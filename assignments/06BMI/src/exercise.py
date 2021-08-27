def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    print(calcula_indice(peso,altura))

def calcula_indice(a,b):
    if a>0 and b>0:
        imc=a/b**2
        if imc<20:
            indice="PESO BAJO"
        elif imc>=20 and imc<25:
            indice="NORMAL"
        elif imc>=25 and imc<30:
            indice="SOBREPESO"
        elif imc>=30 and imc<40:
            indice="OBESIDAD"
        elif imc>=40:
            indice="OBESIDAD MORBIDA"
    else:
        indice="Revisa tus datos, alguno de ellos es erróneo."
    return indice



if __name__=='__main__':
    main()