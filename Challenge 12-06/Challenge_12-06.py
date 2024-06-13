numero_usuario = int(input ('Ingrese numero que quiere multiplicar: '))

print(f"Tabla de multiplicar del {numero_usuario}:")
for i in range(1, 11):
    resultado = numero_usuario * i
    print(f"{numero_usuario} x {i} = {resultado}")