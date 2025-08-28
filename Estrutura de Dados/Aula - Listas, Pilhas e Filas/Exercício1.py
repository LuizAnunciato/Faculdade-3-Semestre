#Exercício 1 - Último a Entrar, Primeiro a Sair

#Lista Vazia
pilha = []

print(f"Pilha vazia? {not pilha}")
print()
#Operação "Push"
#Empilhar
pilha.append(10)
pilha.append(20)
pilha.append(30)

print(f"Pilha depois do Push: {pilha}")
print()

#Operação Top
#Acessa o último elemento da lista
topo = pilha[-1]
print(f"Elemento no topo: {topo}")
print()

#Operação desempilhar
desempilhar = pilha.pop()
print(f"Pilha depois do Pop: {pilha}")
print()

#Verificar se a lista está vazia
if not pilha:
    print("A pilha está vazia")
else:
    print("A pilha não está vazia")
