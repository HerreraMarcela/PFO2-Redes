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
    print(f"\n[Estado HTTP {res.status_code}]")
    if res.ok:
        print(" Acceso concedido al Sistema de Tareas:")
        print("  1. Validar endpoint POST /registro con hash scrypt")
        print("  2. Verificar persistencia de usuarios en SQLite")
        print("  3. Visualizar respuestas HTTP y bienvenida del sistema")
        print("\n(Interfaz gráfica disponible en: http://127.0.0.1:5000/tareas)")
    else:
        print("No se pudo acceder a las tareas. Verificá que el servidor esté activo.")


def menu():
    while True:
        print("\n--- CLIENTE API ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Ver tareas")
        print("4. Salir")

        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            registrar()
        elif opcion == "2":
            login()
        elif opcion == "3":
            ver_tareas()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()