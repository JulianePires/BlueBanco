def alterarDados(dados):
	
	data = ""
	
	while data != "Cancelar" and data != "cancelar":
		
		data = input("Escolha uma das opções: | Senha | Idade | Endereço | Cancelar\n")

		if data == "Usuario" or data == "usuario":
			newUser = input("Digite um novo nome de usuário: \n")
			while newUser == "":
				print("Usuário inválido\n")
			dados["usuario"] = newUser

		elif data == "Idade" or data == "idade":
			newAge = int(input("Digite uma nova idade: \n"))
			while newAge <= 12 :
				newAge = int(input("Idade incorreta! Digite uma nova idade: \n"))
			dados["idade"] = newAge

		elif data == "Endereço" or data == "endereco":
			newAddress = input("Digite um novo endereço: ")
			while newAddress == "":
				print("Endereço inválido")
			dados["endereco"] = newAddress

		elif data != "Cancelar" or data != "cancelar":
			data = input("Opção Inválida! Escolha uma das opções: Usuário | Idade | Endereço | Cancelar\n")

		print("Dados alterados com sucesso!\n")