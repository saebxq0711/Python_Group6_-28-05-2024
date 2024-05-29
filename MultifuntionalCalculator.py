def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero."
    return a / b

def decimal_a_binario(decimal):
    return bin(decimal)[2:]

def binario_a_decimal(binario):
    return int(binario, 2)

def conversion_temperatura(celsius):
    return celsius * 9/5 + 32

def calcular_imc(peso, altura):
    return  (altura**2) / peso 

def conversion_cm_mt(cm):
    return cm / 100

def conversion_mt_cm(mt):
    return mt * 100

def conversion_mt_km(mt):
    return mt / 1000

def conversion_km_mt(km):
    return km * 1000

def conversion_segundos_minutos(segundos):
    return segundos / 60

def conversion_minutos_horas(minutos):
    return minutos / 60

def conversion_horas_minutos_y_segundos(horas):
    minutos = int(horas % 60)
    horas = int(horas // 60)
    return f"{horas} horas y {minutos} minutos"

print("Estas son las calculadoras disponibles:")
print("1: Calculadora básica (Suma, Resta, Multiplicación, División)")
print("2: Operaciones Numéricas (Decimal a binario, Binario a decimal)")
print("3: Conversión de temperatura (Celsius a Fahrenheit)")
print("4: Calcular IMC")
print("5: Conversión de unidades de medida (cm a mt, mt a cm, mt a km, km a mt)")
print("6: Conversión de unidades de tiempo (Segundos a minutos, minutos a horas, horas a minutos y segundos)")

calculadora_seleccionada = int(input("Seleccione la calculadora que desea usar: "))

if calculadora_seleccionada == 1:
    operacion_basica = input("Seleccione la operación: \n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir\n")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if operacion_basica == 1:
        print(f"Resultado: {suma(num1, num2)}")
    elif operacion_basica == 2:
        print(f"Resultado: {resta(num1, num2)}")
    elif operacion_basica == 3:
        print(f"Resultado: {multiplicacion(num1, num2)}")
    elif operacion_basica == 4:
        print(f"Resultado: {division(num1, num2)}")
    elif operacion_basica == 5:
        print("Finalizado")
    else:
        print("Opción no válida.")

elif calculadora_seleccionada == 2:
    operacion_numerica = input("Seleccione la operación: \n1. Decimal a binario\n2. Binario a decimal\n")
    if operacion_numerica == '1':
        decimal = int(input("Ingrese el número decimal: "))
        print(f"Binario: {decimal_a_binario(decimal)}")
    elif operacion_numerica == 2:
        binario = input("Ingrese el número binario: ")
        print(f"Decimal: {binario_a_decimal(binario)}")
    else:
        print("Opción no valida.")

elif calculadora_seleccionada == 3:
    
    celcius = float(input("Ingrese la temperatura en grados Celcius: ")) 
    print(f"Temperatura en Fahrenheit: {conversion_temperatura(celcius)}")
                     
elif calculadora_seleccionada == 4:
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Su IMC es: {imc:.2f}")

elif calculadora_seleccionada == 5:
    conversion_unidades = input("Seleccione la conversión: \n1. cm a mt\n2. mt a cm\n3. mt a km\n4. km a mt\n")

    if conversion_unidades == '1':
        cm = float(input("Ingrese la cantidad en centímetros: "))
        print(f"{cm} cm = {conversion_cm_mt(cm)} mt")
    elif conversion_unidades == '2':
        mt = float(input("Ingrese la cantidad en metros: "))
        print(f"{mt} mt = {conversion_mt_cm(mt)} cm")
    elif conversion_unidades == '3': 
        mt = float(input("Ingrese la cantidad en metros: "))
        print(f"{mt} mt = {conversion_mt_km(mt)} km") 
    elif conversion_unidades == '4': 
        km = float(input("Ingrese la cantidad en kilómetros: "))
        print(f"{km} km = {conversion_km_mt(km)} mt")
    else:
        print("Opción Inválida")
        
if calculadora_seleccionada == 6:
    conversion_tiempo = input("Seleccione la conversión: \n1. Segundos a minutos\n2. Minutos a horas\n3. Horas a minutos y segundos\n")
    if conversion_tiempo == '1':
        segundos = float(input("Ingrese la cantidad en segundos: "))
        print(f"{segundos} segundos = {conversion_segundos_minutos(segundos)} minutos")
    elif conversion_tiempo == '2':
        minutos = float(input("Ingrese la cantidad en minutos: "))
        print(f"{minutos} minutos = {conversion_minutos_horas(minutos)} horas") 
    elif conversion_tiempo == '3':
        horas = float(input("Ingrese la cantidad en horas:"))
        print(f"{horas} horas = {conversion_horas_minutos_y_segundos(horas)} minutos y segundos")
    else:
        print("Opción Inválida")
    
