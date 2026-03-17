class PedidoService:
    def __init__(self, pedido_repository):
        self.pedido_repository = pedido_repository

    def criar_pedido(self, cliente_id, itens):
        # Lógica para criar um pedido
        pedido = {
            'cliente_id': cliente_id,
            'itens': itens,
            'status': 'pendente'
        }
        self.pedido_repository.salvar(pedido)
        return pedido