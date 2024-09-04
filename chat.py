# colocando em pratica

# OS é uma variavel do python usada para interagir com o sistema operacional
import os

mensagem = []

nome = input("nome: ")

# loop infinito = "enquanto for verdadeiro" (a condição do true sempre sera true(verdadeiro) )
while True:
    # limpar o terminal
    os.system('cls')
    
    # So vai exibir informações se tiver pelo meno um iten cadastrado
    if len(mensagem) > 0:
        for m in mensagem:
            print(m['nome'], "-", m['texto'] )
            
            # separar a lista de mensagem 
    print("_______________")
            
    texto = input("mensagem: ")
    if texto == "fim":
            # quebrar o loop
        break
            
        # adicionando mensagem na lista
    mensagem.append({
        "nome":nome,
        "texto": texto
        })