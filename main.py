lista = []

class Produto:
  def __init__(self, nome, valor, marca):
    self.nome = nome
    self.valor = valor
    self.marca = marca

while True:
  option = int(input('''
-----lista de Compras-----
1-Adicionar Item na Lista
2-Remover Item da Lista
3-Mostrar Lista Completa
4-Finalizar Programa
--------------------------
Digite uma das opções acima: '''))
  print("--------------------------")

  if option == 1:
    nwNome = str(input("Digite o nome do produto: "))
    nwValor = float(input("Digite o valor do produto: "))
    nwMarca = str(input("Digite a marca do produto: "))
    nwProduto = Produto(nwNome, nwValor, nwMarca)
    lista.append(nwProduto)
    print("--------------------------")
    print("-Item adicionado-")

  if option == 2:
    rmProduto = str(input("Digite o nome do item que deseja remover: "))
    for id, char in enumerate(lista):
      if char.nome == rmProduto:
        del lista[id]
        print("--------------------------")
        print("-Item removido-")
      else:
        print("--------------------------")
        print("-Item não encontrado-")

  if(option == 3):
    for id, char in enumerate(lista):
      print("--------------------------")
      print("{}-".format(id + 1))
      print("Nome: {}".format(char.nome))
      print("Valor: {}".format(char.valor))
      print("Marca: {}".format(char.marca))

  if option == 4:
    print("Finalizando programa...")
    break