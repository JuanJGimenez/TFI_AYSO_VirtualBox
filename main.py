# conversor_temperaturas.py
# Conversor de temperaturas: Celsius -> Fahrenheit y Kelvin
# Trabajo Práctico Integrador - Arquitectura y Sistemas Operativos
# UTN - Tecnicatura Universitaria en Programación a Distancia

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_a_kelvin(c):
    return c + 273.15

def mostrar_resultado(celsius, fahrenheit, kelvin):
    print("-" * 35)
    print(f"  Celsius    : {celsius:.2f} °C")
    print(f"  Fahrenheit : {fahrenheit:.2f} °F")
    print(f"  Kelvin     : {kelvin:.2f} K")
    print("-" * 35)

# Lista de temperaturas ingresadas por el usuario
temperaturas = []

print("=" * 35)
print("   CONVERSOR DE TEMPERATURAS")
print("=" * 35)
print("Ingresá 3 valores en grados Celsius:")
print()

for i in range(3):
    entrada = input(f"  Temperatura {i+1}: ")
    celsius = float(entrada)
    temperaturas.append(celsius)

print("\n--- Resultados de conversión ---")
for temp in temperaturas:
    f = celsius_a_fahrenheit(temp)
    k = celsius_a_kelvin(temp)
    mostrar_resultado(temp, f, k)

# Calcular y mostrar el promedio
promedio = sum(temperaturas) / len(temperaturas)
print(f"\nPromedio de las temperaturas ingresadas: {promedio:.2f} °C")
print("Conversión completada exitosamente.")
print("=" * 35)