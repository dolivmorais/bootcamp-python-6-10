# calculadora


def calculadora(opracao, n1, n2):
    if opracao == "+":
        soma = n1 + n2
        return soma
    elif opracao == "-":
        subtracao = n1 - n2
        return subtracao
    elif opracao == "*":
        mult = n1 * n2
        return mult
    elif opracao == "/" and n2 == 0:
        print("Erro, divisão por zero")
    elif opracao == "/":
        divisao = n1 / n2
        return divisao


print(calculadora("/", 2, 2))
