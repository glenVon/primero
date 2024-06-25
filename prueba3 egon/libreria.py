Libros=[]
Generos=['ficcion','no ficcion','ciencia']
CANTIDAD=[]

def registrar_libros():
    try:
        Titulo= input('ingresa el titulo del libro: ')
        Autor= input('ingresa el autor del libro: ')
        Genero= input('ingresa el genero del libro: ').lower()
        while Genero not in Generos:
            print('este genero no se encuentra disponible')
            return
        precio= int(input('ingresa valor del libro: '))
    except ValueError:
        print('ERROR: No has ingresado bien los datos ')

    Libros.append({
         Titulo,
         Autor,
         Genero,
         precio
    })

    

def listar_libros():
    print('--TITULO  AUTOR  GENERO  PRECIO--')
    for lib in Libros:
        print(lib)

def registrar_venta():
    titulo=input('ingrese titulo del libro: ')
    Cantidad= int(input('ingrese las unidades del libro: '))
    precio_uni=int(input('ingrese precio por unidad: '))
    precio_fin=int(input('valor final: '))

    CANTIDAD.append({
        titulo,
        Cantidad,
        precio_uni,
        precio_fin
    })


def imprimir_reporte_de_ventas():
    print('--REPORTE DE VENTAS--')
    for titulo in Libros:
        print(titulo)
    for cantidad in CANTIDAD:
        print(cantidad)
    for Libros in Libros:
        print(Libros)


def generar_txt():
    registrar_libros.txt
    with open(registrar_libros,'w') as archivo:
        print(archivo.txt)


try:
    while True:
        print('''
----LIBRERIA----
      1.REGISTRAR LIBRO
      2.LISTA DE LIBROS
      3.REGISTRO DE VENTAS
      4.GENERAR ARCHIVO TXT
      5.SALIR
''')
        opcion=int(input('ingrese una opcion: '))

        if opcion==1:
            registrar_libros()
        elif opcion==2:
            listar_libros()
        elif opcion==3:
            registrar_venta()
        elif opcion==4:
            imprimir_reporte_de_ventas()
        elif opcion==5:
            generar_txt()
        else:
            break
except ValueError:
    print('ERROR: Valores incorrectos')



