#Por si hay problemas con la terminal
def DirectorioyRuta():
    import os
    existe = os.path.exists('models')
    ruta = os.getcwd()
    print(f"¿Existe carpeta 'models'? {existe}")
    print(f"Ruta actual: {ruta}")
    return existe, ruta