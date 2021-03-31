from main import dados

def alterarDados():
	data = ""
	while data != "Cancelar":
		data = input("Escolha uma das opções: | Senha | Idade | Endereço | Cancelar")

		if data != "Usuário" or data != "Senha" or data != "Idade" or data != "Endereço":
			data = input("Opção Inválida! DEscolha uma das opções: Usuário | Idade | Endereço | Cancelar")
		
		if data == "Usuario":
			newUser = input("Digite um novo nome de usuário: ")
			if newUser == "":
				print("Usuário inválido")
			dados["usuario"] = newUser

		if data == "Idade":
			newAge = input("Digite uma nova idade: ")
			if newAge <= 12 :
				print("Idade incorreta")
			dados["idade"] = newAge

		if data == "Endereço":
			newAddress = input("Digite um novo endereço: ")
			if newAddress == "":
				print("Endereço inválido")
			dados["endereco"] = newAddress

		print("Dados alterados com sucesso!")