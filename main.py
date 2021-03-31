import deposito
import saque
import consultarSaldo
import consultarDados
import alterarDados

print("<<< Bem-vinde ao BlueBank, o seu azulzinho >>>\n\n")
user = input("Usuário: ")

while user == "":
	user = input("Usuário inválido! O usuário não pode estar em branco. Digite um novo usuário: ")

password = input("Senha: ")

while password.lenght < 6:
	password = input("Senha inválida! Sua senha deve ter um mínimo de 6 caracteres. Digite uma nova senha: ")

age = int(input("Informe a sua idade: "))

while age < 12:
	user = input("Idade inválida! A idade mínima para acesso aos serviços é de 13 anos. Informe a sua idade: ")

address = input("Muito bem! Agora informe o seu endereço: ")

while user == "":
	user = input("Endereço inválido! O endereço não pode estar em branco. Digite um novo endereço: ")

print("Você adentrou a matriz da BlueBank, te daremos algumas opções para que você possa desfrutar dos nossos serviços \n\n")

dados = {"usuario": user, "idade": age, "endereço": address}
saldo = float
saldo = 1000
command = ""

while command != "sair":
	
	print("Bem-vinde ao sistema superinteligente da Blue, digite uma das opções de comando: \n\n deposito | saque | consultasaldo | consultadados alterardados | sair")
	
	if command == "deposito":
		novoValor = float(input("Digite o novo valor a ser depositado: "))
		if novoValor <= 0:
			novoValor = float(input("Valor inválido! Digite o novo valor a ser depositado: "))
		saldo = deposito.deposito(novoValor)
	
	if command == "saque":
		valorSaque = float(input("Digite um valor a ser sacado: "))
		if valorSaque > saldo:
			valorSaque = float(input("Valor abaixo do saldo atual. Digite um valor acima do saldo atual: "))
		saldo = saque.saque(valorSaque)

	if command == "consultasaldo":
		consultarSaldo.consultarSaldo()
	
	if command == "consultadados":
		consultarDados.consultarDados()
	
	if command == "alterardados":
		alterarDados.alterarDados()
