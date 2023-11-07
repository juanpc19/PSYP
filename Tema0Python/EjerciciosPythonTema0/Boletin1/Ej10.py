#no hay que indicar tipo parametro entrada en python
def maximo(num1,num2):
    max=0
    
    if num1>num2:
        max=num1
    elif num2>num1:
        max=num2
    else:
        print("Los numeros son iguales")
    
    return max