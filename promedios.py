notas = []

print("Se solicitarán 3 notas para calcular su promedio")

for i in range(3):
    nota = int(input("Ingrese una nota: "))
    notas.append(nota)

promedio = sum(notas)/3

print("El promedio de las notas es ", promedio)