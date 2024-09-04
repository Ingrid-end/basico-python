# Usamos main como arquivo principal pelas boas praticas no python!

# INPUT
nome =input("animal preferido")
idade = int( input("idade animal") )
peso = float( input("peso animal") )

print(nome)
print(idade)
print(peso)

# OPERADORES
soma = 1+1
mult = 2*2
divisao = 20 / 2
potencia = 7 ** 2

print("soma", soma)
print("mult", mult)
print("divisao", divisao)
print("potencia", potencia)

# CONDICIONAIS
idade = int( input("digite sua idade:") )
if idade >= 18:
    print("permitido entrar!")
else:
    print("NÃO PODE ENTRAR!")

salario = float( input("informe teu salario:") )
if salario <= 3000:
    print("programador junior")
elif salario > 3000 and salario <= 6000:
    print("promagramdor pleno")
elif salario > 6000 and salario <= 15000:
    print("programador senior")
else:
    print("gerente de projetos")

# LISTAS
lista_numeros = [1,2,3]

lista_numeros[0]= 5

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])

# funções(metodos) LISTAS
numeros = [10,9,8,7,6]
# total itens da lista
print("total:", len(numeros))
# menor valor
print("total:", min(numeros))
# maior valor
print("total:", max(numeros))



# REPETIÇÕES
# LOOOP 
notas = []
for x in range(5):
    codigo_aluno = input("rm: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno,nota]
    # colocando o resultado na lita de notas
    notas.append(resultado)
    # lista de notas a posição 0 é o codigo do aluno e a posição 1 a nota,
print("quantidade de notas", len(notas) )

# Fazemos outra lista, pegando o codigo do aluno na posição 0 da lista de notas e a posição 1 que é a nota
for n in notas:
    codigo_aluno = n [0]
    nota = n [1]
    print("O RM", codigo_aluno, "tirou a nota:", nota)
    
    
# DICIONARIOS

player={
    "nome":"Fulaninho",
    "level": "2",
}
# lista de dicionarios
npcs = [
 {"nome":"monstrinho", "dano":6},   
 {"nome":"flavinha", "dano":6} ,
 {"nome":"alemanha", "dano":6} ,
]

# FUNÇÕES
def minha_funcao(valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = int(input("valor1: "))
    valor2 = int(input("valor2: "))
    
    resposta = minha_funcao(valor1,valor2)
    print(valor1, "+", valor2, "=", resposta)