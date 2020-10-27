import os
from flask import Flask, jsonify, request

app = Flask (__name__)

@app.route('/')
def nao_entre_em_panico():
    prox = 1
    ant = 0
    maximo = 50
    found = 0
    resposta = "0 -"
    while (found < maximo):
        fibo = prox
        prox = prox + ant
        ant = fibo
        found = found+1
        resposta+= str(prox) + "-"


    return resposta

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host= '0.0.0.0', port=port)