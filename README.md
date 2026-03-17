## Exemplo de Projeto para Testes Unitários

Este projeto é um exemplo para a disciplina de Qualidade de Software.

## Estrutura

- `exemplo.py`: classe `PedidoService` com método `criar_pedido`.
- `test_pedido_service.py`: testes unitários com `unittest`.
- `.github/workflows/python-tests.yml`: GitHub Actions para rodar testes.

## Como rodar localmente

```bash
python -m unittest discover -s . -p "test*.py"
```

## Tarefa para alunos

1. Adicionar um novo teste em `test_pedido_service.py` que verifique o comportamento quando `itens` é `None` ou quando `cliente_id` não é inteiro.
2. Configurar a execução no GitHub Actions (já configurado em `.github/workflows/python-tests.yml`).
3. Cadastrar as alterações em um branch e abrir pull request.
