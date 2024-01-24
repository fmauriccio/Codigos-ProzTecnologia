while True:
    print("Olá, vamos calcular?")
    print("Escolha uma das operações básicas abaixo: ")
    print("1 - ADIÇÃO")
    print("2 - SUBTRAÇÃO")
    print("3 - MULTIPLICAÇÃO")
    print("4 - DIVISÃO")
    print("Ou digite '5' para SAIR!")

    escolha = input("Digite a opção desejada: ")

    if escolha == "5":
        print("Saindo do sistema, volte sempre!")
        break

    elif escolha == "1":
        print ("OPERAÇÃO DE ADIÇÃO ESCOLHIDA!")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"O resultado da operação é: {resultado}")

    elif escolha == "2":
        print ("OPERAÇÃO DE SUBTRAÇÃO ESCOLHIDA!")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"O resultado da operação é: {resultado}")

    elif escolha == "3":
        print ("OPERAÇÃO DE MULTIPLICAÇÃO ESCOLHIDA!")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"O resultado da operação é: {resultado}")

    elif escolha == "4":
        print ("OPERAÇÃO DE DIVISÃO ESCOLHIDA!")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 / num2
        print(f"O resultado da operação é: {resultado}")

    else:
        print("Opção inválida! Escolha uma opção válida!")
        