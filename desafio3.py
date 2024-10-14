import json

def analisa_faturamento(faturamento_diario):
    # Filtra os dias com faturamento (ignorando os dias sem faturamento)
    faturamento_validos = []
    for valor in faturamento_diario:
        if valor['valor'] > 0:
            faturamento_validos.append(valor['valor'])
    if not faturamento_validos:
        return None, None, 0  # Retorna None se não houver faturamento

    # Calcula o menor e maior faturamento
    menor_faturamento = min(faturamento_validos)
    maior_faturamento = max(faturamento_validos)

    # Calcula a média mensal
    media_mensal = sum(faturamento_validos) / len(faturamento_validos)

    # Contabiliza os dias com faturamento superior à média
    dias_acima_media = 0
    for valor in faturamento_validos:
        if valor > media_mensal:
            dias_acima_media +=1

    return menor_faturamento, maior_faturamento, dias_acima_media

if __name__ == "__main__":
    # Lê os dados do arquivo JSON
    with open('faturamento.json', 'r') as file:
        data = json.load(file)

    faturamento_diario = data['faturamento']

    menor, maior, dias_acima_media = analisa_faturamento(faturamento_diario)

    if menor is not None:
        print(f"Menor faturamento do mês: R$ {menor}")
        print(f"Maior faturamento do mês: R$ {maior}")
        print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
    else:
        print("Não há faturamento válido para analisar.")
