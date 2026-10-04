import requests

URL = "http://127.0.0.1:5000"


def registrar():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    res = requests.post(f"{URL}/registro", json={
        "usuario": usuario,
        "contraseña": contraseña
    })

    print("Respuesta:", res.json())


def login():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    res = requests.post(f"{URL}/login", json={
        "usuario": usuario,
        "contraseña": contraseña
    })

    print("Respuesta:", res.json())


def ver_tareas():
    res = requests.get(f"{URL}/tareas")
    print("Estado HTTP:", res.status_code)
    print("HTML recibido correctamente. Podés abrir en el navegador: http://127.0.0.1:5000/tareas")


def menu():
    while True:
        print("\n--- CLIENTE API ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
       
        print("3. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            registrar()
        elif opcion == "2":
            login()
        
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()