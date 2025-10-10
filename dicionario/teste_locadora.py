import os
os.system('cls')

estoque_veiculos = {
    "001": {"modelo": "Chevrolet Tracker", "valor_diaria": 120},
    "002": {"modelo": "Chevrolet Onix", "valor_diaria": 90},
    "003": {"modelo": "Chevrolet Spin", "valor_diaria": 150},
    "004": {"modelo": "Hyundai HB20", "valor_diaria": 85},
    "005": {"modelo": "Hyundai Tucson", "valor_diaria": 120},
    "006": {"modelo": "Fiat Uno", "valor_diaria": 60},
    "007": {"modelo": "Fiat Mobi", "valor_diaria": 70},
    "008": {"modelo": "Fiat Pulse", "valor_diaria": 130}
}

veiculos_alugados = {}

def boas_vindas():
  print('Seja bem vindo! Aqui temos uma boa opção pra você!')
  print('=='*60)
  return ""

def abre_opcoes():
  print("Diga como podemos ajudar.")
  print('Selecione uma das opções a seguir:')
  print('1 - Alugar um dos veículos')
  print('2 - Devolver veículo alugado')
  print('3 - sair')
  print('--'*30)

def exibir_veiculos_disponiveis(estoque_veiculos):
  for carro, modelo in estoque_veiculos.items():
    print(f"Código: {carro} - Modelo: {modelo['modelo']} => Diária R$ {modelo['valor_diaria']}")
  print('--'*30)
  return

def exibir_veiculos_alugados(veiculos_alugados):
  for carro, modelo in veiculos_alugados.items():
    print(f"Código: {carro} - Modelo: {modelo['modelo']} => Diária R$ {modelo['valor_diaria']}")
  print('--'*30)
  

def seleciona_opcao():
  while True:
        selecao = input("Selecione a opção desejada (1-3): ")
        if selecao in ['1', '2', '3']:
            return selecao
        print("Opção inválida! Digite 1, 2 ou 3.")

def seleciona_veiculo():
  selecao_veiculo = input('Digite o código do veículo: ')
  if selecao_veiculo in estoque_veiculos:
    modelo = estoque_veiculos[selecao_veiculo]
    print(f'{selecao_veiculo} = Modelo: {modelo['modelo']} => R$ {modelo['valor_diaria']}')
    return selecao_veiculo
  else:
    print('Modelo inválido ou indisponível')

while True:
  boas_vindas()
  abre_opcoes()
  selecao = seleciona_opcao()
  if selecao == '3':
    print("="*70)
    print("Muito obrigado e espero que volte em outra oportunidade")
    print("="*70)
    break
  elif selecao == "1":
    exibir_veiculos_disponiveis(estoque_veiculos)
    codigo = seleciona_veiculo()
    if codigo not in estoque_veiculos:
      print('*** Veículo não disponível ***')

    if codigo:
      confirma_modelo = input('Confirma opção? s / n: ')
      if confirma_modelo.lower() == "s":
        diarias = int(input('Quantas diárias? '))
        if diarias <=0:
          print("Numero de diárias deve ser maior que zero")
          continue
        diaria = estoque_veiculos[codigo]['valor_diaria']
        total_a_pagar = diarias * diaria
        print(f'Total a pagar: R$ {total_a_pagar:.2f}')
        confirma_aluguel = input('Confirma locação? s/n ')
        if confirma_aluguel.lower() == "s":
          veiculo_movido = estoque_veiculos.pop(codigo)
          veiculos_alugados[codigo] = veiculo_movido
          print('----------------------------------------------------------------------------------')
          print(f"Parabéns, você alugou o {veiculos_alugados[codigo]['modelo']} por {diarias} dias.")
          print('----------------------------------------------------------------------------------')
          print('')
          print('')
          os.system('cls')

  elif selecao == "2":
    if len(veiculos_alugados) == 0:
      print('Não há veiculos para devolução')
      print('*'*60)
      continue
    else:
      exibir_veiculos_alugados(veiculos_alugados)
      print('Selecione o veículo que vai devolver:')

      selecao_veiculo = input('Digite o código do veículo: ')

      if selecao_veiculo in veiculos_alugados:
        modelo = veiculos_alugados[selecao_veiculo]
        print(f'{selecao_veiculo} = Modelo: {modelo["modelo"]} => R$ {modelo["valor_diaria"]}')
        codigo_devolucao = selecao_veiculo
      else:
        print('*** Veículo não está alugado ou código inválido ***')
        continue
    
      confirma_devolucao = input('Confirma devolução? s/n ')
      if confirma_devolucao.lower() == "s":
        veiculo_devolvido = veiculos_alugados.pop(codigo_devolucao)
        estoque_veiculos[codigo_devolucao] = veiculo_devolvido
        print('Muito obrigado por devolver o veículo e esperamos vê-lo novamente!')
        print("---"*40)
        os.system('cls')