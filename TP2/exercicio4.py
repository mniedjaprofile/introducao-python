def tabuada():
    """
    Exibe a tabuada dos números de 1 a 10.
    """
    for numero in range(1, 11): 
        print(f"\nTabuada de {numero}:")
        print("-" * 15)
        
        for multiplicador in range(1, 11):  
            resultado = numero * multiplicador
            print(f"{numero} x {multiplicador} = {resultado}")
        
        print("-" * 15)  

tabuada()
