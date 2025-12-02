import csv
from collections import namedtuple
from getpass import getpass

from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel


## constantes
ARQUIVO_USUARIOS = 'usuarios.txt'
ARQUIVO_PRODUTOS = 'produtos.txt'
USUARIO_LOGADO = None

##################### Funções de usuário #####################

##### CRUD Read
# Função para ler usuários de um arquivo CSV.
# Parâmetro: arquivo_csv (str) - caminho do arquivo CSV.
# Retorno: dict - dicionário com logins como chaves e tuplas nomeadas Usuario como valores.
# conheça as tuplas nomeadas: https://www.geeksforgeeks.org/namedtuple-in-python/
def ler_usuarios(arquivo_csv):
    Usuario = namedtuple('Usuario', ['login', 'senha', 'tipo'])
    usuarios = {}
    
    with open(arquivo_csv, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            nome_usuario, senha, tipo = row
            usuarios[nome_usuario] = Usuario(login=nome_usuario,senha=senha, tipo=tipo)
    
    return usuarios


##### CRUD Read
# Função para realizar login de um usuário.
# Atualiza a variável global USUARIO_LOGADO em caso de login bem sucedido.
# Parâmetro: usuarios (dict) - dicionário de usuários.
# Retorno: None
def fazer_login(usuarios):
    # preciso explicitar o acesso à variável global
    # senão a atribuição ao final da função criará uma nova variável local
    global USUARIO_LOGADO

    console.print(Panel('''🟢 [bold green]Login[/bold green] 🟢\n\nPor favor, insira suas credenciais.''', 
                        expand=False, title="Tela de Login"))
    username = Prompt.ask("[bold cyan]Nome de Usuário[/bold cyan]")
    senha = getpass("Senha: ")

    user = usuarios.get(username, None)
    if user is not None and user.senha == senha:
        console.print("\n[bold green]Login bem-sucedido![/bold green]")
        USUARIO_LOGADO = user
    else:
        console.print(f"[bold red]Erro: usuário ou senha incorretos!", style="red")



##### CRUD Create
# Função para cadastrar um novo usuário.
# Parâmetros: 
#   usuarios (dict) - dicionário de usuários.
#   arquivo_csv (str) - caminho do arquivo CSV.
# Retorno: str - nome do novo usuário ou False em caso de falha.
def cadastrar_usuario(usuarios, arquivo_csv):
    console.print(Panel('''[bold green]Cadastro de Novo Usuário[/bold green]\nPor favor, insira os dados do novo usuário.''', 
                        title="Novo Usuário", expand=False))

    nome_usuario = Prompt.ask("[bold cyan]Nome de Usuário[/bold cyan]")
    senha = getpass("Senha: ")

    # controle de acesso permite criação de novos admins somente se usuário logado é admin
    if USUARIO_LOGADO is not None and USUARIO_LOGADO.tipo == 'admin':
        tipo = Prompt.ask("[bold cyan]Tipo de Usuário (admin/user)[/bold cyan]") 
    else:
        tipo = 'user'

    if usuarios.get(nome_usuario, None) is not None:
        console.print(f"[bold red]Erro:[/bold red] Usuário '[bold red]{nome_usuario}[/bold red]' já existe!", style="red")
        return False
    else: 
        with open(arquivo_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nome_usuario, senha, tipo]) 
        console.print(f"[bold green]Usuário '{nome_usuario}' cadastrado com sucesso![/bold green]")

    return nome_usuario

