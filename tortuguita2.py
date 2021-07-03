# o objetivo é diminuir as linhas de codigo usando funções
from turtle import Turtle
# inicializando Turtle
t = Turtle()
t.shape("turtle")
print("-----------TORTUGUITA 1.2------------")

def desisao_direcao():
    resposta = int(input(" deseja andar quantas pixels?"))
    return resposta
def desisao_lado(turtle):
    resposta = int(input(" deseja ira para esquerda (1) ou direita (2)?"))
    if resposta == 1:
        desisao_esquerda(turtle)
    elif resposta == 2:
        desisao_direita(turtle)
    else:
        print("resposta invalida")
def desisao_esquerda(turtle):
    esquerda = int(input("quantos graus para a esquerda?"))
    t.left(esquerda)
def desisao_direita(turtle):

    direita = int(input("quantos graus para a direita?"))
    t.right(direita)

while True:
    desisao = int(input(" deseja ir para frente(1) ou para trás (2)?"))
    if desisao == 1:
            direcao = desisao_direcao()
            desisao_lado(t)
            t.forward(direcao)
    elif desisao == 2:
            direcao = desisao_direcao()
            desisao_lado(t)
            t.backward(direcao)
    else:
        print("resposta invalida")
    resposta = int(input("continuar andando? sim (1); não (2)")) 
    if resposta == 1:
                continue
    elif resposta == 2:
                break
    else:
        print("entrada invalida")
        continue