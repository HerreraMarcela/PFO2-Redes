from flask import Flask, request, jsonify, render_template_string, redirect
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# -------------------------------
# Inicializar base de datos
# -------------------------------
def inicializar_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE,
        contraseña TEXT
    )
    """)

    conn.commit()
    conn.close()


# -------------------------------
# Registro de usuario
# -------------------------------
@app.route("/registro", methods=["POST"])
def registro():
    data = request.json

    usuario = data.get("usuario")
    contraseña = data.get("contraseña")

    if not usuario or not contraseña:
        return jsonify({"error": "Faltan datos"}), 400

    hash_pass = generate_password_hash(contraseña)

    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)",
            (usuario, hash_pass)
        )

        conn.commit()
        conn.close()

        return jsonify({"mensaje": "Usuario registrado correctamente"})

    except sqlite3.IntegrityError:
        return jsonify({"error": "El usuario ya existe"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -------------------------------
# Inicio de sesión
# -------------------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    usuario = data.get("usuario")
    contraseña = data.get("contraseña")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT contraseña FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()

    conn.close()

    if resultado and check_password_hash(resultado[0], contraseña):
        return jsonify({"mensaje": "Login exitoso"})
    else:
        return jsonify({"error": "Credenciales incorrectas"}), 401


# -------------------------------
# Página de inicio
# -------------------------------
@app.route("/")
def inicio():
    return redirect("/tareas")

# -------------------------------
# Vista de tareas (frontend)
# -------------------------------
@app.route("/tareas", methods=["GET"])
def tareas():
    # Lee directamente el index.html en la raíz
    with open("index.html", "r", encoding="utf-8") as f:
        return render_template_string(f.read())


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    inicializar_db()
    app.run(debug=True)