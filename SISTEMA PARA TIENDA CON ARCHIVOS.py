# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

# Clase Inventario
class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    id, nombre, cantidad, precio = linea.strip().split(',')
                    producto = Producto(id, nombre, int(cantidad), float(precio))
                    self.productos[id] = producto
        except FileNotFoundError:
            print("El archivo de inventario no se encuentra. Se creará un nuevo archivo al guardar datos.")
        except PermissionError:
            print("No se tienen permisos para leer el archivo de inventario.")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos.values():
                    file.write(f"{producto.get_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n")
            print("Inventario guardado con éxito.")
        except PermissionError:
            print("No se tienen permisos para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print(f"Error: Ya existe un producto con el ID {producto.get_id()}.")
        else:
            self.productos[producto.get_id()] = producto
            self.guardar_inventario()
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id):
        if id in self.productos:
            producto = self.productos.pop(id)
            self.guardar_inventario()
            return f"Producto con ID {id} eliminado. Detalles: {producto}"
        else:
            return f"Error: No se encontró un producto con el ID {id}."

    def actualizar_producto(self, id, nombre=None, cantidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if nombre is not None:
                producto.set_nombre(nombre)
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            self.guardar_inventario()
            return f"Producto con ID {id} actualizado."
        else:
            return f"Error: No se encontró un producto con el ID {id}."

    def buscar_producto_por_id(self, id):
        return self.productos.get(id)

    def buscar_productos_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_todos_los_productos(self):
        if not self.productos:
            return "No hay productos en el inventario."
        else:
            return '\n'.join(str(producto) for producto in self.productos.values())

    def mostrar_ruta_archivo(self):
        return f"El archivo de inventario se encuentra en: {self.archivo}"

    def cambiar_nombre_archivo(self, nuevo_nombre):
        if not nuevo_nombre.endswith('.txt'):
            nuevo_nombre += '.txt'
        try:
            with open(self.archivo, 'r') as file:
                contenido = file.read()

            with open(nuevo_nombre, 'w') as file:
                file.write(contenido)

            self.archivo = nuevo_nombre
            return f"Nombre del archivo cambiado a {self.archivo}."
        except FileNotFoundError:
            return "Error: El archivo original no se encuentra."
        except PermissionError:
            return "Error: No se tienen permisos para cambiar el nombre del archivo."
        except Exception as e:
            return f"Error inesperado al cambiar el nombre del archivo: {e}"

# Funciones para mostrar el logo y la información
def mostrar_logo_uea():
    # Simulación de un logo usando caracteres ASCII
    print("""
**************************************************
*                                                *
*                  UEA                           *
*INGENIERIA EN TECNOLOGIAS DE LA INFORMACION     *
*                                                *
**************************************************
    """)

def mostrar_informacion():
    print("Ingeniería en Tecnologías de la Información\n")

def limpiar_consola():
    print("\n" * 100)  # Simular el borrado de la consola imprimiendo 100 líneas en blanco.

# Función para mostrar el menú
def mostrar_menu():
    mostrar_logo_uea()
    mostrar_informacion()
    print("Gestión de Inventario")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre o ID")
    print("5. Mostrar todos los productos")
    print("6. Mostrar ubicación del archivo de inventario")
    print("7. Cambiar nombre del archivo de inventario")
    print("8. Salir")

# Función principal
def main():
    archivo_inventario = input("Ingrese el nombre del archivo de inventario (por defecto 'inventario.txt'): ") or 'inventario.txt'
    inventario = Inventario(archivo_inventario)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
            limpiar_consola()
            print("Producto añadido con éxito.")

        elif opcion == '2':
            id = input("Ingrese el ID del producto a eliminar: ")
            mensaje = inventario.eliminar_producto(id)
            limpiar_consola()
            print(mensaje)

        elif opcion == '3':
            id = input("Ingrese el ID del producto a actualizar: ")
            nombre = input("Ingrese el nuevo nombre (dejar en blanco para no cambiar): ")
            cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")
            nombre = nombre if nombre else None
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            mensaje = inventario.actualizar_producto(id, nombre, cantidad, precio)
            limpiar_consola()
            print(mensaje)

        elif opcion == '4':
            criterio = input("Ingrese el nombre del producto o el ID a buscar: ")
            producto = inventario.buscar_producto_por_id(criterio)
            if producto:
                print(producto)
            else:
                resultados = inventario.buscar_productos_por_nombre(criterio)
                if resultados:
                    for producto in resultados:
                        print(producto)
                else:
                    print("No se encontraron productos con ese nombre o ID.")
            limpiar_consola()

        elif opcion == '5':
            productos = inventario.mostrar_todos_los_productos()
            print(productos)
            limpiar_consola()

        elif opcion == '6':
            ruta = inventario.mostrar_ruta_archivo()
            print(ruta)
            limpiar_consola()

        elif opcion == '7':
            nuevo_nombre = input("Ingrese el nuevo nombre del archivo (sin extensión): ")
            mensaje = inventario.cambiar_nombre_archivo(nuevo_nombre)
            print(mensaje)
            limpiar_consola()

        elif opcion == '8':
            print("Saliendo del sistema de gestión de inventarios.")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")
            limpiar_consola()

if __name__ == "__main__":
    main()
