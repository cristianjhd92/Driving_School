# Se importa de decoradores.py la función validate_input para validar la entrada de datos
from decorators import validate_input

# Se crea la clase Person con los atributos document, name, lastname y age
class Person:
    # Se crea el constructor de la clase con los atributos document, name, lastname y age
    def __init__(self, document, name, lastname, age):
        # Con el __ se encapsulan los atributos de la clase
        self.__document = document
        self.__name = name
        self.__lastname = lastname
        self.__age = age
    
    # Se crean los métodos get para obtener los valores de los atributos de la clase
    def get_document(self):
        return self.__document
    
    def get_full_name(self):
        return f"{self.__name} {self.__lastname}"
    
    def get_age(self):
        return self.__age

# Clase base DatabaseManager para manejo de datos
class DatabaseManager:
    # Se crea la lista de estudiantes, se usa __ para encapsular la lista y se inicializa vacía
    __students = []  # Encapsulación de la lista de estudiantes
    
    # Se crea el método add_student para agregar un alumno a la lista
    @classmethod # Decorador para indicar que es un método de clase y no de instancia para acceder a la lista de estudiantes
    def add_student(cls, student): # Se recibe el objeto student como parámetro y cls hace referencia a la clase
        cls.__students.append(student) # Se agrega el objeto student a la lista de estudiantes
    
    # Se crea el método get_students para obtener la lista de estudiantes
    @classmethod
    def get_students(cls): # cls hace referencia a la clase para acceder a la lista de estudiantes
        return cls.__students # Se retorna la lista de estudiantes
    
    # Se crea el método remove_student para eliminar un alumno de la lista
    @classmethod 
    def remove_student(cls, student): # Se recibe el objeto student como parámetro y cls hace referencia a la clase
        cls.__students.remove(student) # Se elimina el objeto student de la lista de estudiantes

