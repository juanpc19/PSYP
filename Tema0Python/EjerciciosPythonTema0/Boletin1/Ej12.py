#no hay que indicar tipo parametro entrada en python
def calculadora(num1,num2,operacion):
    resultado=0
    
    if operacion==1:
        resultado=num1+num2
    elif operacion==2:
        resultado=num1-num2
    elif operacion==3:
        resultado=num1*num2
    elif operacion==4:
        resultado=num1/num2
        
    return resultado

