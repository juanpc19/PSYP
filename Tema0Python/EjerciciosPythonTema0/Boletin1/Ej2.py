#variable numero1, asigno siguiente valor introducido por teclado con input (el cual acompaño de mensaje por pantalla para usuario) y aplico cast al input a recibir 
numero1=int(input("Asigne valor a numero 1:"))

#variable numero2, asigno siguiente valor introducido por teclado con input (el cual acompaño de mensaje por pantalla para usuario) y aplico cast al input a recibir 
numero2=int(input("Asigne valor a numero 2:"))

#if condicion, se cierra con ":"
if numero1==numero2:
    print ("Los numeros son iguales.")
#elif condicion, se cierra con ":"
elif numero1>numero2:
    print (numero2, numero1)
#else tambien se cierra con ":"
else:
    print (numero1, numero2)