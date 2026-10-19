def saludar(nombre):
    """Función que saluda a la persona cuyo nombre se pasa como argumento."""
    return f"Hola, {nombre}!"
otra = saludar
print(otra("Lucía"))  # Esto imprimirá: Hola, Lucía!
def aplicar_dos_veces(funcion, valor):
    """Función que aplica otra función dos veces a un valor."""
    return funcion(funcion(valor))          
def sumar_iva(precio):
    """Función que suma el IVA (21%) a un precio dado."""
    return round(precio * 1.21, 2)  # Redondea a dos decimales
def duplicar(x):
    """Función que duplica el valor dado."""
    return x * 2 
print(aplicar_dos_veces(sumar_iva, 5))  
print(aplicar_dos_veces(duplicar, 100))