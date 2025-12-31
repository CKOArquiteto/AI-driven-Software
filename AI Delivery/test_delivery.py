# Gerado com o prompt:
# "Crie testes unitários em Pytest para a função calcular_pedido
# usando dados simulados de pedidos."

from delivery import calcular_pedido

def test_pedido_com_desconto():
    itens = [
        {"quantidade": 2, "preco_unitario": 30.0},
        {"quantidade": 1, "preco_unitario": 50.0},
    ]

    r = calcular_pedido(itens, "normal")

    print(r, "resultado - desconto")

    assert r["total_itens"] == 3
    assert r["valor_bruto"] == 110.0
    assert r["desconto"] == 11.0
    assert r["valor_entrega"] == 10.0
    assert r["valor_final"] == 109.0


def test_pedido_sem_desconto():
    itens = [
        {"quantidade": 1, "preco_unitario": 40.0},
    ]

    r = calcular_pedido(itens, "expressa")
    
    print(r, "resultado - s/desconto")

    assert r["desconto"] == 0.0
    assert r["valor_entrega"] == 20.0
    assert r["valor_final"] == 60.0