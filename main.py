import deposito
import saque
import consultarSaldo
import consultarDados
import alterarDados

print("<<< Bem-vinde ao BlueBank, o seu azulzinho >>>\n\n")

user = input("Usuário: \n")
while user == "":
	user = input("Usuário inválido! O usuário não pode estar em branco. Digite um novo usuário: \n")

password = input("Senha: \n")
while len(password) < 6:
	password = input("Senha inválida! Sua senha deve ter um mínimo de 6 caracteres. Digite uma nova senha: \n")

age = int(input("Informe a sua idade: \n"))
while age < 12:
	age = int(input("Idade inválida! A idade mínima para acesso aos serviços é de 13 anos. Informe a sua idade: \n"))

address = input("Muito bem! Agora informe o seu endereço: \n")
while address == "":
	address = input("Endereço inválido! O endereço não pode estar em branco. Digite um novo endereço: \n")

print("Você adentrou a matriz da BlueBank, te daremos algumas opções para que você possa desfrutar dos nossos serviços \n\n")

dados = {"usuario": user, "idade": age, "endereco": address}
saldo = 1000
command = ""

while command != "sair":
	
	command = input("Bem-vinde ao sistema superinteligente da Blue, digite uma das opções de comando: \n\n deposito | saque | consultasaldo | consultadados | alterardados | sair\n")
	
	if command == "deposito":
		novoValor = float(input("Digite o novo valor a ser depositado: \n"))
		while novoValor <= 0:
			novoValor = float(input("Valor inválido! Digite o novo valor a ser depositado: \n"))
		saldo = deposito.deposito(novoValor, saldo)
	
	if command == "saque":
		valorSaque = float(input("Digite um valor a ser sacado: "))
		while valorSaque > saldo:
			valorSaque = float(input("Valor acima do saldo atual. Digite um valor abaixo do saldo atual: \n"))
		saldo = saque.saque(valorSaque, saldo)

	if command == "consultasaldo":
		consultarSaldo.consultarSaldo(saldo)
	
	if command == "consultadados":
		consultarDados.consultarDados(dados)
	
	if command == "alterardados":
		alterarDados.alterarDados(dados)
	
