#Mi primer Archivo
#Ejercicio 1:
#print ('Hola mundo')

#Ejercicio 2:
saludo = 'Hola mundo'
#print(saludo)

#Ejercicio 3:
#nombre = input("Introduzca nombre de usuario: ")
#print('Hola'+ nombre+'!')

#Ejercicio 4:
#print(((3+2)/(2*5))**2)


#Ejercicio 5:
#horas = float(input('Numero de horas trabajadas:'))
#costo = float( input('Costo de hora de trabajo:'))
#resultado= (horas*costo)
#print(resultado)

#eJERCICIO 6
#n= int(input('Ingrese un numero entero positivo:'))
#print((n*(n+1))/2)

#Ejercicio 7
#peso= input('Introduzca su peso(Kg):')
#estatura = input('Introduzca su altura (m):')
#imc = round(float(peso)/float(estatura)**2,2)
#print('Tu indice de masa corporal es', imc)

#Ejercicio 8
#print ('Ingrese dos numeros enteros')
#n=  input('N:')
#m= input('M:')
#resultado= (float(n)// float(m))
#residuo= (float(n) % float(m))
#print('El cociente es:',resultado + 'y su residuo es:', residuo)

#Ejercicio 9
#invertir= float(input('Ingrese cantidad a invertir:'))
#interes= float( input('Ingrese interes anual:'))
#años= float( input('Ingrese el numero de años:'))
#Capital= round (invertir*((interes/100 + 1)**años),2)
#print ('Su capital seria de:', Capital)

#Ejercicio 10
#payaso= float( imput('Digite el numero de payasos vendidos en el ultimo pedido:'))
#muñeca= float( imput('Digite el numero de mueñcas vendidos en el ultimo pedido:'))
#peso payaso= int( 112)
#peso muñeca= int(75)
#peso total= ((payaso * peso payaso) + (muñeca*peso muñeca))
#print('El peso total es:', peso total)

#Ejercicio 11
#numero=0
#numero= int(input('Digite un numero entero:'))
#suma= numero*(numero+1)/2
#if suma>20:
 #print(str(numero) + str(suma) +    '¡Que gran numero!')
#if suma <20:
 # print( str(suma))

n= 0
m=0
n=int(input('Ingrese un numero entero:'))
m =int(input('Ingrese un numero entero:'))
c= n//m
print('El cociente de la division de estos dos numeros es:' + str(c))
r= n%m
print('El resto de la divion de estos dos numeros es:' + str(r))
if c<1:
  print('El divisor es mayor al dividendo')
if c>1:
  print('El divisor es menor que el dividendo')
if c==1:
  print('El divisor y el dividendo son iguales')