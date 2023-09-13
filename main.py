'''
Mi primer Archivo
Ejercicio 1:
print ('Hola mundo')

#Ejercicio 2:
saludo = 'Hola mundo'
print(saludo)

#Ejercicio 3:
nombre = input("Introduzca nombre de usuario: ")
print('Hola'+ nombre+'!')

#Ejercicio 4:
print(((3+2)/(2*5))**2)


#Ejercicio 5:
horas = float(input('Numero de horas trabajadas:'))
costo = float( input('Costo de hora de trabajo:'))
resultado= (horas*costo)
print(resultado)

#eJERCICIO 6
n= int(input('Ingrese un numero entero positivo:'))
print((n*(n+1))/2)

#Ejercicio 7
peso= input('Introduzca su peso(Kg):')
estatura = input('Introduzca su altura (m):')
imc = round(float(peso)/float(estatura)**2,2)
print('Tu indice de masa corporal es', imc)

#Ejercicio 8
print ('Ingrese dos numeros enteros')
n=  input('N:')
m= input('M:')
resultado= (float(n)// float(m))
residuo= (float(n) % float(m))
print('El cociente es:',resultado + 'y su residuo es:', residuo)

#Ejercicio 9
invertir= float(input('Ingrese cantidad a invertir:'))
interes= float( input('Ingrese interes anual:'))
años= float( input('Ingrese el numero de años:'))
Capital= round (invertir*((interes/100 + 1)**años),2)
print ('Su capital seria de:', Capital) 

#Ejercicio 10
payaso= float( imput('Digite el numero de payasos vendidos en el ultimo pedido:'))
muñeca= float( imput('Digite el numero de mueñcas vendidos en el ultimo pedido:'))
peso payaso= int( 112)
peso muñeca= int(75)
peso total= ((payaso * peso payaso) + (muñeca*peso muñeca))
print('El peso total es:', peso total)

#Ejercicio 11
numero=0
numero= int(input('Digite un numero entero:'))
suma= numero*(numero+1)/2
if suma>20:
 print(str(numero) + str(suma) +    '¡Que gran numero!')
if suma <20:
  print( str(suma))

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

invertir=float(input('Digite la cantidad a invertir:'))
interes=float(input('Digite el interes anual:'))
años=int(input('Digite el numero de años:'))
capital= (invertir*((interes//100)+1)**años)
print(capital)
if capital<100000:
  print(str(capital)+'Baja rentabilidad')
if 100000<capital>1000000:
  print(str(capital)+'Rentabilidad moderada')
if capital>1000000:
  print(str(capital)+'Es una buena inversion')

payasos= int(input('Digite cantidad de payasos vendidos en el ultimo pedido:'))
muñecas= int(input('Digite cantidad de muñecas vendidos en el ultimo pedido:'))
x=""
pedido= ((112*payasos)+(75*muñecas))
if pedido<30000:
  print('El peso del pedido es:'+ str(pedido))
if pedido>30000:
  print('El peso del pedido es:'+ str(pedido))
if pedido>30000:
 x= input('Desea enviar este pedido:')
 print('Contenedor enviado')
if x=='no':
  print('Contenedor no enviado')

dinero= float(input('Digite la cantidad de dinero que depositara:'))
if 0<dinero>1000000

num1= int(input('Dar un numero:'))
num2= int(input('Dar un numero:'))
def numeros(num1, num2):
  return num1 + num2
numero = numeros(num1, num2)
print(numero)

num1= int(input('Dar un numero:'))
num2= int(input('Dar un numero:'))
def numeros(x,y):
  return num1 - num2
numero = numeros(num1,num2)
print(numero)

num1= int(input('Dar un numero:'))
num2= int(input('Dar un numero:'))
def numeros(x,y):
  return num1*num2
numero = numeros(num1,num2)
print(numero)


num1= int(input('Dar un numero:'))
num2= int(input('Dar un numero:'))
x= num1
y= num2
def numeros(x,y):
  return num1//num2
if num2 ==0:
  print('No es valido') 
numero = numeros(num1,num2)
print(numero)

num1= int(input('Dar un numero:'))
num2= int(input('Dar un numero:'))
def numeros(num1, num2):
  return num1 + num2
numero = numeros(num1, num2)
print(numero)

num1= int(input('Dar un numero:'))
num2= int(input('Dar un numero:'))
def numeros(x,y):
  return num1 - num2
numero = numeros(num1,num2)
print(numero)

num1= int(input('Dar un numero:'))
num2= int(input('Dar un numero:'))
def numeros(x,y):
  return num1*num2
numero = numeros(num1,num2)
print(numero)


num1= int(input('Dar un numero:'))
num2= int(input('Dar un numero:'))
x= num1
y= num2
num1= int(input('Dar un numero:'))
num2= int(input('Dar un numero:'))
if num2 ==0:
  print('No es valido') 
numero = numeros(num1,num2)
print(numero)


num1= x
num2 = y
operacion= input('Indique la operacion que desea:')
num1= float(input('Dar un numero:'))
num2= float(input('Dar un numero:'))
if operacion=='suma':
def numeros(x,y):
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


#****
def intereses(inv):
  d= inv
  if (d>0 and d<1000000):
    return 2
  elif(d>=1000000 and d <2000000):
    return 5
  else:
    return 7

def calbalance(int, inv):
  n= int
  d= inv
  return round((d*(1+(n/100))), 2)

def ctahorro():
  #inversion,interes,b1,b2,b3=0.0
  inversion= float(input("Ingrese el valor de la inversion: "))
  interes= intereses (inversion)
  b1= calbalance(interes,inversion)
  b2=calbalance(interes, b1)
  b3= calbalance(interes, b2)
  print(" Balance 1: " + str(b1) + " Balance 2: " + str(b2) + " Balance 3: "+str(b3))

ctahorro()
'''
''''
def circulo(radio):
  return (3.14159*(radio**2))

def triangulo(base,altura):
 
  return ((base*altura)/2)

def cuadrado(lado):
  return (lado*lado)

def resultados():
  area= 0.0
  figura=""
  figura= input("Digite figura a calcular: ")
  if (figura.lower()=="triangulo"):
    b=0.0
    a=0.0
    b= float(input("Digite base del triangulo: "))
    a= float(input("Digite altura del triangulo: "))
    area= triangulo(b,a)
    print("El area del triangulo es:", area)

  if (figura.lower()=="circulo"):
    radio= 0.0
    radio= float(input("Digite el radio del circulo: "))
    area1= circulo(radio)
    print("El area del circulo es:", area1)

  if (figura.lower()=="cuadrado"):
    lado=0.0
    lado= float(input("Digite el lado del cuadrado: "))
    area= cuadrado(lado)
    print("El area del cuadrado es:", area)
  
resultados()
'''
''''
def maximo(a,b):
  if a>b:
    return a
  else:
    return b

def minimo(a,b):
  if a<b:
    return a
  else: 
    return b

#programa principal
x=int(input("un numero: "))
y=int(input("otro numero: "))
print(maximo(x-3,minimo(x+2,y-5)))
'''
''''
def descuentop (p):
  if p>=2000000:
    return (p+(p*0.10))

def descuentos (o):
  if o=="si":
    return (o+(o*0.5))
  if o=="no":
    return (p+(p*0.10))

def iva(n,r):
  n*0.20
  r*0.20
  
  
#principal

p= float(input("Digite el precio de su estereo:"))
resultado= descuentop(p)
o= input("¿La marca de su producto es NOSY?:")
resultado= descuentos(o)
'''
'''
def saludar():
  print("Hola")

saludar()


def suma(a,b):
  return a+b

suma(2,4)


#Año bisiesto 1.
def agno (a):
  if a%100 == 0:
    print("No lo es")
  elif a%4 == 0:
    print("Es bisiesto")
  elif a%400 == 0:
    print("Es bisiesto")
  else:
    print("No lo es")
    
a= int(input("Digite el año: "))
agno(a)


#Perros 2.
def perros(a,p):
  if a<= 30 and p< 15:
    print("Es un perro pequeno")
  elif 30<= a <=40 and 15<= p <= 25:
    print("Es un perro mediano")
  elif 40<= a <=60 and 25<= p <=45:
    print("Es un perro grande")

a= int(input("Digite la altura de su perro:"))
p= int(input("Digite el peso de su perro:"))
print (perros(a,p))



#Temperaturas 3.
def kel(v,o):
  if (cel):
    print(C = v - 273.15)
  elif (fah):
    print ( F = 1.8*(v - 273.15)+ 32)

def cel(v,o):
  if (kel):
    print( K = v + 273.15)
  elif (fah):
    print(f= (v-32) * 5/9)

def fah(v,o):
  if (cel):
    print(c= (v - 32) * 5/9)
  elif (kel):
    print(K = 5/9 (v - 32) + 273.15)

def principal():
v= int(input("Digite la temperatura:"))
escala= input("Digite la escala:")
if escala== Kelvin:
  kel(v,o)
elif escala== Celsius:
  cel(v,o)
elif escala== Fahrenheit:
  fah(v,o)

input("Digite la escala a la que desea llegar:")

principal()


def intereses(inv):
  d= inv
  if (d>0 and d<1000000):
    return 2
  elif(d>=1000000 and d <2000000):
    return 5
  elif (2000000<d):
    return 7

def balance(int, inv):
  n= int
  d= inv
  return round((d*(1+(n/100))), 2)

def cuenta():
  inversion= float(input("Ingrese el valor de la inversion: "))
  interes= intereses (inversion)
  a1= balance(interes,inversion)
  a2= balance(interes, a1)
  a3= balance(interes, a2)
  print(" Balance 1: " + str(a1) + " Balance 2: " + str(a2) + " Balance 3: "+str(a3))

cuenta()  

def porcentaje(w,z):

    return (w*(1+(z/100)))

 

w=int(input("Ingrese valor: "))

z=int(input("Ingrese porcentaje: "))

print(round(porcentaje(w-20000, z+2),2))

def jamon (com):
  n=com
  if (n==2):
    return 2
  elif (2<n<5):
    return 5
  elif (n>5):
    return 100

def arepas(com):
  return 3

#int=interes
def formula(com,int):
  n=com
  i=int
  return (n*(1+(i/100)))
  

def compras():
 int(input("¿Cuantos panes comprara?:"))
 int(input("¿Cuantos jamones comprara?:"))
 int(input("¿Cuantas arepas comprara?:"))


#Valor jamón: 7000
#Valor Arepas: 6000
#Valor pan tajado: 6500

  
a=0
while (a<=10):
  print(a)
  a=a+1


def suma(num1,num2):
  num1= int(input('Dar un numero:'))
  num2= int(input('Dar un numero:'))
def numeros(num1, num2):
  return num1 + num2
numero = numeros(num1, num2)
print(numero)

num1= int(input('Dar un numero:'))
num2= int(input('Dar un numero:'))
def numeros(x,y):
  return num1 - num2
numero = numeros(num1,num2)
print(numero)

num1= int(input('Dar un numero:'))
num2= int(input('Dar un numero:'))
def numeros(x,y):
  return num1*num2
numero = numeros(num1,num2)
print(numero)


num1= int(input('Dar un numero:'))
num2= int(input('Dar un numero:'))
x= num1
y= num2
def numeros(x,y):
  return num1//num2
if num2 ==0:
  print('No es valido') 
numero = numeros(num1,num2)
print(numero)

#######3###3###3#
def Menu():
  print("Calculadora
  1.Suma
  2.Resta
  3.Meltiplicacion
  4.Division
  5.Salir)

def suma():
  a= float(input("Ingrese primer numero a sumar:"))
  b= float(input("Ingrese segundo numero a sumar:")) 
  return a+b

def resta():
  c= float(input("Ingrese primer numero a restar:"))
  d= float(input("Ingrese segundo numero a sumar:"))
  return c-d

def multiplicacion():
  e= float(input("Ingrese primer numero a restar:"))
  f= float(input("Ingrese segundo numero a multiplicar:"))
  return e*f

def division():
   g= float(input("Ingrese primer numero a dividir:"))
   h= float(input("Ingrese segundo numero a dividir:"))
   if h==0:
     print("Error, division entre 0")
   else:
     return g/h
   
def calculadora():
    Menu()
    opcion=0

    while opcion!=5:
      opcion=int(input("Seleccione opcion"))
      if (opcion==1):
        print("La suma es:", suma())
      elif (opcion==2):
        print("La resta es:", resta())
      elif (opcion==3):
        print("La multiplicacion es:", multiplicacion())
      elif (opcion==4):
        print ("La division es:", division())
        
        
  

for c in range(1,10,3):
  print(c)


#ADIVINAR NUMERO 
import random
def adivina():
  numero = random.randint(1,100)
  adivinado = False
  
  while not adivinado:
    intento= int(input("Adivina el numero: "))
    if intento ==numero:
      print("¡Correcto! Has adivinado el numero.")
    elif intento<numero:
      print("El numero es mayor.")
    else:
      print("El numero es menor.")

adivina()


#Numero tabla multiplicar 
def numero():
  n= int(input("Digite su numero:"))
  for i in range(1,11):
    resultado =n*i
    print(n,"x",i,"=",resultado)

numero()
'''

#NUMERO FACTORIAL
def factorial():
  n= int(input("Ingrese un numero:"))
  factorial=1
  
  for i in range (1,n+1):
    factorial *=i
    
  print("El factorial de", n, "es", factorial)

factorial()




  

    
    
  
    
    
    
    
      
    


  
  

  




