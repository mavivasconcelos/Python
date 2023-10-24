#Validador de CPF
pergunta_cpf = list(input("Digite seu CPF. Apenas os dígitos: "))
lista_cpf = []
for i in pergunta_cpf:
    lista_cpf.append(int(i))

validacao1 = []
x = 10
for digito in lista_cpf [:9]:
  i = digito * x
  validacao1.append(i)
  x -= 1
soma1 = sum (validacao1)

validacao2 = []
y = 11
if (soma1*10)%11 == lista_cpf[9]:
  for digito in lista_cpf [:10]:
    i = digito * y
    validacao2.append(i)
    y -= 1
  soma2 = sum (validacao2)

  if (soma2*10)%11 == lista_cpf[10]:
    print ("CPF válido")
else:
  print ("CPF inválido")