# Documento Descritivo do Sistema de Estoque
Introdução
O sistema modela o "Sistema de Estoque", uma solução para gerenciamento de estoque de uma empresa de varejo. Os usuários são administradores (tipo 'admin'), com controle total de cadastros e exclusões, e usuários comuns (tipo 'user'), limitados a atualizações próprias e cadastros básicos de produtos. A empresa oferece produtos com controle de nome, quantidade em estoque e valor unitário, suportando operações de estoque via interface em terminal.​

## Implementação: Usuários
### Estrutura de Dados
Dados carregados em dicionário com chave como login (str) e valor como tupla nomeada Usuario (campos: login, senha, tipo). Permite busca O(1) por login.​

### Estrutura do Arquivo
Arquivo usuarios.txt em CSV: cada linha contém login,senha,tipo (ex: "admin123,senha123,admin"), sem cabeçalho, lido/escrito via csv.reader/writer.​

### Funcionalidades
- Ler usuários do arquivo (R).
- Fazer login validando credenciais (R).
- Cadastrar usuário novo, admins só por admin logado (C).
- Excluir usuário reescrevendo arquivo (D).
- Atualizar senha, users só própria (U).​

## Implementação: Produtos
### Estrutura de Dados
Dicionário com chave como nome do produto (str) e valor como tupla nomeada Produto (campos: produto, qtd int, valor float). Facilita listagem e atualizações.​

## Estrutura do Arquivo
Arquivo produtos.txt em CSV: linhas com produto,qtd,valor (ex: "camiseta,50,29.90"), sem cabeçalho, com validação de tipos na entrada.​

### Funcionalidades
- Ler e imprimir lista de produtos (R).
- Cadastrar produto novo por usuários logados (C).
- Atualizar qtd/valor, apenas por admins (U).
- Excluir produto reescrevendo arquivo (D)

## Conclusão
Um trabalho divertido, apesar do desafio de utilizar cores e elementos visuais para melhor clareza e estética foi bom colocar em prática elementos de console e CLI. Se fosse pra refazer eu implementaria algum tipo de saída que não buga a tabela de produtos quando tem grandes nomes ou valores... além de uma melhor validação dos dados de entrada.