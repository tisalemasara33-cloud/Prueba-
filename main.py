# Programa básico de prueba
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}!")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

print(f"La suma es: {num1 + num2}")
print(f"La resta es: {num1 - num2}")
print(f"La multiplicación es: {num1 * num2}")
if num2 != 0:
    print(f"La división es: {num1 / num2}")
else:
    print("No se puede dividir entre cero")

