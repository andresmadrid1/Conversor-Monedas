# The program is initialized
from pickletools import read_uint1


# Function which allows to calcule the currency convertion value
def moneda_conversion_destino(tipo_moneda,tipo_moneda_destino,cantidad_monedas):
    if(tipo_moneda == 2 and tipo_moneda_destino == 1):
        pesos = cantidad_monedas * 3742.67
        pesos = round(pesos, 2)
        print("De acuerdo a la taza de conversion actual tienes " + str(pesos) + " Pesos Colombianos")
        

    elif(tipo_moneda == 2 and tipo_moneda_destino == 2):
        pesos = cantidad_monedas * 0.92
        pesos = round(pesos, 2)
        print("De acuerdo a la taza de conversion actual tienes " + str(pesos) + " euros")
        

    elif(tipo_moneda == 1 and tipo_moneda_destino == 1):
        pesos = cantidad_monedas * 0.00027  
        pesos = round(pesos, 2)
        print("De acuerdo a la taza de conversion actual tienes " + str(pesos) + " dolares")
        

    elif(tipo_moneda == 1 and tipo_moneda_destino == 2):
        pesos = cantidad_monedas * 0.00025 
        pesos = round(pesos, 2)
        print("De acuerdo a la taza de conversion actual tienes " + str(pesos) + " euros")
        

    elif(tipo_moneda == 3 and tipo_moneda_destino == 1):
        pesos = cantidad_monedas * 4061.86 
        pesos = round(pesos, 2)
        print("De acuerdo a la taza de conversion actual tienes " + str(pesos) + " pesos colombianos")
        

    elif(tipo_moneda == 3 and tipo_moneda_destino == 2):
        pesos = cantidad_monedas * 1.08 
        pesos = round(pesos, 2)
        print("De acuerdo a la taza de conversion actual tienes " + str(pesos) + " dolares")
        

    else:
        print("No es posible hacer la conversión por favor escoja una moneda valida distinta a la original")
        
###################################################################################################################
# Function which allows to get the currency convertion value original
def moneda_conversion_original(tipo_moneda):

    if(tipo_moneda == 1):     
        cantidad_monedas = float(input("¿Cuantos pesos tienes?: "))
        menu = """ 
Taza de conversion: 

1 - dolar
2 - euro 

Por favor escoja el numero de moneda a la cual desea realizar la conversion: """
        tipo_moneda_destino = int(input(menu))
        moneda_conversion_destino(tipo_moneda,tipo_moneda_destino,cantidad_monedas)
        

    elif(tipo_moneda == 2):
        cantidad_monedas = float(input("¿Cuantos dolares tienes?: "))
        menu = """ 
Taza de conversion: 

1 - Pesos Colombianos
2 - euro 

Por favor escoja el numero de moneda a la cual desea realizar la conversion: """
        tipo_moneda_destino = int(input(menu))
        moneda_conversion_destino(tipo_moneda,tipo_moneda_destino,cantidad_monedas)
        

    elif(tipo_moneda == 3):
        cantidad_monedas = float(input("¿Cuantos euros tienes?: "))
        menu = """ 
Taza de conversion: 

1 - Pesos Colombianos
2 - dolar

Por favor escoja el numero de moneda a la cual desea realizar la conversion: """
        tipo_moneda_destino = int(input(menu))
        moneda_conversion_destino(tipo_moneda,tipo_moneda_destino,cantidad_monedas)
        

    else:
        print("Lo siento no tenemos la taza de conversion que busca para " + tipo_moneda)

###################################################################################################################
# The program ask the user for type of currency      
menu = """ 
Hola bienvenido a nuestro programa de conversion de monedas coinKey 💰💰💰
Estas son las tazas de conversion que tenemos disponibles de acorde al mercado: 

1 - Pesos Colombianos
2 - dolar
3 - euro 

Por favor escoja el numero de moneda desea evaluar: """
tipo_moneda = int(input(menu))
print(str(tipo_moneda))
moneda_conversion_original(tipo_moneda)



