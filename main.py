"""
print("Hola")
"""
"""
var1 = input("texto uno:")
varint = 12334

print(f"{var1} - {str(varint)}")

insertText = input("el texto que mostrara si es diferente de 0")

insertNumber = int(input("ingresa numero: "))

if insertNumber == 0:
    print("Valor es: " + str(insertNumber))
else: 
    print("el valor es diferente de 0 por lo tanto " + insertText)
"""
#funciones
"""
insertText = input("el texto que mostrara si es diferente de 0 ")

var_insertNumber = int(input("ingresa numero: "))

def insertarNumero(insertNumber):
    resultado = ""

    if insertNumber == 0:
        resultado = "Valor es: " + str(insertNumber)

    elif insertNumber >= 12 :
        resultado = insertNumber 
    else: 
        resultado = "el valor es diferente de 0 por lo tanto " + insertText

    return resultado

print(insertarNumero(var_insertNumber))
"""
#listas
personas = ["uno","dos","tres"]
dato = int(input("Que numero de persona quieres ver 1, 2 o 3? "))

print(personas[(dato - 1)])

for persona in personas:
    print("-" + persona)