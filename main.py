import time

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
    if len(lista) > 0:
      for id, char in enumerate(lista):
        if char.nome == nwProduto.nome:
          print("--------------------------")
          print("-Item com mesmo nome encontrado-")
          rm = str(input("Deseja removê-lo? y/n >"))
          if rm == "y":
            del lista[id]
            print("-Item removido e substituido-")
            lista.append(nwProduto)
            break
          if rm == "n":
            print("-Ok, item antigo mantido-")
            break
    else:
      lista.append(nwProduto)
      print("--------------------------")
      print("-Item removido-")

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
    if len(lista) == 0:
      print("--------------------------")
      print("-Não há nenhum item na lista-")

  if option == 4:
    print("Finalizando programa...")
    break
  
  time.sleep(0.5)