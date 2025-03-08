import random  # Importamos la librería para generar números aleatorios

# Definimos las ciudades y días de la semana
ciudades = ["Quito", "Guayaquil"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2  # Número de semanas

# Creamos una matriz 3D con temperaturas aleatorias entre 10°C y 35°C
temperaturas = [[[random.randint(10, 35) for _ in range(7)] for _ in range(semanas)] for _ in range(len(ciudades))]

# Mostrar los datos generados
print("\n📌 Registro de temperaturas diarias:")
for i, ciudad in enumerate(ciudades):  # Recorremos las ciudades
    print(f"\nCiudad: {ciudad}")
    
    for semana in range(semanas):  # Recorremos las semanas
        print(f"  Semana {semana + 1}: {temperaturas[i][semana]}")  # Muestra las temperaturas diarias

# Calcular y mostrar el promedio de temperaturas por ciudad y semana
print("\n📊 Promedio de temperaturas:")
for i, ciudad in enumerate(ciudades):
    print(f"\nCiudad: {ciudad}")

    for semana in range(semanas):
        promedio = sum(temperaturas[i][semana]) / len(dias_semana)  # Calculamos el promedio
        print(f"  Semana {semana + 1}: Promedio de temperatura = {promedio:.2f}°C")  # Mostramos el resultado
