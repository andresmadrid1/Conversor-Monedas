# The program is initialized
from pickletools import read_uint1


print("Hola bienvenido a nuestro programa de conversion de monedas coinKey")
print("Estas son las tazas de conversion que tenemos disponibles de acorde al mercado: ")
print('')
print('Pesos Colombianos')
print('dolar')
print('euro')
print('')
# Function which allows to calcule the currency convertion value
def moneda_conversion_destino(tipo_moneda,tipo_moneda_destino,cantidad_monedas):
    if(tipo_moneda == 'dolar' and tipo_moneda_destino == 'pesos colombianos'):
        pesos = cantidad_monedas * 3742.67
        pesos = round(pesos, 2)
        print("De acuerdo a la taza de conversion actual tienes " + str(pesos) + " Pesos Colombianos")
        return

    if(tipo_moneda == 'dolar' and tipo_moneda_destino == 'euros'):
        pesos = cantidad_monedas * 0.92
        pesos = round(pesos, 2)
        print("De acuerdo a la taza de conversion actual tienes " + str(pesos) + " euros")
        return

    if(tipo_moneda == 'pesos colombianos' and tipo_moneda_destino == 'dolar'):
        pesos = cantidad_monedas * 0.00027  
        pesos = round(pesos, 2)
        print("De acuerdo a la taza de conversion actual tienes " + str(pesos) + " dolares")
        return

    if(tipo_moneda == 'pesos colombianos' and tipo_moneda_destino == 'euros'):
        pesos = cantidad_monedas * 0.00025 
        pesos = round(pesos, 2)
        print("De acuerdo a la taza de conversion actual tienes " + str(pesos) + " euros")
        return

    if(tipo_moneda == 'euro' and tipo_moneda_destino == 'pesos colombianos'):
        pesos = cantidad_monedas * 4061.86 
        pesos = round(pesos, 2)
        print("De acuerdo a la taza de conversion actual tienes " + str(pesos) + " pesos colombianos")
        return

    if(tipo_moneda == 'euro' and tipo_moneda_destino == 'dolar'):
        pesos = cantidad_monedas * 1.08 
        pesos = round(pesos, 2)
        print("De acuerdo a la taza de conversion actual tienes " + str(pesos) + " dolares")
        return

    else:
        print("No es posible hacer la conversión por favor escoja una moneda valida distinta a la original")
        return

# Function which allows to get the currency convertion value original
def moneda_conversion_original(tipo_moneda):
    if(tipo_moneda == 'dolar'):
        cantidad_monedas = float(input("¿Cuantos dolares tienes?: "))
        #print(str(cantidad_monedas))
        tipo_moneda_destino = input("A cual moneda desea realizar la conversion?: ").lower()
        moneda_conversion_destino(tipo_moneda,tipo_moneda_destino,cantidad_monedas)
        return
    if(tipo_moneda == 'pesos colombianos'):
        cantidad_monedas = float(input("¿Cuantos pesos tienes?: "))
        #print(str(cantidad_monedas))
        tipo_moneda_destino = input("A cual moneda desea realizar la conversion?: ").lower()
        moneda_conversion_destino(tipo_moneda,tipo_moneda_destino,cantidad_monedas)
        return
    if(tipo_moneda == 'euro'):
        cantidad_monedas = float(input("¿Cuantos euros tienes?: "))
        #print(str(cantidad_monedas))
        tipo_moneda_destino = input("A cual moneda desea realizar la conversion?: ").lower()
        moneda_conversion_destino(tipo_moneda,tipo_moneda_destino,cantidad_monedas)
        return
    else:
        print("Lo siento no tenemos la taza de conversion que busca para " + tipo_moneda)

# The program ask the user for type of currency      
tipo_moneda = input("Por favor escoja que tipo de moneda desea evaluar: ").lower()
moneda_conversion_original(tipo_moneda)


