importar  os
from  flask  import  Flask , jsonify , request

app  =  Flask ( __name__ )

@ app . rota ( '/' )
def  nao_entre_em_panico ():
    prox  =  1
    formiga  =  0
    maximo  =  50
    encontrado  =  0
    resposta  =  "0 -"
    while ( encontrado  <  maximo ):
        fibo  =  prox
        prox  =  prox  +  ant
        formiga  =  fibo
        encontrado  =  encontrado + 1
        resposta + =  str ( prox ) +  "-"


     resposta de retorno

if  __name__  ==  "__main__" :
    porta  =  int ( os . amb . get ( "PORT" , 5000 ))
    app . executar ( host =  '0.0.0.0' , porta = porta )