##### CRUD Delete
# Parâmetros: 
#   usuarios (dict) - dicionário de usuários.
#   arquivo_csv (str) - caminho do arquivo CSV.
# Retorno: bool - True se o usuário foi excluído com sucesso, False caso contrário.
def excluir_usuario(usuarios, arquivo_csv):
    console.print(Panel('''[bold red]Exclusão de Usuário[/bold red]\nPor favor, insira o nome do usuário a ser excluído.''', 
                        title="Excluir Usuário", expand=False))
    nome_usuario = Prompt.ask("[bold cyan]Nome de Usuário[/bold cyan]")

    # se encontrar o usuário, remova do arquivo
    if usuarios.get(nome_usuario, None) is not None:
        with open(arquivo_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            for usuario in usuarios.values():
                if usuario.login != nome_usuario:
                    writer.writerow([usuario.login, usuario.senha, usuario.tipo]) 
        console.print(f"[bold green]Usuário '{nome_usuario}' excluído com sucesso![/bold green]")
        return True
    else:
        console.print(f"[bold yellow]Usuário '{nome_usuario}' não encontrado![/bold yellow]", style="yellow")
        return False
    

##### CRUD Update
# Função para atualizar a senha de um usuário.
# controle de acesso permite a admins alterar a senha de qualquer usuário
# e users podem apenas alterar a própria senha.
# Parâmetros: 
#   usuarios (dict) - dicionário de usuários.
#   arquivo_csv (str) - caminho do arquivo CSV.
# Retorno: bool - True se a senha foi atualizada com sucesso, False caso contrário.
def atualiza_senha(usuarios, arquivo_csv):
    global USUARIO_LOGADO

    if USUARIO_LOGADO is None:
        print('Essa função não deve ser chamada sem um usuário logado!!!')
        return False

    if USUARIO_LOGADO.tipo == 'user':
        console.print(Panel('''[bold yellow]Atualização de Senha[/bold yellow]\nPor favor, informe a nova senha desejada.''', 
                            title="Atualizar Senha", expand=False))
        nome_usuario = USUARIO_LOGADO.login
    else:
        console.print(Panel('''[bold yellow]Atualização de Senha[/bold yellow]\nPor favor, insira o nome do usuário cuja senha será atualizada.''', 
                            title="Atualizar Senha", expand=False))

        nome_usuario = Prompt.ask("[bold cyan]Nome de Usuário[/bold cyan]")
    
    nova_senha = getpass("Nova senha: ")

    if usuarios.get(nome_usuario, None) is not None:
        with open(arquivo_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            for _, usuario in usuarios.items():
                if usuario.login != nome_usuario:
                    writer.writerow([usuario.login, usuario.senha, usuario.tipo])
                else:
                    writer.writerow([usuario.login, nova_senha, usuario.tipo])
        console.print(f"[bold green]Usuário '{nome_usuario}' Atualizado com sucesso![/bold green]")
        return True
    else:
        console.print(f"[bold yellow]Usuário '{nome_usuario}' não encontrado![/bold yellow]", style="yellow")
        return False
##################### FIM FUNÇÕES DE USUARIO ########################

#####################  FUNÇÕES DE PRODUTO    ########################

#######  READ VENDAS   ####
def ler_produtos(arquivo_csv):
    Produto = namedtuple('produto', ['produto','qtd', 'valor'])
    produtos={}
    
    with open(arquivo_csv, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            produto, qtd, valor = row
            produtos[produto] = Produto(produto=produto,qtd=qtd, valor=valor)
    return produtos

##### IMPRIME NA TELA OS PRODUTOS
def imprime_produtos(produtos):
    while True:
        console.print(f"[bold purple]Produto[/bold purple][bold green]\t\t\tQuant[/bold green][bold blue]\t\t\tValor[/bold blue]", style="yellow")
        for produto in produtos.values():
            console.print(f"[bold purple]{produto.produto}[/bold purple][bold green]\t\t\t{produto.qtd}[/bold green][bold blue]\t\t\t{produto.valor}[/bold blue]")
        sair = Prompt.ask("[bold red]Sair? (s/N)[/bold red]")
        if (sair): 
            if (sair.lower() == "s") or (sair.lower() == "sim"):
                break
#### CADASTRAR PRODUTOS ######
# Função para cadastrar um novo produto.
# Parâmetros: 
#   usuarios (dict) - dicionário de usuários.
#   arquivo_csv (str) - caminho do arquivo CSV.
# Retorno: str - nome do novo produto ou False em caso de falha.
def cadastrar_produto(produtos, arquivo_csv):
    console.print(Panel('''[bold green]Cadastro de Novo Produto[/bold green]\nPor favor, insira os dados do novo Produto.''', 
                        title="Novo Usuário", expand=False))

    # Se usuario logado solicita o input dos dados, senão acusa erro e retorna falso
    if USUARIO_LOGADO is not None:
        produto_nome = Prompt.ask("[bold yellow]Nome do Produto[/bold yellow]")
        qtd = Prompt.ask("[bold cyan]Quantidade em estoque (inteiro)[/bold cyan]")
        valor = Prompt.ask("[bold cyan]Valor do produto (inteiro ou decimal ex: 19.49)[/bold cyan]")
        try:
            qtd=int(qtd)
            valor=float(valor)
        except ValueError:
            console.print(f"[bold red]Valor necessita ser inteiro ou decimal e quantidade ser inteiro[/bold red]")
            return False
            
    else:
        console.print(f"[bold]Apenas usuários logados podem inserir produtos![/bold]", style="red")
        return False
    
    if produtos.get(produto_nome, None) is not None:
        console.print(f"[bold red]Erro:[/bold red] Produto: '[bold red]{produto_nome}[/bold red]' já existe!", style="red")
        return False
    else: 
        with open(arquivo_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([produto_nome, qtd, valor]) 
        console.print(f"[bold green]Produto '{produto_nome}' cadastrado com sucesso![/bold green]")

    return produto_nome


##### CRUD Update
# Função para atualizar um produto.
# controle de acesso, permitindo apenas admins a atualizar valores e...
# quantidade de produts
# Parâmetros: 
#   usuarios (dict) - dicionário de produtos
#   arquivo_csv (str) - caminho do arquivo CSV.
# Retorno: bool - True se o produto foi atualizado com sucesso, False caso contrário.
def atualizar_produto(produtos, arquivo_csv):
    global USUARIO_LOGADO

    if (USUARIO_LOGADO is None):
        console.print(f"[bold red]Essa função apenas está disponível para usuários logados![/bold red]")
        return False
 
    if USUARIO_LOGADO.tipo != "admin":
        console.print(f"[bold red]Essa função só está disponível para usuário do tipo admin![/bold red]")
        return False
    produto_nome = Prompt.ask("[bold]Digite o nome do produto que deseja alterar[/bold]")
    if produtos.get(produto_nome, None) is not None:
        nova_qtd = Prompt.ask("[bold]Digite a nova quantidade (em inteiro)[/bold]")
        novo_valor = Prompt.ask("[bold]Digite o novo valor(inteiro, ou decimal ex: 8.01)[/bold]")
        try:
            nova_qtd=int(nova_qtd)
            novo_valor=float(novo_valor)
        except ValueError:
            console.print(f"[bold red]Valor necessita ser inteiro ou decimal e quantidade ser inteiro[/bold red]")
            return False
            
        with open(arquivo_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            for _, produto in produtos.items():
                if produto.produto != produto_nome:
                    writer.writerow([produto.produto, produto.qtd, produto.valor])
                else:
                    writer.writerow([produto_nome, nova_qtd, novo_valor])
            console.print(f"[bold green]Produto '{produto_nome}' alterado com sucesso![/bold green]")
            return True
    else:
        console.print(f"[bold yellow]Produto '{produto_nome}' não encontrado![/bold yellow]", style="yellow")
        return False
    
    
##### CRUD Delete
# Parâmetros: 
#   produtos (dict) - dicionário de produtos.
#   arquivo_csv (str) - caminho do arquivo CSV.
# Retorno: bool - True se o produto foi excluído com sucesso, False caso contrário.
def excluir_produto(produtos, arquivo_csv):
    console.print(Panel('''[bold red]Exclusão de Produtos[/bold red]\nPor favor, insira o nome do produto a ser excluído.''', 
                        title="Excluir Produto", expand=False))
    nome_produto = Prompt.ask("[bold cyan]Nome do Produto[/bold cyan]")

    # se encontrar o produto, remova do arquivo
    if produtos.get(nome_produto, None) is not None:
        with open(arquivo_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            for produto in produtos.values():
                if produto.produto != nome_produto:
                    writer.writerow([produto.produto, produto.qtd, produto.valor]) 
        console.print(f"[bold green]Produto '{nome_produto}' excluído com sucesso![/bold green]")
        return True
    else:
        console.print(f"[bold yellow]Produto '{nome_produto}' não encontrado![/bold yellow]", style="yellow")
        return False
  
#################### FUNÇÕES MENU DE USUÁRIO ########################
# Função para exibir o menu inicial.
# Retorno: str - opção escolhida pelo usuário.
def menu_inicial():
    console.print(Panel("[bold green]Sistema de Estoque![/bold green]\nEscolha uma das opções abaixo:", title="Menu Inicial", expand=False))
    console.print("[bold cyan]1.[/bold cyan] [bold white]Fazer Login[/bold white]")
    console.print("[bold cyan]2.[/bold cyan] [bold white]Cadastro[/bold white]")
    console.print("[bold cyan]3.[/bold cyan] [bold white]Sair do sistema[/bold white]")
    
    opcao = Prompt.ask("[bold yellow]Digite o número da opção desejada[/bold yellow]", choices=["1", "2", "3"])
    return opcao

# Função para exibir o menu interno.
# Retorno: str - opção escolhida pelo usuário.
def menu_interno():
    console.print(Panel(f"[bold green]Olá {USUARIO_LOGADO.login}![/bold green]\nEscolha uma das opções abaixo:", 
                        title="Menu Interno", expand=False))
    
    # controle de acesso para gerenciamento de usuários
    # admin pode atualizar ou excluir
    # users apenas atualizam (lógica interna para atualizar somente seu próprio cadastro)
    if USUARIO_LOGADO.tipo == 'admin':
        console.print("[bold cyan]1.[/bold cyan] [bold white]Atualizar cadastro[/bold white]")
        console.print("[bold cyan]2.[/bold cyan] [bold white]Excluir cadastro[/bold white]")
        console.print("[bold cyan]3.[/bold cyan] [bold white]Acessar Menu Produtos[/bold white]")
        console.print("[bold white]Para fazer logout digite[/bold white] [bold cyan]0[/bold cyan]")
        opcao = Prompt.ask("[bold yellow]Digite o número da opção desejada[/bold yellow]", choices=["0","1", "2", "3"])
    else:
        console.print("[bold cyan]1.[/bold cyan] [bold white]Atualizar cadastro[/bold white]")
        console.print("[bold cyan]3.[/bold cyan] [bold white]Acessar Menu Produtos[/bold white]")
        console.print("[bold white]Para fazer logout digite[/bold white] [bold cyan]0[/bold cyan]")
        opcao = Prompt.ask("[bold yellow]Digite o número da opção desejada[/bold yellow]", choices=["0","1","3"])
    return  opcao


############## MENU PRODUTOS ##########################################
def menu_produtos():
    console.print(Panel(f"[bold green]Olá {USUARIO_LOGADO.login}![/bold green]\nEscolha uma das opções abaixo:", 
                        title="Menu Produtos", expand=False))
    
    # controle de acesso para gerenciamento de produtos
    # admin pode atualizar ou excluir
    # users apenas atualizam (lógica interna para atualizar somente seu próprio cadastro)
    if USUARIO_LOGADO.tipo == 'admin':
        console.print("[bold cyan]1.[/bold cyan] [bold white]Visualizar Produtos[/bold white]")
        console.print("[bold cyan]2.[/bold cyan] [bold white]Cadastrar Produtos[/bold white]")
        console.print("[bold cyan]3.[/bold cyan] [bold white]Atualizar Produtos[/bold white]")
        console.print("[bold cyan]4.[/bold cyan] [bold white]Remover Produtos[/bold white]")
        console.print("[bold white]Para fazer retornar ao menu anterior digite[/bold white] [bold cyan]0[/bold cyan]")

        opcao = Prompt.ask("[bold yellow]Digite o número da opção desejada[/bold yellow]", choices=["0","1", "2","3","4"])
    else:
        console.print("[bold cyan]1.[/bold cyan] [bold white]Visualizar Produtos[/bold white]")
        console.print("[bold cyan]2.[/bold cyan] [bold white]Cadastrar Produtos[/bold white]")
        console.print("[bold white]Para fazer retornar ao menu anterior digite[/bold white] [bold cyan]0[/bold cyan]")

        opcao = Prompt.ask("[bold yellow]Digite o número da opção desejada[/bold yellow]", choices=["0","1","2"])
    return  opcao

##################### Fluxo principal do código ###################### 
console = Console()
usuarios = ler_usuarios(ARQUIVO_USUARIOS)
produtos = ler_produtos(ARQUIVO_PRODUTOS)
while True:
    opcao = menu_inicial()
    if opcao == "1":
        fazer_login(usuarios)
    elif opcao == "2":
        novo_user = cadastrar_usuario(usuarios, ARQUIVO_USUARIOS)
        if novo_user != False:
            usuarios = ler_usuarios(ARQUIVO_USUARIOS)
            USUARIO_LOGADO = usuarios.get(novo_user)
    elif opcao == "3": 
        break
    else:
        console.print(f"[bold yellow]Opção inválida![/bold yellow]", style="yellow")

    if USUARIO_LOGADO is not None:
        while True:
            opcao = menu_interno()
            if opcao == '0': break
            elif opcao == "1": 
                if atualiza_senha(usuarios, ARQUIVO_USUARIOS):
                    usuarios = ler_usuarios(ARQUIVO_USUARIOS)
            elif opcao == "2": 
                if excluir_usuario(usuarios, ARQUIVO_USUARIOS):
                    usuarios = ler_usuarios(ARQUIVO_USUARIOS)
            elif opcao == "3":
                while True:
                    opcao_produtos = menu_produtos()
                    match opcao_produtos:
                        case "1":
                            imprime_produtos(ler_produtos(ARQUIVO_PRODUTOS))
                        
                        case "2":
                            cadastrar_produto(produtos, ARQUIVO_PRODUTOS)
                            produtos=ler_produtos(ARQUIVO_PRODUTOS)
                        case "3":
                            atualizar_produto(produtos, ARQUIVO_PRODUTOS)
                            produtos=ler_produtos(ARQUIVO_PRODUTOS)
                        case "4":
                            excluir_produto(produtos, ARQUIVO_PRODUTOS)
                            produtos=ler_produtos(ARQUIVO_PRODUTOS)
                        case "0":
                            break
############################################################################
    