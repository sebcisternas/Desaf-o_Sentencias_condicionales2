ventas = {
 "Enero": 15000,
 "Febrero": 22000,
 "Marzo": 12000,
 "Abril": 17000,
 "Mayo": 81000,
 "Junio": 13000,
 "Julio": 21000,
 "Agosto": 41200,
 "Septiembre": 25000,
 "Octubre": 21500,
 "Noviembre": 91000,
 "Diciembre": 21000,
}

umbral = int(input("Ingrese el valor del umbral = "))

ventasUmbral={key:value for key,value in ventas.items() if value>umbral}

print("Estos son los Meses que superan el umbral especificado")

print(ventasUmbral)