from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "¡Bienvenido a tu aplicación Flask desplegada con éxito! 🚀",
        "status": "ok"
    })

@app.route('/info')
def info():
    return jsonify({
        "app": "Mi App Flask",
        "version": "1.0.0",
        "autor": "Tu Nombre",
        "descripcion": "Una aplicación Flask lista para despliegue."
    })

if __name__ == '__main__':
    # Escucha en 0.0.0.0 para que funcione dentro de contenedores/Docker
    app.run(host='0.0.0.0', port=5000, debug=False)
