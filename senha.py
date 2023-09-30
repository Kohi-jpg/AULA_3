nome_digitado = input('Digite o nome:\n')
senha_digitada = input("Digite a senha\n")
senha = '1234'
nome = 'camila'

if senha_digitada == senha and nome == 'camila':
    print("acesso permitido")
else:
    print(f"acesso negado, verifique se você digitou a senha: {senha_digitada} ou o nome: {nome_digitado} foram digitados corretamente")

    