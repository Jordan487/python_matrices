Calcula el promedio de temperaturas para cada ciudad.

    Args:
        temperaturas (dict): Diccionario con las temperaturas de cada ciudad.

    Returns:
        dict: Diccionario con los promedios de temperatura de cada ciudad.
    """
    promedios = {}
    for ciudad, temps in temperaturas.items():
        promedio = sum(temps) / len(temps)
        promedios[ciudad] = promedio
    return promedios

# Datos de ejemplo (puedes modificarlos con tus datos reales)
temperaturas = {
    "Ciudad A": [25, 28, 30, 27],
    "Ciudad B": [22, 24, 26, 23],
    "Ciudad C": [31, 33, 35, 32]
}

# Calcular y mostrar los promedios
promedios_calculados = calcular_promedio_temperaturas(temperaturas)
print(promedios_calculados)
