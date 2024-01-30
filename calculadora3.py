num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
print(f"Os número escolhidos para o calculo foram {num1} e {num2}")
print("Agora escolha qual a operação aritimética:\n1 - ADIÇÃO\n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO")
operacao = int(input("Insira o número referente a sua escolha: "))

def calculadora(num1, num2, operacao):
    if operacao == 1:
        resultado = num1 + num2
        print(f"Resultado: {resultado}")
    elif operacao == 2:
        resultado = num1 - num2
        print(f"Resultado: {resultado}")
    elif operacao == 3:
        resultado = num1 * num2
        print(f"Resultado: {resultado}")
    elif operacao == 4:
        if num2 != 0:  
            resultado = num1 / num2
            print(f"Resultado: {resultado}")
        else:
            print("Erro: divisão por zero.")
            return 0
    else:
        print("Operação inválida. Escolha um número de 1 a 4.")
        return 0
calculadora(num1, num2, operacao)