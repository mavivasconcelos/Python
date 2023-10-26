def calcular_tempo_entrega (distancia, velocidade):
  tempo_entrega = ((distancia/velocidade)*60)+5
  return tempo_entrega

def calcular_taxa_tempo (tempo_entrega):
  if tempo_entrega > 60:
    taxa_entrega = 0
  elif tempo_entrega <= 60 or tempo >= 30:
    taxa_entrega = 3
  elif tempo_entrega < 30:
    taxa_entrega = 5
  return taxa_entrega

def gerar_recibo(nome_cliente, comida_pedida, taxa_entrega):
  if comida_pedida == "pizza":
    custo_comida = 20
    total_pago = taxa_entrega + custo_comida
  return total_pago
  
distancia = float(input("Digite distancia em KM: "))
velocidade = float(input("Digite velocidade em KM/h: "))
nome_cliente = input("Digite nome de cliente: ")
comida_pedida = input("Digite comida pedida: ")

tempo_entrega = calcular_tempo_entrega(distancia, velocidade)
taxa_entrega = calcular_taxa_tempo(tempo_entrega)
total_pago = gerar_recibo(nome_cliente, comida_pedida, taxa_entrega)

print (f"\nNome do cliente: {nome_cliente}\nComida pedida: {comida_pedida}\nTaxa de entrega: {total_pago}")