import pytest

from exemplo_lista_pedidos import total_pedido

def test_preço_primeiro_produtos():
    assert total_pedido (100) == 9.00
# def test_soma_todos():
#    assert total_pedido ([100, 101, 102, 103, 104, 105, 200, 201]) == 84.00    