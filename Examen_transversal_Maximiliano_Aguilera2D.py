productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
    'FS1230HD': ['Acer', 14, '4GB', 'SSD', '256GB', 'Intel Celeron', 'integrada']
}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0]
}

def stock_marca(marca):

    total_stock = 0
    for modelo, info in productos.items():
        if info[0].lower() == marca.lower():
            total_stock += stock[modelo][1]
    print(f"El stock es: {total_stock}")

def busqueda_precio(p_min, p_max):
    notebooks_encontrados = []
    for modelo, info_stock in stock.items():
        precio = info_stock[0]
        cantidad_stock = info_stock[1]
        if p_min <= precio <= p_max and cantidad_stock > 0:
            marca = productos[modelo][0]
            notebooks_encontrados.append(f"{marca}--{modelo}")
    
    if not notebooks_encontrados:
        print("no hay notebooks en ese rango de precios.")
    else:
        notebooks_encontrados.sort()
        print(f"los notebooks entre los precios consultas son: {notebooks_encontrados}")

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    else:
        return False

def mostrar_menu():
    """Muestra el menú principal de opciones."""
    print("\n*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese opción: ")

        if opcion == '1':
            marca_consultar = input("Ingrese marca a consultar: ")
            stock_marca(marca_consultar)
        elif opcion == '2':
            while True:
                try:
                        precio_min_str = input("Ingrese precio mínimo: ")
                        p_min = int(precio_min_str)
                        precio_max_str = input("Ingrese precio máximo: ")
                        p_max = int(precio_max_str)
                        break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            busqueda_precio(p_min, p_max)
        elif opcion == '3':
            while True:
                modelo_actualizar = input("Ingrese modelo a actualizar: ")
                while True:
                    try:
                        precio_nuevo_str = input("Ingrese precio nuevo: ")
                        precio_nuevo = int(precio_nuevo_str)
                        break
                    except ValueError:
                        print("Debe ingresar un valor entero para el precio")
                
                if actualizar_precio(modelo_actualizar, precio_nuevo):
                    print("Precio actualizadO")
                else:
                    print("El modelo no existe")
                
                respuesta = input("Desea actualizar otro precio (s/n)?: ").lower()
                if respuesta != 'si':
                    break
        elif opcion == '4':
            print("Programa finalizado.")
            break
        else:
            print("Debe seleccionar una opción válida!!")

if __name__ == "__main__":
    main()