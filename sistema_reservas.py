
print("Reservas Del Hotel")
habitaciones = 0


nombre = input(str("Ingrese su nombre completo: "))
identi = int(input("Ingrese su numero de identificacion: "))

print("El Hotel Cuenta Con 10 Habitacones distribuidas ")
habitaciones = 1 (int(input("marca 1 para seleccionar la habitacion: ")))

print("habitacion 1, habitaion 2, habitacion 3, habitacion 4,, habitacion 5, habitacion 6, habitacin 7, habitacion 8, habitacion 9, habitacion 10 ")
habitaciones = int(input("Ingrese el numero de la habitacion que desea: "))

if habitaciones == 2 or habitaciones == 3 or habitaciones == 4 or habitaciones == 5 or habitaciones == 6 or habitaciones == 7 or habitaciones == 8 or habitaciones == 9 or habitaciones == 10:
     print("habitacion disponible ")

else:
     print("habitacion no disponible ")


mes_entrada = str (input ("Ingresar mes de entrada: "))
dia_entrada = int (input ("Ingresar el dia de la entrada: "))
hora_entrada = int (input ("Ingresar hora de la entrada por la mañana: "))

mes_salida= str (input ("Ingresar mes de salida: "))
dia_salida = int (input ("Ingresar el dia de la salida: "))
hora_salida = int (input ("Ingresar hora de la salida por la mañana: "))

print ("Reserva lista")
print ("Recibo")

print ("la persona",nombre,"con identificacion numero",identi,"ha reservado la habitacion numero",habitaciones,)
print ("El horario de ENTRADA establecido es: MES ", mes_entrada, " DIA ", dia_entrada , " HORA ", hora_entrada,"A.M" )
print ("El horario de SALIDA establecido es: MES ", mes_salida, " DIA ", dia_salida , " HORA ", hora_salida,"A.M" )