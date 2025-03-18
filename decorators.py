# Se recibe una función como parámetro
def validate_input(func):
    # Se crea una función interna que recibe los parámetros de la función original
    # *args recibe argumentos posicionales y **kwargs recibe argumentos con nombre
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
            # Si la función no devuelve un valor válido, se imprime un mensaje
        if not result:
            print("Entrada no válida, intente nuevamente.")
            # Se devuelve el resultado de la función
        return result
        # Se devuelve la función interna
    return wrapper