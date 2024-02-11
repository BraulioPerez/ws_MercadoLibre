from flask import Flask, jsonify, send_file
import json

app = Flask(__name__)

@app.route('/descargar_json', methods=['GET'])
def descargar_json():
    data = {"mensaje": "Hola, Mundo!"}
    with open('archivo.json', 'w') as f:
        json.dump(data, f)
    return send_file('archivo.json', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
