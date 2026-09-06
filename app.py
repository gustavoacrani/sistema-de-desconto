# Sistema de desconto progressivo para uma loja online

# Solicita ao usuário o valor total da compra
valor_compra = float(input("Digite o valor total da compra (R$): "))

# Verifica a faixa de valor da compra e define o percentual de desconto
if valor_compra <= 0:
    print("Valor inválido. O valor da compra deve ser maior que zero.")
else:
    if valor_compra < 200:
        desconto_percentual = 0.05  # 5% de desconto
    elif valor_compra < 300:
        desconto_percentual = 0.10  # 10% de desconto
    else:
        desconto_percentual = 0.15  # 15% de desconto

    # Calcula o valor do desconto e o valor final da compra
    valor_desconto = valor_compra * desconto_percentual
    valor_final = valor_compra - valor_desconto

    # Exibe os resultados para o usuário
    print("\n====== RESUMO DA COMPRA ======")
    print(f"Valor da compra: R$ {valor_compra:.2f}")
    print(f"Desconto aplicado: R$ {valor_desconto:.2f} ({desconto_percentual * 100:.0f}%)")
    print(f"Valor final a pagar: R$ {valor_final:.2f}")