# Clase Student heredando de Person y DatabaseManager
class Student(Person, DatabaseManager):
    # Se crea el constructor de la clase con los atributos document, name, lastname, age y category
    def __init__(self, document, name, lastname, age, category):
        # Se llama al constructor de la clase padre Person con los atributos document, name, lastname y age
        super().__init__(document, name, lastname, age)
        # Se encapsula el atributo category de la clase
        self.__category = category
    
    # Se crea el método get_category para obtener el valor del atributo category
    def get_category(self):
        # Se retorna el valor del atributo category
        return self.__category
    
    # Se crean los métodos de clase para realizar las operaciones CRUD

    # Se crea el método create_student para crear un alumno
    @classmethod
    def create_student(cls):
        # Se solicitan los datos del alumno
        print("-------------------------------------------------------")
        document = input("Ingrese el número de documento: ")
        name = input("Ingrese el nombre: ")
        lastname = input("Ingrese el apellido: ")
        age = input("Ingrese la edad: ")
        category = input("Ingrese la categoría: ")
        print("-------------------------------------------------------")
        
        # Se crea un objeto student con los datos ingresados
        student = cls(document, name, lastname, age, category)
        # Se agrega el objeto student a la lista de estudiantes
        cls.add_student(student)
        # Se muestra un mensaje de confirmación
        print("-------------------------------------------------------")
        print("Alumno agregado exitosamente")
        print("-------------------------------------------------------")
    
    # Se crea el método show_students para mostrar todos los alumnos
    @classmethod
    def show_students(cls):
        # Se obtiene la lista de estudiantes con el método get_students
        students = cls.get_students()
        # Se verifica si la lista de estudiantes está vacía
        if not students:
            # Se muestra un mensaje indicando que no hay estudiantes registrados
            print("-------------------------------------------------------")
            print("No hay estudiantes registrados.")
            print("-------------------------------------------------------")
            # Se retorna
            return
        # Se recorre la lista de estudiantes
        for student in students:
            # Se muestra los datos de cada estudiante
            print("-------------------------------------------------------")
            print("Número de documento:", student.get_document())
            print("Nombre Completo:", student.get_full_name())
            print("Edad:", student.get_age())
            print("Categoría:", student.get_category())
            print("-------------------------------------------------------")
    
    # Se crea el método find_student para buscar un alumno por número de documento
    @classmethod # Decorador para indicar que es un método de clase y no de instancia para acceder a la lista de estudiantes
    @validate_input # Se aplica el decorador validate_input para validar la entrada de datos
    def find_student(cls):
        # Se solicita el número de documento del alumno
        print("-------------------------------------------------------")
        document = input("Ingrese el número de documento del alumno a buscar: ")
        print("-------------------------------------------------------")
        # Se recorre la lista de estudiantes llamando al método get_students
        for student in cls.get_students():
            # Se verifica si el número de documento del estudiante es igual al ingresado
            if student.get_document() == document:
                # Se muestran los datos del estudiante
                print("-------------------------------------------------------")
                print("Número de documento:", student.get_document())
                print("Nombre Completo:", student.get_full_name())
                print("Edad:", student.get_age())
                print("Categoría:", student.get_category())
                print("-------------------------------------------------------")
                # Se retorna True si se encuentra el estudiante
                return True
        # Se retorna False si no se encuentra el estudiante
        return False
    
    # Se crea el método update_student para actualizar los datos de un alumno
    @classmethod # Decorador para indicar que es un método de clase y no de instancia para acceder a la lista de estudiantes
    @validate_input # Se aplica el decorador validate_input para validar la entrada de datos
    def update_student(cls):
        # Se solicita el número de documento del alumno a actualizar
        print("-------------------------------------------------------")
        document = input("Ingrese el número de documento del alumno a actualizar: ")
        print("-------------------------------------------------------")
        # Se recorre la lista de estudiantes llamando al método get_students
        for student in cls.get_students():
            # Se verifica si el número de documento del estudiante es igual al ingresado
            if student.get_document() == document:
                # Se solicita el dato a actualizar
                print("-------------------------------------------------------")
                query = input("¿Qué dato desea actualizar? (nombre, apellido, edad, categoría): ")
                print("-------------------------------------------------------")
                # Se verifica el dato a actualizar
                if query == "nombre":
                    # Se solicita el nuevo nombre del alumno
                    student._Person__name = input("Ingrese el nuevo nombre: ")
                    print("-------------------------------------------------------")

                elif query == "apellido":
                    # Se solicita el nuevo apellido del alumno
                    student._Person__lastname = input("Ingrese el nuevo apellido: ")
                    print("-------------------------------------------------------")
                
                elif query == "edad":
                    # Se solicita la nueva edad del alumno
                    student._Person__age = input("Ingrese la nueva edad: ")
                    print("-------------------------------------------------------")
                
                elif query == "categoría":
                    # Se solicita la nueva categoría del alumno
                    student.__category = input("Ingrese la nueva categoría: ")
                    print("-------------------------------------------------------")
                
                else:
                    # Se muestra un mensaje indicando que el dato ingresado es incorrecto
                    print("Dato no válido")
                    print("-------------------------------------------------------")
                    # Se retorna False si el dato ingresado es incorrecto
                    return False
                # Se muestra un mensaje de confirmación
                print("-------------------------------------------------------")
                print("Alumno actualizado exitosamente")
                print("-------------------------------------------------------")
                # Se retorna True si se actualiza el estudiante
                return True
        # Se retorna False si no se encuentra el estudiante
        return False
    
    # Se crea el método delete_student para eliminar un alumno
    @classmethod # Decorador para indicar que es un método de clase y no de instancia para acceder a la lista de estudiantes
    @validate_input # Se aplica el decorador validate_input para validar la entrada de datos
    def delete_student(cls):
        # Se solicita el número de documento del alumno a eliminar
        print("-------------------------------------------------------")
        document = input("Ingrese el número de documento del alumno a eliminar: ")
        print("-------------------------------------------------------")
        # Se recorre la lista de estudiantes llamando al método get_students
        for student in cls.get_students():
            # Se verifica si el número de documento del estudiante es igual al ingresado
            if student.get_document() == document:
                # Se elimina el estudiante de la lista de estudiantes llamando al método remove_student de la clase DatabaseManager
                cls.remove_student(student)
                # Se muestra un mensaje de confirmación
                print("-------------------------------------------------------")
                print("Alumno eliminado exitosamente")
                print("-------------------------------------------------------")
                # Se retorna True si se elimina el estudiante
                return True
        # Se retorna False si no se encuentra el estudiante
        return False
