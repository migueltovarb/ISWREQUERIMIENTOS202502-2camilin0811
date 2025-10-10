lmenu_cine = [
    "1. Registrar función nueva a una película",
    "2. Lista de funciones disponibles",
    "3. Vender boletos",
    "4. Calcular total a pagar",
    "5. Resumen de ventas diarias"
]

class CineMovieTime:
    def __init__(self, id_pelicula, nombre_pelicula, funciones_boletos, precio):
        self.id_pelicula = id_pelicula
        self.nombre_pelicula = nombre_pelicula
        self.funciones_boletos = funciones_boletos if funciones_boletos else {}
        self.precio = precio
        self.ventas = []  

    def agregar_funcion(self, nueva_funcion, boletos):
        if nueva_funcion not in self.funciones_boletos:
            self.funciones_boletos[nueva_funcion] = boletos
            print(f"Función '{nueva_funcion}' agregada correctamente a la película '{self.nombre_pelicula}' con {boletos} boletos disponibles.")
        else:
            print(f"La función '{nueva_funcion}' ya existe para esta película.")

    def vender_boletos(self, funcion, cantidad):
        if funcion not in self.funciones_boletos:
            print(f"La función '{funcion}' no está disponible para esta película.")
            return
        if cantidad > self.funciones_boletos[funcion]:
            print("No hay suficientes boletos disponibles para la venta en esa función.")
            return
        total = self.precio * cantidad
        self.funciones_boletos[funcion] -= cantidad
        self.ventas.append((funcion, cantidad, total))
        print(f"Venta realizada: {cantidad} boletos para '{self.nombre_pelicula}' en función '{funcion}'. Total a pagar: ${total:.2f}")

    def resumen_ventas(self):
        if not self.ventas:
            print(f"No hay ventas registradas para '{self.nombre_pelicula}'.")
            return
        print(f"Resumen de ventas para '{self.nombre_pelicula}':")
        for funcion, cantidad, total in self.ventas:
            print(f"  Función: {funcion} | Boletos vendidos: {cantidad} | Total: ${total:.2f}")

    def get_id(self):
        return self.id_pelicula

    def get_data(self):
        print(f"ID Película: {self.id_pelicula}\nNombre: {self.nombre_pelicula}\nFunciones disponibles:")
        if self.funciones_boletos:
            for f, b in self.funciones_boletos.items():
                print(f"  - {f} (Boletos disponibles: {b})")
        else:
            print("  (Ninguna)")
        print(f"Precio: {self.precio}")

    def __str__(self):
        return f"ID: {self.id_pelicula}, Nombre: {self.nombre_pelicula}"



class InventarioPeliculas:
    def __init__(self):
        self.peliculas = {}  

    def agregar_pelicula(self, pelicula_nueva):
        if pelicula_nueva.id_pelicula in self.peliculas:
            print("Ya existe una película con ese ID.")
            return
        self.peliculas[pelicula_nueva.id_pelicula] = pelicula_nueva
        print("Película agregada correctamente.")

    def consultar_pelicula(self, id_pelicula):
        pelicula = self.peliculas.get(id_pelicula)
        if pelicula:
            print("\nPelícula encontrada:")
            pelicula.get_data()
        else:
            print("\nPelícula no encontrada.")

    def valor_inventario(self):
        return sum(p.precio for p in self.peliculas.values())

    def __str__(self):
        return "Inventario Organizado XYZ"
    


def impresion_menu():
    print("\nMenu de opciones")
    for i in lmenu_cine:
        print(i)
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
            if 1 <= opcion <= 5:
                return opcion
            else:
                print("Opción inválida. Por favor, seleccione una opción entre 1 y 5.")
        except ValueError:
            print("ERROR: Debe ingresar un número entero.")
            

def main():
    inventario = InventarioPeliculas()
    while True:
        op = impresion_menu()
        if op == 1:
            id_pelicula = input("Ingrese el ID de la película: ").strip().upper()
            nombre_pelicula = input("Ingrese el nombre de la película: ").strip()
            funciones_boletos = {}
            while True:
                funcion = input("Ingrese el horario/función (o deje vacío para terminar): ").strip()
                if not funcion:
                    break
                while True:
                    try:
                        boletos = int(input(f"Ingrese la cantidad de boletos disponibles para '{funcion}': "))
                        break
                    except ValueError:
                        print("Debe ingresar un número entero.")
                funciones_boletos[funcion] = boletos
            while True:
                try:
                    precio = float(input("Ingrese el precio del boleto: "))
                    break
                except ValueError:
                    print("El precio debe ser un número.")
            pelicula_nueva = CineMovieTime(
                id_pelicula,
                nombre_pelicula,
                funciones_boletos,
                precio
            )
            inventario.agregar_pelicula(pelicula_nueva)
        elif op == 2:
            print("\nFunciones disponibles por película:")
            for pelicula in inventario.peliculas.values():
                print(f"Película: {pelicula.nombre_pelicula} (ID: {pelicula.id_pelicula})")
                if pelicula.funciones_boletos:
                    for f, b in pelicula.funciones_boletos.items():
                        print(f"  - {f} (Boletos disponibles: {b})")
                else:
                    print("  (Sin funciones registradas)")
        elif op == 3:
            id_pelicula = input("Ingrese el ID de la película para la venta: ").strip().upper()
            funcion = input("Ingrese la función (horario) para la venta: ").strip()
            try:
                cantidad = int(input("Ingrese la cantidad de boletos a vender: "))
            except ValueError:
                print("La cantidad debe ser un número entero.")
                continue
            pelicula = inventario.peliculas.get(id_pelicula)
            if pelicula:
                pelicula.vender_boletos(funcion, cantidad)
            else:
                print("Película no encontrada para venta.")
        elif op == 4:
            id_pelicula = input("Ingrese el ID de la película para calcular el total a pagar: ").strip().upper()
            funcion = input("Ingrese la función (horario): ").strip()
            try:
                cantidad = int(input("Ingrese la cantidad de boletos: "))
            except ValueError:
                print("La cantidad debe ser un número entero.")
                continue
            pelicula = inventario.peliculas.get(id_pelicula)
            if pelicula and funcion in pelicula.funciones_boletos:
                total = pelicula.precio * cantidad
                print(f"Total a pagar por {cantidad} boletos para '{pelicula.nombre_pelicula}' en función '{funcion}': ${total:.2f}")
            else:
                print("Película o función no encontrada.")
        elif op == 5:
            print("\nResumen de ventas diarias:")
            for pelicula in inventario.peliculas.values():
                pelicula.resumen_ventas()
if __name__ == "__main__":
    main()