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