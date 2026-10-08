# SIMULADOR DE COLA DE TRANSACCIONES

print("Simulador de cola de transacciones")

 # CONSTANTES DEL PROGRAMA

MAX_INTENTOS = 3
ESTADO_OK = "OK"
ESTADO_SIN_CONEXION = "SIN_CONEXION"


 # DATOS DE LAS TRANSACCIONES


transacciones = [
    {
        "id": 1,
        "cliente": "Juan",
        "monto": 50000,
        "estado_origen": ESTADO_OK
    },
    {
        "id": 2,
        "cliente": "Maria",  
        "monto": 75000,
        "estado_origen": ESTADO_SIN_CONEXION
    },
    {
        "id": 3,
        "cliente": "Pedro",
        "monto": 30000,
        "estado_origen": ESTADO_OK
    },
    {
        "id": 4,
        "cliente": "Ana",
        "monto": 45000,
        "estado_origen": ESTADO_SIN_CONEXION
    },
    {
        "id": 5,
        "cliente": "Carlos",
        "monto": 0,
        "estado_origen": ESTADO_OK
    },
    {
        "id": 6,
        "cliente": "Laura",
        "monto": 25000,
        "estado_origen": ESTADO_SIN_CONEXION
    },
    {
        "id": 7,
        "cliente": "Sofia",
        "monto": 90000,
        "estado_origen": ESTADO_OK
    },
    {
        "id": 8,
        "cliente": "David",
        "monto": 15000,
        "estado_origen": ESTADO_SIN_CONEXION
    },
    {
        "id": 9,
        "cliente": "Camila",
        "monto": 40000,
        "estado_origen": ESTADO_SIN_CONEXION
    },
    {
        "id": 10,
        "cliente": "Andres",
        "monto": 55000,
        "estado_origen": ESTADO_SIN_CONEXION
    }
]


      # Revisar los datos de una transacción

def revisar_transaccion(transaccion):
    if transaccion["monto"] <= 0:
        return "FALLA_NEGOCIO"

    if transaccion["cliente"] == "":
        return "FALLA_NEGOCIO"

    return "OK"

     # Procesar una transacción

def procesar_transaccion(transaccion):
    resultado = revisar_transaccion(transaccion)

    if resultado == "FALLA_NEGOCIO":
        print("ID:", transaccion["id"], "Intento: 1", "Resultado: FALLA_NEGOCIO")
        return "FALLA_NEGOCIO"

    if transaccion["estado_origen"] == ESTADO_OK:
        print("ID:", transaccion["id"], "Intento: 1", "Resultado: EXITOSA")
        return "EXITOSA"

    return "SIN_CONEXION"

# Hacer los intentos cuando no hay conexión

def hacer_intentos(transaccion):
    for intento in range(1, MAX_INTENTOS + 1):

        if transaccion["id"] % 2 == 0 and intento == 2:
            print("ID:", transaccion["id"], "Intento:", intento, "Resultado: EXITOSA")
            return "EXITOSA"

        if intento == MAX_INTENTOS:
            print("ID:", transaccion["id"], "Intento:", intento, "Resultado: FALLA_SISTEMA")
            return "FALLA_SISTEMA"

        print("ID:", transaccion["id"], "Intento:", intento, "Resultado: SIN_CONEXION")

       # Procesar las transacciones 

exitosas = 0
fallidas_negocio = 0
fallidas_sistema = 0
total_reintentos = 0

for transaccion in transacciones:
    resultado = procesar_transaccion(transaccion)

    if resultado == "EXITOSA":
        exitosas += 1

    elif resultado == "FALLA_NEGOCIO":
        fallidas_negocio += 1

    elif resultado == "SIN_CONEXION":
        resultado_intentos = hacer_intentos(transaccion)

        if resultado_intentos == "EXITOSA":
            exitosas += 1
            total_reintentos += 1

        else:
            fallidas_sistema += 1
            total_reintentos += 2     
    

        # Resumen final

total_transacciones = len(transacciones)
porcentaje_exito = (exitosas / total_transacciones) * 100

print()
print("RESUMEN")
print("Total de transacciones:", total_transacciones)
print("Exitosas:", exitosas)
print("Fallidas por negocio:", fallidas_negocio)
print("Fallidas por sistema:", fallidas_sistema)
print("Total de reintentos:", total_reintentos)
print("Porcentaje de éxito:", round(porcentaje_exito, 1), "%")