# Gerado com o prompt:
# "Crie uma função em Python que calcule o total de itens,
# valor bruto, desconto, valor de entrega e valor final de um pedido."

def calcular_pedido(itens, tipo_entrega):
    total_itens = sum(i["quantidade"] for i in itens)
    valor_bruto = sum(i["quantidade"] * i["preco_unitario"] for i in itens)

    desconto = 0.0
    if valor_bruto >= 100:
        desconto = valor_bruto * 0.10

    valor_entrega = 10.0 if tipo_entrega == "normal" else 20.0
    valor_final = valor_bruto - desconto + valor_entrega

    return {
        "total_itens": total_itens,
        "valor_bruto": round(valor_bruto, 2),
        "desconto": round(desconto, 2),
        "valor_entrega": valor_entrega,
        "valor_final": round(valor_final, 2),
    }