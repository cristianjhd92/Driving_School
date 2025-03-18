# Se importan las librerías os para limpiar la pantalla de la consola y Student para acceder a los métodos de la clase Student
import os
from crud import Student

# Se crea una clase para manejar el menú de la aplicación
class Menu:
    
    # Función estática para limpiar la pantalla de la consola
    @staticmethod
    def clear_screen():
        # Se utiliza la función os.system para limpiar la pantalla de la consola
        os.system('cls' if os.name == 'nt' else 'clear')

    # Función estática para mostrar el menú de la aplicación
    @staticmethod
    def show_menu():
        # Mientras se cumpla la condición, se muestra el menú
        while True:
            # Se limpia la pantalla de la consola
            Menu.clear_screen()
            # Se muestra el menú de la aplicación
            print(
"""
-------------------------------------------------------
Bienvenido a la aplicación de la escuela de conducción
-------------------------------------------------------
1. Ingresar nuevo alumno
2. Mostrar todos los alumnos
3. Buscar un alumno por número de documento
4. Actualizar los datos de un alumno
5. Eliminar un alumno
6. Salir
-------------------------------------------------------
""")
            # Se solicita al usuario que seleccione una opción
            option = input("Seleccione una opción: ")
            # Se verifica la opción seleccionada por el usuario
            if option == "1":
                # Se llama al método create_student de la clase Student
                Student.create_student()
            elif option == "2":
                Student.show_students()
            elif option == "3":
                Student.find_student()
            elif option == "4":
                Student.update_student()
            elif option == "5":
                Student.delete_student()
            elif option == "6":
                # Se limpia la pantalla de la consola
                Menu.clear_screen()
                print("-------------------------------------------------------")
                print("Saliendo del sistema...")
                print("-------------------------------------------------------")
                # Se rompe el ciclo while para salir de la aplicación
                break
            else:
                print("Opción no válida, intente de nuevo.")
            # Se espera a que el usuario presione Enter para continuar
            input("Presione Enter para continuar...")

# Se verifica si el script se ejecuta directamente
if __name__ == "__main__":
    # Se llama al método show_menu de la clase Menu
    Menu.show_menu()