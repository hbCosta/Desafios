def calcular_percentuais(faturamento):
    total_faturamento = sum(faturamento.values())  # Calcula o total de faturamento

    percentuais = {}
    for estado, valor in faturamento.items():
        percentual = (valor/total_faturamento) * 100
        percentuais[estado] = percentual

    return percentuais, total_faturamento

if __name__ == "__main__":
    # Faturamento mensal detalhado por estado
    faturamento_mensal = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    percentuais, total = calcular_percentuais(faturamento_mensal)

    print(f"Faturamento total: R$ {total:.2f}\n")
    print("Percentual de representação por estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")
