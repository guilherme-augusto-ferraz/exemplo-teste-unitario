import unittest

from exemplo import PedidoService


class PedidoRepositoryFake:
    def __init__(self):
        self.salvos = []

    def salvar(self, pedido):
        self.salvos.append(pedido)


class TestPedidoService(unittest.TestCase):
    def setUp(self):
        self.repo = PedidoRepositoryFake()
        self.service = PedidoService(self.repo)

    def test_criar_pedido_salva_com_status_pendente(self):
        pedido = self.service.criar_pedido(cliente_id=101, itens=[{"nome": "caneta", "qtd": 2}])

        self.assertEqual(pedido["cliente_id"], 101)
        self.assertEqual(pedido["status"], "pendente")
        self.assertEqual(len(self.repo.salvos), 1)
        self.assertEqual(self.repo.salvos[0], pedido)

    def test_criar_pedido_sem_itens_retorna_lista_vazia(self):
        pedido = self.service.criar_pedido(cliente_id=202, itens=[])

        self.assertEqual(pedido["cliente_id"], 202)
        self.assertEqual(pedido["itens"], [])
        self.assertEqual(pedido["status"], "pendente")


if __name__ == "__main__":
    unittest.main()
