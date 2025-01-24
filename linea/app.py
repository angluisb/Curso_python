from funciones import calcular_y



def main():
    m=2
    b=3
    X=[ x for x in range(1,11)]
    Y=[calcular_y(x,m,b) for x in X]
    print(f"Enteros:")
    cordenadas_enteros= list(zip(X,Y))
    print(cordenadas_enteros)
    

if __name__ == '__main__':
    main()