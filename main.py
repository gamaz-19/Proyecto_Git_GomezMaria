###################################
####### Empanadas Doña Pepa #######
###################################


from functions.functionJSONS import*




empanadasTodas= []
idEmpanada = 1

booleano = True
while booleano:
    print ('''
Bienvenido a Empanadas Doña Pepa

1. Tipos de empanadas
2. Registrar empanada
3. Editar empanadas
4. Eliminar empanadas
5. Salir de Empanadas Dona Pepa

''')


    menuPrincipal = (int(input("Ingrese el numero de su seleccion: ")))
    
    if (menuPrincipal==1):
        print("Tipos de empanadas")
        for i in range (len(empanadasTodas)):
            empanadasNombres = [nombre["nombre"] for nombre in empanadasTodas]
            #Set se usa para quiter los duplicados
            empanadasNombres = set(empanadasNombres)
        print (empanadasNombres)



    elif (menuPrincipal==2):

        print("Registrar empanada")
        nombre= (input("Nombre = "))
        precio= (int(input("Precio = ")))
        ingredientes= (input("Ingredientes = "))
        print("Ingrese 's' si esta disponible, ingrese 'n' si no esta disponible")
        disponibilidad= (input("Disponible = "))

        empanadaNueva={
            "id" : idEmpanada,
            "nombre" : nombre,
            "precio" : precio,
            "ingredientes" : ingredientes,
            "disponibilidad" : disponibilidad
        }

        empanadasTodas.append(empanadaNueva)

        idEmpanada = (idEmpanada + 1 )
        print(empanadaNueva)


    elif (menuPrincipal==3):
        print("Editar empanada")
        empanadaCambio=(int(input("Ingrese el numero de id de la empanada que quiere editar: ")))

        for i in range (len(empanadasTodas)):
            if empanadaCambio == empanadasTodas[i]["id"]:
                print (empanadasTodas[i])

                nombreN = (input ("Nombre: "))
                precioN= (int(input("Precio = ")))
                ingredientesN= (input("Ingredientes = "))
                print("Ingrese 's' si esta disponible, ingrese 'n' si no esta disponible")
                disponibilidadN= (input("Disponible = "))

                empanadasTodas[i]["nombre"] = nombreN
                empanadasTodas[i]["precio"] = precioN
                empanadasTodas[i]["ingredientes"] = ingredientesN
                empanadasTodas[i]["disponibilidad"] = disponibilidadN

                print (empanadasTodas[i])

    elif (menuPrincipal==4):
        print("Eliminar empanada")
        empanadaEliminar=(int(input("Ingrese el numero de id de la empanada que quiere editar: ")))

        for i in range (len(empanadasTodas)):
            if empanadaEliminar == empanadasTodas[i]["id"]:
                empanadaEliminada = empanadasTodas.pop(i)
                print (empanadaEliminada)
                break



    elif (menuPrincipal==5):
        print("Saliendo de Empanadas Dona Pepa")
        booleano=False

    else:
        print("Seleccion no valida")


# Desarrollado por: Maria Alejandra Gomez Archila - cc.1005234916