#Mi primer Archivo
#Ejercicio 1:
#print ('Hola mundo')

#Ejercicio 2:
#saludo = 'Hola mundo'
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

#n= 0
#m=0
#n=int(input('Ingrese un numero entero:'))
#m =int(input('Ingrese un numero entero:'))
#c= n//m
#print('El cociente de la division de estos dos numeros es:' + str(c))
#r= n%m 
#print('El resto de la divion de estos dos numeros es:' + str(r))
#if c<1:
 # print('El divisor es mayor al dividendo')
#i3f c>1:
 # print('El divisor es menor que el dividendo')
#if c==1:
 # print('El divisor y el dividendo son iguales')

#invertir=float(input('Digite la cantidad a invertir:'))
#interes=float(input('Digite el interes anual:'))
#años=int(input('Digite el numero de años:'))
#apital= (invertir*((interes//100)+1)**años)
#print(capital)
#if capital<100000:
 # print(str(capital)+'Baja rentabilidad')
#if 100000<capital>1000000:
 # print(str(capital)+'Rentabilidad moderada')
#if capital>1000000:
  #print(str(capital)+'Es una buena inversion')

#payasos= int(input('Digite cantidad de payasos vendidos en el ultimo pedido:'))
#muñecas= int(input('Digite cantidad de muñecas vendidos en el ultimo pedido:'))
#x=""
#pedido= ((112*payasos)+(75*muñecas))
#if pedido<30000:
 # print('El peso del pedido es:'+ str(pedido))
#if pedido>30000:
 # print('El peso del pedido es:'+ str(pedido))
#if pedido>30000:
 #x= input('Desea enviar este pedido:')
## print('Contenedor enviado')
#if x=='no':
 # print('Contenedor no enviado')

#dinero= float(input('Digite la cantidad de dinero que depositara:'))
#if 0<dinero>1000000

#num1= int(input('Dar un numero:'))
#num2= int(input('Dar un numero:'))
#def numeros(num1, num2):
 # return num1 + num2
#numero = numeros(num1, num2)
#print(numero)

#num1= int(input('Dar un numero:'))
#num2= int(input('Dar un numero:'))
#def numeros(x,y):
 # return num1 - num2
#numero = numeros(num1,num2)
#print(numero)

#num1= int(input('Dar un numero:'))
#num2= int(input('Dar un numero:'))
#def numeros(x,y):
 # return num1*num2
#numero = numeros(num1,num2)
#print(numero)


#num1= int(input('Dar un numero:'))
#num2= int(input('Dar un numero:'))
#x= num1
#y= num2
#def numeros(x,y):
 # return num1//num2
#if num2 ==0:
 # print('No es valido') 
#numero = numeros(num1,num2)
#print(numero)

#num1= int(input('Dar un numero:'))
#um2= int(input('Dar un numero:'))
#def numeros(num1, num2):
 # return num1 + num2
#numero = numeros(num1, num2)
#print(numero)

#num1= int(input('Dar un numero:'))
#num2= int(input('Dar un numero:'))
#def numeros(x,y):
 # return num1 - num2
#numero = numeros(num1,num2)
#print(numero)

#num1= int(input('Dar un numero:'))
#num2= int(input('Dar un numero:'))
#def numeros(x,y):
 # return num1*num2
#numero = numeros(num1,num2)
#print(numero)


#num1= int(input('Dar un numero:'))
#num2= int(input('Dar un numero:'))
#x= num1
#y= num2
#num1= int(input('Dar un numero:'))
#num2= int(input('Dar un numero:'))
#if num2 ==0:
 # print('No es valido') 
#numero = numeros(num1,num2)
#print(numero)


num1= x
num2 = y
operacion= input('Indique la operacion que desea:')
num1= float(input('Dar un numero:'))
num2= float(input('Dar un numero:'))
if operacion=='suma':
def numeros(x, y):
  return num1 + num2
if  operacion=='resta':
def numeros(x, y):
  return num1 - num2
if  operacion=='multiplicacion':
def numeros(x, y):
  return num1 * num2
if  operacion=='division':
def numeros(x, y):
  return num1 // num2