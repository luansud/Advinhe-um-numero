import os
import tkinter
from random import randint
from tkinter import *

num_sorteado = randint(1, 100)
chances = 10

def advinhar():
    global chances
    num_user = int(entry_numero.get())
    if num_user < num_sorteado:
        chances -= 1
        texto_resultado["text"] = "Numero abaixo do escolhido, Você ainda tem "+ str(chances)+ " chances"

    elif num_user > num_sorteado:
        chances -= 1
        texto_resultado["text"] = "Numero mais alto que o escolhido,  Você ainda tem "+ str(chances)+ " chances"

    else:
        texto_resultado["text"] = "Vc acertou!!! O Número escolhido era: "+ str(num_sorteado)

    if chances == 1:
       texto_resultado["text"] = "Infelizmente Voce não acertou, que pena, Tente novamente mais tarde"
       texto_botao["command"] = "jogo.destroy"


jogo = Tk()
jogo.title("Jogo de Advinhação")
texto_inicial = Label(jogo, text="Advinhe um numero entre 1 e 100")
texto_inicial.grid(column=0,row=0, padx=5,pady=5)

entry_numero = Entry(jogo)
entry_numero.grid(column=0,row=1, padx=5,pady=5)

texto_botao = Button(jogo, text="Teste agora",command=advinhar)
texto_botao.grid(column=0,row=2)

texto_resultado = Label(jogo, text="")
texto_resultado.grid(column=0,row=4,padx=5,pady=5)

texto_botao2 = Button(jogo, text="Jogue de novo",command=advinhar)
texto_botao2.grid(column=0,row=3,pady=1,padx=1)

jogo.mainloop()

