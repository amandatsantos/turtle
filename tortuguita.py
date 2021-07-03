from turtle import Turtle
# inicializando turtle
t = Turtle()
t.shape("turtle")
print("--------------------BEM VINDO AO TORTUGUITA!!!!!-----------")
while True:
        desisao = int(input("em qual direção você deseja ir : esquerda (1) ou direita (2)?"))
        if desisao == 1:
            esq=int(input("quantos graus para esquerda?"))
            t.left(esq)
        elif desisao ==2:
            dir=int(input("quantos graus para direita?"))
            t.right(dir)
        else: 
            print ("resposta invalida")
            break
        dir = int(input("deseja ir pra frente ou para tras?1-frente; 2-trás:"))
        if dir == 1:
            dis=int(input("distancia:"))
            t.forward(dis)
        elif dir == 2:
             dis=int(input("distancia:"))
             t.backward(dis)
        else:
            print("resposta invalida")
            break
        desisao=int(input("deseja continuar a andar? 1-sim; 2-não"))
        if desisao ==1 :
            continue
        elif desisao ==2:
            break
        else:
            print("resposta invalida")

        desisao = int(input("deseja continuar a jogar? 1 - sim; 2 - não :"))
               
        if desisao ==1:
            continue
        if desisao ==2:
            print("você saiu do jogo".quit())
        else:
            while True:
                print("responta invalida")
                break
        

    



    