from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    # Liest den Parameter ?name=... aus der URL
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'

if __name__ == '__main__':
    # host 0.0.0.0 ist wichtig, damit der Container von außen erreichbar ist
    app.run(host='0.0.0.0', port=8080)