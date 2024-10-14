def fibonacci_e_verificacao(numero):
    fibo = []

    for i in range(numero):
        if i == 0:
            fibo.append(0)  # Adiciona 0 para o primeiro número da sequência
        elif i == 1:
            fibo.append(1)  # Adiciona 1 para o segundo número da sequência
        else:
            fibo.append(fibo[i - 1] + fibo[i - 2])  # Adiciona a soma dos dois anteriores

    print(fibo)

    # Verifica se o número informado está na sequência de Fibonacci
    if numero in fibo:
        print(f"Número {numero} está presente na sequência de Fibonacci.\n")
    else:
        print(f"Número {numero} não está presente na sequência de Fibonacci.\n")

if __name__ == "__main__":
    numero = int(input("Digite um número: "))
    fibonacci_e_verificacao(numero)
